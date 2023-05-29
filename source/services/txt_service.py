from os import path

from source.services.file_service import FileService


class TxtService(FileService):
    @staticmethod
    def read(file_path: str) -> str:
        print("read - started")

        if not path.exists(file_path):
            raise Exception(f"file not found. Path {file_path}")

        with open(file_path, 'r', encoding="utf-8") as f:
            return f.read()
