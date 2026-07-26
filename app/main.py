from fastapi import FastAPI

from app.api.upload import router as upload_router
from app.core.config import settings
from app.core.logger import logger

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.APP_VERSION,
)

app.include_router(upload_router)


@app.get("/")
def root():

    logger.info("Root endpoint accessed.")

    return {
        "message": "Welcome to Enterprise Knowledge Assistant 🚀"
    }


@app.get("/health")
def health():

    logger.info("Health check.")

    return {
        "status": "healthy"
    }