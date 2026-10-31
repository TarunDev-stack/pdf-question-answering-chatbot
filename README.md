# 📄 PDF Question Answering Chatbot

A **Retrieval-Augmented Generation (RAG)** application that allows users to upload PDF documents and ask questions about their content using natural language.

The application extracts text from the uploaded PDF, splits it into smaller chunks, converts those chunks into vector embeddings, and stores them in a FAISS vector database. When a user asks a question, the system retrieves the most relevant content and uses a language model to generate a context-aware answer.

## ✨ Features

- **PDF Upload:** Upload PDF documents directly through the Streamlit interface.
- **Text Extraction:** Extract text from PDF files using PyMuPDF.
- **Text Chunking:** Split extracted text into manageable chunks with overlapping context.
- **Semantic Search:** Generate embeddings using Sentence Transformers.
- **Vector Database:** Store and retrieve document embeddings using FAISS.
- **AI-Powered Answers:** Generate answers using Google's FLAN-T5 language model.
- **Interactive Interface:** Ask questions through a simple Streamlit web application.

## 🏗️ System Architecture

```text
             PDF Upload
                  |
                  v
          Text Extraction
             (PyMuPDF)
                  |
                  v
            Text Chunking
         (LangChain Splitter)
                  |
                  v
          Generate Embeddings
       (Sentence Transformers)
                  |
                  v
          FAISS Vector Store
                  |
                  |
             User Question
                  |
                  v
          Query Embedding
                  |
                  v
       Similarity-Based Retrieval
                  |
                  v
          Relevant Context
                  |
                  v
          FLAN-T5 Language Model
                  |
                  v
             Final Answer
```

## 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Core programming language |
| Streamlit | Web application interface |
| LangChain | Retrieval-based QA pipeline |
| PyMuPDF | PDF text extraction |
| Sentence Transformers | Text embedding generation |
| FAISS | Vector storage and similarity search |
| Hugging Face Transformers | Language model integration |
| FLAN-T5 Base | Context-aware answer generation |

## 📁 Project Structure

```text
PDF-QA-Chatbot/
│
├── app.py              # Streamlit application
├── ingest.py           # PDF extraction, chunking and indexing
├── qa_chain.py         # Retrieval and question-answering pipeline
├── requirements.txt    # Python dependencies
├── .gitignore          # Files excluded from Git
└── README.md           # Project documentation
```

## ⚙️ Installation and Setup

### 1. Clone the repository

```bash
git clone https://github.com/TarunDev-stack/pdf-question-answering-chatbot.git
```

### 2. Navigate to the project directory

```bash
cd pdf-question-answering-chatbot
```

### 3. Create a virtual environment

```bash
python -m venv venv
```

### 4. Activate the virtual environment

**Windows (PowerShell):**

```powershell
.\venv\Scripts\Activate.ps1
```

**Windows (Command Prompt):**

```cmd
venv\Scripts\activate
```

### 5. Install dependencies

```bash
pip install -r requirements.txt
```

Make sure `langchain-text-splitters` is also included in `requirements.txt`, as it is used by the PDF ingestion module.

### 6. Run the application

```bash
streamlit run app.py
```

The application will open in your browser, usually at:

```text
http://localhost:8501
```

*Note: The embedding model and FLAN-T5 model are downloaded from Hugging Face when first needed. An internet connection is required for the initial download.*

## 🚀 How to Use

1. Start the application using Streamlit.
2. Upload a PDF document using the file uploader.
3. Wait for the document to be processed.
4. Enter a question related to the uploaded document.
5. View the generated answer on the application interface.
6. Ask additional questions about the uploaded document.

## 🧠 Models and Configuration

**Embedding Model**

`sentence-transformers/all-MiniLM-L6-v2`

Used to convert document chunks and user questions into dense vector representations for semantic similarity search.

**Language Model**

`google/flan-t5-base`

Used to generate natural-language answers using the relevant context retrieved from the document.

**Text Chunking Configuration**

- Chunk size: 1000 characters
- Chunk overlap: 200 characters

## 🔍 How RAG Works in This Project

Retrieval-Augmented Generation (RAG) combines information retrieval with language generation.

This application follows three main steps:

1. **Retrieval:** The user's question is converted into an embedding, and FAISS searches for semantically similar document chunks.
2. **Augmentation:** The retrieved chunks are supplied as context to the language model.
3. **Generation:** FLAN-T5 generates an answer based on the retrieved context and the user's question.

This approach helps the language model answer questions using information from the uploaded document rather than relying only on its pre-trained knowledge.

## ⚠️ Current Limitations

- Designed to process one uploaded PDF at a time.
- Text-based PDFs are supported; scanned documents may require OCR.
- Answer quality depends on the quality of the extracted text and retrieved chunks.
- Large PDFs and language models may require additional memory and processing time.

## 🔮 Future Improvements

- Support multiple PDF documents simultaneously.
- Display source page numbers and relevant document references.
- Add conversation history for follow-up questions.
- Integrate larger or more capable language models.
- Add OCR support for scanned PDF documents.
- Optimize model loading and document processing.

## 👨‍💻 Author

**Tarun Dev**

GitHub: [TarunDev-stack](https://github.com/TarunDev-stack)

---

⭐ If you find this project useful, consider giving the repository a star!
