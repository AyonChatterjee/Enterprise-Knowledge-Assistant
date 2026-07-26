from fastapi import APIRouter, UploadFile, File, HTTPException

from app.schemas.upload import UploadResponse
from app.services.upload_service import upload_service

router = APIRouter(
    prefix="/upload",
    tags=["Upload"]
)


@router.post(
    "/",
    response_model=UploadResponse
)
async def upload_pdf(
    file: UploadFile = File(...)
):
    """
    Upload a PDF document.
    """

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    return await upload_service.save_pdf(file)