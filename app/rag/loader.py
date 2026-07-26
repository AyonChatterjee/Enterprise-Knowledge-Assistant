from pathlib import Path

import fitz  # PyMuPDF


class PDFLoader:
    """
    Responsible for extracting text and metadata from PDF documents.
    """

    def load(self, pdf_path: str) -> list[dict]:
        """
        Extract text from every page of a PDF.

        Returns:
            List of page dictionaries.
        """

        document = fitz.open(pdf_path)

        pages = []

        for page_number, page in enumerate(document, start=1):

            text = page.get_text("text")

            pages.append(
                {
                    "page": page_number,
                    "text": text,
                    "source": Path(pdf_path).name,
                }
            )

        document.close()

        return pages


pdf_loader = PDFLoader()