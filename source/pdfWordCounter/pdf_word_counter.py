import operator
import string
from collections import Counter
from os import path
from typing import List, Dict

import fitz
import pandas as pd
from stopwords import clean


class PdfWordCounter:
    def get_words_count_from_pdf_and_save_to_excel(self,
                                                   pdf_file_path: str,
                                                   excel_file_path: str,
                                                   language: str = "en",
                                                   words_to_remove_file_path: str = None) -> None:

        data = self.get_words_count_from_pdf(pdf_file_path, language, words_to_remove_file_path)
        sheet_name = pdf_file_path.split("/")[-1]

        self.save_results_to_excel(data, excel_file_path, sheet_name)

    def get_words_count_from_pdf(self,
                                 pdf_file_path: str,
                                 language: str = "en",
                                 words_to_remove_file_path: str = None) -> Dict[str, int]:
        data = self._get_text_from_pdf(pdf_file_path)
        data = self._remove_punctuations(data)
        data = self._remove_digits(data)
        data = self._get_list_of_words_from_string(data)
        data = self._clean_stopword(data, language)
        data = self._get_count_of_words(data)
        data = self._clean_custom_word(data, words_to_remove_file_path)

        return data

    def _get_text_from_pdf(self, pdf_file_path: str) -> str:
        print("get_text_from_pdf - started")

        doc = fitz.open(pdf_file_path)
        text = ""

        for page in doc:
            text += page.get_text()

        return text

    def _remove_punctuations(self, text: str) -> str:
        print("remove_punctuations - started")

        custom_punctuations = "‘©–"
        translating = str.maketrans('', '', string.punctuation + custom_punctuations)

        return text.translate(translating)

    def _remove_digits(self, text: str) -> str:
        print("remove_digits - started")

        translating = str.maketrans('', '', string.digits)

        return text.translate(translating)

    def _get_list_of_words_from_string(self, text: str) -> List[str]:
        print("get_list_of_word_from_string - started")

        list_of_words = text.lower().split()

        print(f"number of words in a book: {len(list_of_words)}")

        return text.lower().split()

    def _clean_stopword(self, list_of_words: List[str], language: str) -> List[str]:
        print("clean_stopword - started")

        list_of_words = clean(list_of_words, language)

        print(f"number of words after stopword clean up: {len(list_of_words)}")

        return list_of_words

    def _get_count_of_words(self, text: List[str]) -> Dict[str, int]:
        print("get_count_of_words - started")

        words_by_count = Counter(text)
        words_by_count = dict(sorted(words_by_count.items(), key=operator.itemgetter(1), reverse=True))

        return words_by_count

    def _clean_custom_word(self,
                           words_by_count: Dict[str, int],
                           words_to_remove_file_path: str = None) -> Dict[str, int]:
        print("clean_custom_word - started")

        if words_to_remove_file_path is None or not path.isfile(words_to_remove_file_path):
            return words_by_count

        with open(words_to_remove_file_path) as f:
            words_to_remove = f.readlines()

        for word in words_to_remove:
            words_by_count.pop(word.strip(), None)

        print(f"number of words unique words after all clean ups: {len(words_by_count)}")

        return words_by_count

    def save_results_to_excel(self, words_by_count: Dict[str, int], excel_file_path: str, sheet_name: str) -> None:
        print("save_results_to_excel - started")

        df_dict = {"words": words_by_count.keys(), "count": words_by_count.values()}
        df = pd.DataFrame.from_dict(df_dict)

        df.to_excel(excel_file_path, sheet_name=sheet_name, index=False, header=False)
