from langchain_core.documents import Document
from langchain_text_splitters import RecursiveCharacterTextSplitter

from app.core.config import settings


class DocumentSplitter:

    def __init__(self):

        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=settings.CHUNK_SIZE,
            chunk_overlap=settings.CHUNK_OVERLAP,
            separators=[
                "\n\n",
                "\n",
                ". ",
                " ",
                "",
            ],
        )

    def split_documents(
        self,
        documents: list[Document],
    ) -> list[Document]:

        return self.text_splitter.split_documents(documents)


document_splitter = DocumentSplitter()