from fastapi import APIRouter, File, HTTPException, UploadFile

from app.services.upload_service import upload_service

router = APIRouter(prefix="/upload", tags=["Upload"])


@router.post("/")
async def upload_pdf(file: UploadFile = File(...)):
    """
    Upload a PDF document.
    """

    if not file.filename.endswith(".pdf"):
        raise HTTPException(
            status_code=400,
            detail="Only PDF files are allowed."
        )

    result = await upload_service.save_pdf(file)

    return result