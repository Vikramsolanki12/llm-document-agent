from fastapi import APIRouter, UploadFile, File
import shutil
import os

from app.services.document_pipeline import process_document

router = APIRouter()

UPLOAD_DIR = "documents"

os.makedirs(UPLOAD_DIR, exist_ok=True)

@router.post("/upload")
async def upload_document(file: UploadFile = File(...)):

    try:

        print("\nUploading Started...\n")

        file_path = f"{UPLOAD_DIR}/{file.filename}"

        # Save file
        with open(file_path, "wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        print(f"File Saved: {file_path}")

        # Process document
        result = process_document(file_path)

        print("Document Processing Completed")

        return {
            "message": "Document uploaded successfully",
            "result": result
        }

    except Exception as e:

        print("\nUPLOAD ERROR:\n")
        print(str(e))

        return {
            "error": str(e)
        }