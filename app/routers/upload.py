# app/routers/upload.py

from fastapi import APIRouter, UploadFile, File, HTTPException
from fastapi.responses import JSONResponse
import os
import uuid

router = APIRouter()

# Allowed file extensions
ALLOWED_EXTENSIONS = {'pdf', 'docx', 'txt'}

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@router.post("/upload")
async def upload_file(file: UploadFile = File(...)):
    if not allowed_file(file.filename):
        raise HTTPException(status_code=400, detail="Unsupported file type.")

    file_extension = file.filename.rsplit('.', 1)[1].lower()
    unique_id = str(uuid.uuid4())
    saved_filename = f"{unique_id}.{file_extension}"
    file_location = f"data/{saved_filename}"

    with open(file_location, "wb") as buffer:
        buffer.write(await file.read())

    return JSONResponse(content={"file_id": unique_id, "filename": file.filename})
