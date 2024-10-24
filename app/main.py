from fastapi import FastAPI

app = FastAPI(
    title="DocDigest - Legal Document Summarizer",
    description="An API to summarize legal documents and extract key information.",
    version="1.0.0"
)

@app.get("/")
async def root():
    return {"message": "Welcome to DocDigest API"}