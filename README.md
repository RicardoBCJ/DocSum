An API to summarize documents and extract key information.
Table of Contents

    Introduction
    Prerequisites
    Usage
    API Endpoints
    Troubleshooting
    Improvements and Future Work
    Dockerization (Optional)
    Contributing
    License

Introduction

This is an application that allows users to upload documents (PDF, DOCX, TXT, or images) and receive summarized content along with extracted entities using natural language processing techniques.
Prerequisites

    Python 3.10

    Virtual Environment (recommended)

    Poppler (for PDF to image conversion)

        Windows: Download from Poppler for Windows and add the bin folder to your PATH.

        macOS: Install via Homebrew:

        bash

        brew install poppler

    Git (optional, for cloning the repository)

1. Create and Activate a Virtual Environment

Windows:

bash

python -m venv env
env\Scripts\activate

macOS/Linux:

bash

python3 -m venv env
source env/bin/activate

2. Upgrade Pip and Setuptools

bash

pip install --upgrade pip setuptools

3. Install Dependencies

bash

pip install -r requirements.txt

4. Install NLTK Data

bash

python -c "import nltk; nltk.download('punkt')"

5. Install spaCy Language Model

bash

python -m spacy download en_core_web_sm

6. Set Up the Database

No additional steps are needed. The SQLite database will be automatically created when you run the application for the first time.

7. Run the Application

bash

uvicorn app.main:app --reload

8. Access the API Documentation

Open your web browser and navigate to:

http://127.0.0.1:8000/docs

Usage
Upload a Document

    Use the /upload endpoint to upload a document.
    Supported file types: .pdf, .docx, .txt, .png, .jpg, .jpeg.

Retrieve All Documents

    Use the /documents endpoint to get a list of all processed documents.
    Supports pagination and sorting.

Retrieve a Specific Document

    Use the /documents/{file_id} endpoint to get details of a specific document.
    Replace {file_id} with the actual file ID returned during the upload.

API Endpoints
/upload [POST]

    Description: Upload a document for summarization and entity extraction.
    Parameters:
    file: The file to upload.
    Response: JSON object containing the file_id.

/documents [GET]

    Description: Retrieve a list of processed documents.
    Parameters:
        skip: Number of records to skip (for pagination).
        limit: Maximum number of records to return.
        filename: Filter by filename.
        sort: Sort by upload_date or filename.
        order: Sort order asc or desc.
    Response: JSON array of documents.

/documents/{file_id} [GET]

    Description: Retrieve details of a specific document.
    Parameters:
        file_id: The unique identifier of the document.
    Response: JSON object containing document details.

Troubleshooting
Dependency Conflicts

    Ensure all dependencies are installed with compatible versions.
    Use the provided requirements.txt for reference.

Database Errors

    If you encounter database schema errors, you may need to apply migrations or recreate the database.
    Recreating the Database:
        Delete the docdigest.db file.
        Restart the application to recreate the database.

Poppler Issues

    Ensure Poppler is correctly installed and added to your system's PATH.
    Verify by running pdftoppm -h in your command line.

Next Steps:
Implementation of custom ocr
Create a front end for the site

License

This project is licensed under the MIT License.
