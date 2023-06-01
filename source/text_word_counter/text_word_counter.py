import operator
from collections import Counter
from pathlib import Path
from typing import List, Dict

from source.services.excel_service import ExcelService
from source.services.file_service import FileService
from source.services.pdf_service import PdfService
from source.services.text_cleaning_service import TextCleaningService
from source.services.txt_service import TxtService

LANGUAGE = "en_US"


class TextWordCounter:
    def get_words_count_and_save_to_excel(self,
                                          file_path: str,
                                          excel_file_path: str,
                                          only_english: bool,
                                          words_to_remove_file_path: str = None) -> None:
        print("get_words_count_and_save_to_excel - started")

        data = self.get_words_count(file_path, only_english, words_to_remove_file_path)
        sheet_name = file_path.split("/")[-1]

        ExcelService.write(data, excel_file_path, sheet_name)

    def get_words_count(self,
                        file_path: str,
                        only_english: bool,
                        words_to_remove_file_path: str = None) -> Dict[str, int]:
        print("get_words_count - started")

        file_service = self._get_file_service(file_path)
        data = file_service.read(file_path)
        data = TextCleaningService.remove_punctuations(data)
        data = TextCleaningService.remove_digits(data)
        data = TextCleaningService.remove_single_letters(data)
        data = self._get_list_of_words_from_string(data)

        if only_english:
            data = TextCleaningService.remove_all_non_english_words(data, LANGUAGE)

            self._save_temp_cleaned_file(data)

        data = self._get_count_of_words(data)
        data = TextCleaningService.clean_custom_word(data, words_to_remove_file_path)

        return data

    def _save_temp_cleaned_file(self, data: List[str]) -> None:
        print("save_temp_cleaned_file - started")

        with open(r"data\temp_result.txt", "a", encoding="utf-8") as f:
            f.write("\n".join(data))

    def _get_file_service(self, file_path: str) -> FileService or Exception:
        print("get_file_reader - started")
        suffix = Path(file_path, encoding="utf-8").suffix

        if suffix == ".pdf":
            return PdfService

        if suffix == ".txt":
            return TxtService

        raise Exception(f"File extension {suffix} is not supported")

    def _get_list_of_words_from_string(self, text: str) -> List[str]:
        print("get_list_of_word_from_string - started")

        list_of_words = text.lower().split()

        print(f"number of words in a book: {len(list_of_words)}")

        return list_of_words

    def _get_count_of_words(self, text: List[str]) -> Dict[str, int]:
        print("get_count_of_words - started")

        words_by_count = Counter(text)
        words_by_count = dict(sorted(words_by_count.items(), key=operator.itemgetter(1), reverse=True))

        return words_by_count
