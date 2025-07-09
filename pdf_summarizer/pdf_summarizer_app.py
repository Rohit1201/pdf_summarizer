import streamlit as st
from summarizer import read_pdf, summarize_text

st.set_page_config(page_title="PDF Summarizer", layout="centered")
st.title("📄 PDF Summarizer")

uploaded_file = st.file_uploader("Upload a PDF file", type=["pdf"])

if uploaded_file:
    max_chars = st.slider("Limit content for summarization (chars)", min_value=500, max_value=10000, value=3000)
    
    if st.button("Generate Summary"):
        with st.spinner("Summarizing PDF..."):
            text = read_pdf(uploaded_file, max_chars=max_chars)
            summary = summarize_text(text)
            st.subheader("📚 Summary:")
            st.markdown(summary)
