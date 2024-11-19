# Project Link

### [https://swapnilbpatil-chat-withpdf.hf.space/](https://swapnilbpatil-chat-withpdf.hf.space/)


# Chat with PDF  📑

This project is a robust tool designed to allow users to upload one or more PDFs, query their content, and receive precise answers. By leveraging natural language processing (NLP) techniques, it provides an efficient way to interact with and extract meaningful insights from large documents.

---
![image](https://github.com/user-attachments/assets/dc884ab7-b7fc-43a3-8633-4a23ee90dded)
---
## Features

- **Upload Multiple PDFs**: Add one or more PDF documents to the system.
- **Intelligent Question Answering**: Ask any question, and the tool will extract and return relevant answers based on the uploaded PDFs.
- **Search Across Multiple PDFs**: Combines content from all uploaded documents to provide comprehensive answers.
- **User-Friendly Interface**: Simple and intuitive design for seamless interaction.

---

# Workflow Explanation


![rag](https://github.com/user-attachments/assets/05cde9c3-76bd-4107-82b9-c8ace5563053)


## Steps:

### 1. **User Input (Prompt)**  
   - The user provides a query or a prompt.  
   - This input is processed by a **Question Encoder**, which converts the text into a vector (a numerical representation of the input).

---

### 2. **Document/Data Encoding**  
   - The system processes the documents or stored data using a **Context Encoder**.  
   - The Context Encoder transforms the documents into vectors that represent their meaning in a machine-readable format.  
   - These encoded vectors are stored in a **Vector Database (Vector DB)** for easy retrieval.

---

### 3. **Retrieving Relevant Information**  
   - The system compares the vector from the user’s question with the vectors stored in the database.  
   - It retrieves the most relevant context or data based on similarity.

---

### 4. **Combining Prompt and Context**  
   - The retrieved context is combined with the original query (prompt).  
   - This step ensures the response is enriched with relevant information from the database.

---

### 5. **Response Generation**  
   - The enriched input (prompt + context) is passed to a chatbot or a response generation model.  
   - The chatbot generates a response tailored to the user’s query based on the retrieved context.

---

## Key Features:
- **Efficient Retrieval**: The system uses vector-based matching to find relevant information quickly.  
- **Flexible Understanding**: Even if the query wording differs from the stored data, the vector representation ensures the correct match.  
- **Accurate Responses**: By combining user input with retrieved context, the system provides meaningful and precise answers.

---

### Workflow Diagram:
Refer to the workflow diagram for a visual representation of the process.


---
