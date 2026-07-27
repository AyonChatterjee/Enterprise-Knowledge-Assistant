from pathlib import Path
import shutil

from fastapi import UploadFile

from app.core.config import settings
from app.rag.ingestion.loader import pdf_loader
from app.rag.ingestion.splitter import document_splitter
from app.schemas.upload import UploadResponse, ChunkPreview
from app.rag.vectorstore.chroma import vector_store

class UploadService:
    """
    Handles document upload operations.
    """

    def __init__(self):
        self.upload_directory = Path(settings.DATA_DIRECTORY)
        self.upload_directory.mkdir(parents=True, exist_ok=True)

    async def save_pdf(self, file: UploadFile) -> UploadResponse:
        """
        Save the uploaded PDF to disk.
        """

        file_path = self.upload_directory / file.filename

        with file_path.open("wb") as buffer:
            shutil.copyfileobj(file.file, buffer)

        documents = pdf_loader.load(str(file_path))
        chunks = document_splitter.split_documents(documents)
        vector_store.add_documents(chunks)

        return UploadResponse(
          filename=file.filename,
          path=str(file_path),
          status="uploaded",
          pages=len(documents),
          chunks=len(chunks),
          preview=[
              ChunkPreview(
              page_content=chunk.page_content[:250],
              metadata=chunk.metadata,
        )
        for chunk in chunks[:3]
    ],
)


upload_service = UploadService()