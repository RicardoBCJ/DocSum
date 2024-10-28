# app/models/models.py

from sqlalchemy import Column, Integer, String, Text
from app.models.database import Base
from sqlalchemy import Column, Integer, String, Text, DateTime
from datetime import datetime

class Document(Base):
    __tablename__ = 'documents'

    id = Column(Integer, primary_key=True, index=True)
    file_id = Column(String, unique=True, index=True)
    filename = Column(String)
    text = Column(Text)
    summary = Column(Text)
    entities = Column(Text)
    upload_date = Column(DateTime, default=datetime.utcnow)