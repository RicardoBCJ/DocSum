from fastapi import FastAPI
from fastapi import FastAPI
from app.routers import upload

app = FastAPI(
    title="DocDigest - Legal Document Summarizer",
    description="An API to summarize legal documents and extract key information.",
    version="1.0.0"
)

app.include_router(upload.router, tags=["File Upload"])

@app.get("/")
async def root():
    return {"message": "Welcome to DocDigest API"}