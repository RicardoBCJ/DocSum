# app/main.py

from fastapi import FastAPI
from app.routers import upload, documents
from app.models.database import engine, Base
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(
    title="DocSum",
    description="An API to test AI development.",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:3000"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

Base.metadata.create_all(bind=engine)


app.include_router(upload.router, tags=["File Upload"])
app.include_router(documents.router, tags=["Documents"])

@app.get("/")
async def root():
    return {"message": "Welcome to DocDigest API"}
