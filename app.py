import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import RecursiveCharacterTextSplitter
import os
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv

# Import ChatGroq instead of ChatGoogleGenerativeAI
from langchain_groq import ChatGroq

# Load environment variables
load_dotenv()
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
GROQ_API_KEY = os.getenv("GROQ_API_KEY")  # It's better to store your Groq API key in .env

# Configure Google Generative AI
import google.generativeai as genai
genai.configure(api_key=GOOGLE_API_KEY)

# Initialize the LLM using ChatGroq
llm = ChatGroq(
    temperature=0,
    groq_api_key=GROQ_API_KEY,  # Use the Groq API key from environment variables
    model_name="llama-3.1-70b-versatile"
)

def get_pdf_text(pdf_docs):
    text = ""
    for pdf in pdf_docs:
        pdf_reader = PdfReader(pdf)
        for page in pdf_reader.pages:
            extracted_text = page.extract_text()
            if extracted_text:
                text += extracted_text
    return text

def get_text_chunks(text):
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=10000, chunk_overlap=1000)
    chunks = text_splitter.split_text(text)
    return chunks

def get_vector_store(text_chunks):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    vector_store = FAISS.from_texts(text_chunks, embedding=embeddings)
    vector_store.save_local("faiss_index")

def get_conversational_chain():
    prompt_template = """
    Answer the question as detailed as possible from the provided context. Make sure to provide all the details. 
    If the answer is not in the provided context, just say, "Answer is not available in the context." 
    Don't provide the wrong answer.

    Context:
    {context}

    Question:
    {question}

    Answer:
    """

    prompt = PromptTemplate(template=prompt_template, input_variables=["context", "question"])
    
    # Use the ChatGroq instance instead of ChatGoogleGenerativeAI
    chain = load_qa_chain(llm, chain_type="stuff", prompt=prompt)

    return chain

def user_input(user_question):
    embeddings = GoogleGenerativeAIEmbeddings(model="models/embedding-001")
    
    # Load the existing FAISS vector store
    new_db = FAISS.load_local("faiss_index", embeddings, allow_dangerous_deserialization=True)
    docs = new_db.similarity_search(user_question)

    chain = get_conversational_chain()

    response = chain(
        {"input_documents": docs, "question": user_question},
        return_only_outputs=True
    )

    print(response)
    st.write("Reply: ", response.get("output_text", "No response generated."))

def main():
    st.set_page_config(page_title=" 📝 Chat withPDF ")
    st.header("Chat with PDF 📝")

    user_question = st.text_input("Ask a Question from the PDF Files")

    if user_question:
        user_input(user_question)

    with st.sidebar:
        st.title("Menu:")
        pdf_docs = st.file_uploader(
            "Upload your PDF Files and Click on the Submit & Process Button",
            accept_multiple_files=True,
            type=["pdf"]
        )
        if st.button("Submit & Process"):
            if not pdf_docs:
                st.warning("Please upload at least one PDF file.")
                return
            with st.spinner("Processing..."):
                raw_text = get_pdf_text(pdf_docs)
                if not raw_text:
                    st.error("No text found in the uploaded PDF files.")
                    return
                text_chunks = get_text_chunks(raw_text)
                get_vector_store(text_chunks)
                st.success("Processing completed successfully!")

if __name__ == "__main__":
    main()
