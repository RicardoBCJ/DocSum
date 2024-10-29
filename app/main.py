# app/main.py

from fastapi import FastAPI
from app.routers import upload, documents
from app.models.database import engine, Base

app = FastAPI(
    title="DocDigest - Document Summarizer",
    description="An API to summarize documents and extract key information.",
    version="0.1.0"
)

Base.metadata.create_all(bind=engine)


app.include_router(upload.router, tags=["File Upload"])
app.include_router(documents.router, tags=["Documents"])

@app.get("/")
async def root():
    return {"message": "Welcome to DocDigest API"}
