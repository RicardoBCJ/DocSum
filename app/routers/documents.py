# app/routers/documents.py

from fastapi import APIRouter, HTTPException, Depends, Query
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models import models
from sqlalchemy import desc
import json

router = APIRouter()


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def get_document(file_id: str, db: Session = Depends(get_db)):
    document = db.query(models.Document).filter(models.Document.file_id == file_id).first()
    if document is None:
        raise HTTPException(status_code=404, detail="Document not found")

    return {
        "file_id": document.file_id,
        "filename": document.filename,
        "summary": document.summary,
        "entities": json.loads(document.entities)
    }

# New endpoint to get all documents with pagination
@router.get("/documents")
def get_documents(
    skip: int = Query(0, ge=0),
    limit: int = Query(10, ge=1),
    filename: str = None,
    sort: str = Query("upload_date", regex="^(upload_date|filename)$"),
    order: str = Query("desc", regex="^(asc|desc)$"),
    db: Session = Depends(get_db)
):
    query = db.query(models.Document)

    if filename:
        query = query.filter(models.Document.filename.contains(filename))

    if sort == "upload_date":
        sort_column = models.Document.upload_date
    else:
        sort_column = models.Document.filename

    if order == "desc":
        query = query.order_by(desc(sort_column))
    else:
        query = query.order_by(sort_column)

    documents = query.offset(skip).limit(limit).all()
    results = []
    for document in documents:
        results.append({
            "file_id": document.file_id,
            "filename": document.filename,
            "summary": document.summary,
            "entities": json.loads(document.entities)
        })
    return results