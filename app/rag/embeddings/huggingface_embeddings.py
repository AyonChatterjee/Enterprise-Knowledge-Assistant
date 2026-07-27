from langchain_huggingface import HuggingFaceEmbeddings
from app.core.config import settings
class EmbeddingService:
    """
    Embedding service using a local HuggingFace model.
    """

    def __init__(self):
        self.embedding_model = HuggingFaceEmbeddings(
            model_name=settings.EMBEDDING_MODEL,
            model_kwargs={
                "device": "cpu"
            },
            encode_kwargs={
                "normalize_embeddings": True
            }
        )

    @property
    def model(self):
        return self.embedding_model


embedding_service = EmbeddingService()