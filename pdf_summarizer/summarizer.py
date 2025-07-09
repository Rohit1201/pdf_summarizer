import os
from PyPDF2 import PdfReader
from langchain.chat_models import ChatOpenAI
from langchain.schema import SystemMessage, HumanMessage
from dotenv import load_dotenv

load_dotenv()
openai_api_key = os.getenv("OPENAI_API_KEY")

def read_pdf(file, max_chars=3000):
    pdf_reader = PdfReader(file)
    text = ""
    for page in pdf_reader.pages:
        page_text = page.extract_text()
        if page_text:
            text += page_text
    return text[:max_chars]

def summarize_text(text, model="gpt-4o"):
    llm = ChatOpenAI(
        model=model,
        temperature=0.3,
        openai_api_key=openai_api_key
    )

    messages = [
        SystemMessage(content="You are a helpful assistant that summarizes PDF documents clearly and concisely."),
        HumanMessage(content=f"Please summarize the following PDF content:\n\n{text}")
    ]

    response = llm(messages)
    return response.content
