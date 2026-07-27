from typing import Any

from pydantic import BaseModel

class ChunkPreview(BaseModel):
    """
    Represents a preview of one chunk.
    """

    page_content: str

    metadata: dict[str ,  Any]


class UploadResponse(BaseModel):
    """
    Response returned after a successful upload.
    """

    filename: str

    path: str

    status: str

    pages: int

    chunks: int

    preview: list[ChunkPreview]