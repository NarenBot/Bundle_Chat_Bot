import os
import google.generativeai as genai
import streamlit as st
from dotenv import load_dotenv
from src.components.chat_with_pdf import ChatPDF

load_dotenv()

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))


st.set_page_config("Chat with PDF")
st.title("Bundle-Chat-Bot")
st.header("Chat-PDF-Application")

chat = ChatPDF()

question = st.text_input("Ask a question within the PDF")
if question:
    response = chat.get_user_input(question=question)
    st.subheader("Response:")
    st.write(response["output_text"])


with st.sidebar:
    st.title("Menu:")
    pdf_docs = st.file_uploader(
        "Upload your PDF files and click on Submit & Process button.",
        accept_multiple_files=True,
    )
    if st.button("Submit & Process"):
        with st.spinner("Processing..."):
            text = chat.get_pdf_text(pdf_docs=pdf_docs)
            chunks = chat.get_text_chunks(text=text)
            chat.get_vector_stores(chunks=chunks)
            st.success("Done")
