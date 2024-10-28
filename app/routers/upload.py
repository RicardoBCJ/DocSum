# app/routers/upload.py

from fastapi import APIRouter, UploadFile, File, HTTPException, Depends
from fastapi.responses import JSONResponse
import os
import uuid
from app.utils.file_processing import extract_text
from app.utils.nlp_processing import extract_entities, generate_summary
from sqlalchemy.orm import Session
from app.models.database import SessionLocal
from app.models import models
import json

router = APIRouter()

ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt', 'png', 'jpg', 'jpeg'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

# Dependency to get DB session
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.post("/upload")
async def upload_file(file: UploadFile = File(...), db: Session = Depends(get_db)):
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Unsupported file type.")

    file_extension = file.filename.rsplit('.', 1)[1].lower()
    unique_id = str(uuid.uuid4())
    saved_filename = f"{unique_id}.{file_extension}"
    file_location = f"data/{saved_filename}"

    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    try:
        text = await extract_text(file_location)
    except Exception as e:
        os.remove(file_location)
        raise HTTPException(status_code=500, detail=str(e))

    # Process text with NLP
    entities = extract_entities(text)
    summary = generate_summary(text)

    # Store data in the database
    document = models.Document(
        file_id=unique_id,
        filename=file.filename,
        text=text,
        summary=summary,
        entities=json.dumps(entities)
    )
    db.add(document)
    db.commit()
    db.refresh(document)

    return JSONResponse(content={"file_id": unique_id, "filename": file.filename})
