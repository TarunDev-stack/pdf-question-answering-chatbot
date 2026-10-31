# import streamlit as st
# from qa_chain import load_qa_chain

# st.title("📄 PDF QA Chatbot")
# st.write("Ask questions based on the uploaded PDF")

# qa_chain = load_qa_chain()

# query = st.text_input("Enter your question:")
# if query:
#     with st.spinner("Searching for answers..."):
#         response = qa_chain({"query": query})
#         st.success(response["result"])


import streamlit as st
from qa_chain import load_qa_chain
from ingest import read_pdf, split_text, create_vectorstore

st.set_page_config(
    page_title="PDF QA Chatbot",
    page_icon="📄",
    layout="centered"
)

st.title("📄 PDF Question Answering Chatbot")
st.write("Upload a PDF and ask questions about its content.")

# PDF Upload
uploaded_file = st.file_uploader(
    "Upload your PDF",
    type=["pdf"]
)

if uploaded_file is not None:

    with open("uploaded.pdf", "wb") as f:
        f.write(uploaded_file.getbuffer())

    with st.spinner("Processing PDF..."):

        raw_text = read_pdf("uploaded.pdf")
        chunks = split_text(raw_text)
        create_vectorstore(chunks)

    st.success("PDF processed successfully!")

    # Load RAG pipeline
    qa_chain = load_qa_chain()

    question = st.text_input("Ask a question about your PDF:")

    if question:
        with st.spinner("Generating answer..."):
            response = qa_chain.invoke({"query": question})

        st.success(response["result"])