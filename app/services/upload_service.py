from pathlib import Path
import shutil

from fastapi import UploadFile

from app.core.config import settings
from app.rag.loader import pdf_loader


class UploadService:
    """
    Handles document upload operations.
    """

    def __init__(self):
        self.upload_directory = Path(settings.DATA_DIRECTORY)
        self.upload_directory.mkdir(parents=True, exist_ok=True)

    async def save_pdf(self, file: UploadFile) -> dict:
        """
        Save the uploaded PDF to disk.
        """

        file_path = self.upload_directory / file.filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        pages = pdf_loader.load(str(file_path))

        return {
            "filename": file.filename,
            "pages": len(pages),
            "path": str(file_path),
            "status": "uploaded" , 
            "preview": pages[:2]  # Return the first two pages as a preview
        }


upload_service = UploadService()