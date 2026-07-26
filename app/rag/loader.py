from pathlib import Path

import fitz
from langchain_core.documents import Document


class PDFLoader:
    """
    Loads PDF files and converts every page into
    LangChain Document objects.
    """

    def load(self, pdf_path: str) -> list[Document]:

        pdf = fitz.open(pdf_path)

        documents = []

        source = Path(pdf_path).name

        for page_number, page in enumerate(pdf, start=1):

            text = page.get_text()

            if not text.strip():
                continue

            document = Document(
                page_content=text,
                metadata={
                    "page": page_number,
                    "source": source,
                },
            )

            documents.append(document)

        pdf.close()

        return documents


pdf_loader = PDFLoader()