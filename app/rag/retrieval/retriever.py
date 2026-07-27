from langchain_core.documents import Document
from app.core.config import settings
from langchain_core.retrievers import BaseRetriever
from app.core.logger import logger
from app.rag.vectorstores.chroma import vector_store


class DenseRetriever:
    """
    Responsible for retrieving relevant
    documents from ChromaDB.
    """

    def __init__(self):
        self.retriever: BaseRetriever = (vector_store.vector_store.as_retriever(
            search_type=settings.SEARCH_TYPE,
            search_kwargs={
                "k": settings.TOP_K,
                "fetch_k": settings.FETCH_K,
                "lambda_mult": settings.MMR_LAMBDA,
            },
        )
    )
        
    async def retrieve(
        self,
        question: str,
    ) -> list[Document]:

        """
        Retrieve the most relevant documents for a user query
        using Maximum Marginal Relevance (MMR).
        """

        logger.info(
            "Retrieving relevant documents.",
            extra={
                "search_type": settings.SEARCH_TYPE,
                "top_k": settings.TOP_K,
            },
        )
        return await self.retriever.ainvoke(question)


dense_retriever = DenseRetriever()