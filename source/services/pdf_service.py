from os import path

import fitz

from source.services.file_service import FileService


class PdfService(FileService):
    @staticmethod
    def read(file_path: str) -> str:
        print("get_text_from_pdf - started")

        if not path.exists(file_path):
            raise Exception("file not found")

        doc = fitz.open(file_path)
        text = ""

        for page in doc:
            text += page.get_text()

        return text
