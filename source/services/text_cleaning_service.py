import re
import string
from os import path
from typing import List, Dict

from stopwords import clean


class TextCleaningService:
    @staticmethod
    def remove_punctuations(text: str) -> str:
        print("remove_punctuations - started")

        custom_punctuations = "‘©–—â€¦"
        translating = str.maketrans('', '', string.punctuation + custom_punctuations)

        return text.translate(translating)

    @staticmethod
    def remove_digits(text: str) -> str:
        print("remove_digits - started")

        translating = str.maketrans('', '', string.digits)

        return text.translate(translating)

    @staticmethod
    def remove_single_letters(text: str) -> str:
        print("remove_single_letters - started")

        return re.sub('(\\b[A-Za-z] \\b|\\b [A-Za-z]\\b)', '', text)

    @staticmethod
    def clean_stopword(list_of_words: List[str], language: str) -> List[str]:
        print("clean_stopword - started")

        list_of_words = clean(list_of_words, language)

        print(f"number of words after stopword clean up: {len(list_of_words)}")

        return list_of_words

    @staticmethod
    def clean_custom_word(words_by_count: Dict[str, int], words_to_remove_file_path: str = None) -> Dict[str, int]:
        print("clean_custom_word - started")

        if words_to_remove_file_path is None or not path.isfile(words_to_remove_file_path):
            return words_by_count

        with open(words_to_remove_file_path) as f:
            words_to_remove = f.readlines()

        for word in words_to_remove:
            words_by_count.pop(word.strip(), None)

        print(f"number of words unique words after all clean ups: {len(words_by_count)}")

        return words_by_count
