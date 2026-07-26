from pathlib import Path
import shutil

from fastapi import UploadFile

from app.core.config import settings


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

        return {
            "filename": file.filename,
            "path": str(file_path),
            "status": "uploaded"
        }


upload_service = UploadService()