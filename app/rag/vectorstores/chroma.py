from langchain_chroma import Chroma
from app.core.config import settings
from app.rag.embeddings.huggingface_embeddings import embedding_service


class ChromaVectorStore:
    """
    Handles all interactions with ChromaDB.
    """

    def __init__(self):
        self.vector_store = Chroma(
            collection_name="enterprise_documents",
            embedding_function=embedding_service.model,
            persist_directory=settings.CHROMA_DB_PATH,
        )

    def add_documents(self, documents):
        """
        Add documents to the vector database.
        """
        self.vector_store.add_documents(documents)

    def similarity_search(self, query: str, k: int = 5):
        """
        Search for similar documents.
        """
        return self.vector_store.similarity_search(query, k=k)


vector_store = ChromaVectorStore()

