import unittest
import uuid
from os import path

from source.text_word_counter.text_word_counter import TextWordCounter

PDF_FILE_PATH = "data/test_pdf.pdf"
TXT_FILE_PATH = "data/test_txt.txt"
WORDS_TO_REMOVE_FILE_PATH = "data/test_words_to_remove.txt"


class TestTextWordCounter(unittest.TestCase):

    def test_given_pdf_when_getting_counter_with_excel_save_then_excel_file_created(self):
        counter = TextWordCounter()
        excel_file_path = f"result/{str(uuid.uuid4())}result.xlsx"
        counter.get_words_count_and_save_to_excel(
            PDF_FILE_PATH, excel_file_path, WORDS_TO_REMOVE_FILE_PATH
        )

        self.assertTrue(path.isfile(excel_file_path))

    def test_given_pdf_when_getting_counter_with_cleanup_then_correct_number_of_unique_words_returned(self):
        counter = TextWordCounter()
        data = counter.get_words_count(PDF_FILE_PATH, WORDS_TO_REMOVE_FILE_PATH)

        self.assertEqual(561, len(data), "incorrect number of unique word")

    def test_given_txt_when_getting_counter_with_cleanup_then_correct_number_of_unique_words_returned(self):
        counter = TextWordCounter()
        data = counter.get_words_count(TXT_FILE_PATH, WORDS_TO_REMOVE_FILE_PATH)

        self.assertEqual(5, len(data), "incorrect number of unique word")


if __name__ == '__main__':
    unittest.main()
