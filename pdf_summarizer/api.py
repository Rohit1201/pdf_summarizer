from fastapi import FastAPI, UploadFile, File, HTTPException
from pdf_summarizer.summarizer import read_pdf, summarize_text
import uvicorn

app = FastAPI(title="PDF Summarizer API")

@app.post("/summarize")
async def summarize_pdf(file: UploadFile = File(...)):
    if not file.filename.endswith(".pdf"):
        raise HTTPException(status_code=400, detail="Only PDF files are supported.")

    contents = await file.read()
    summary = summarize_text(read_pdf(contents))
    return {"summary": summary}

if __name__ == "__main__":
    uvicorn.run("api:app", host="0.0.0.0", port=8000, reload=True)
