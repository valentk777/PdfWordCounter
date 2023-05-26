import unittest
import uuid
from os import path

from source.pdfWordCounter.pdf_word_counter import PdfWordCounter

LANGUAGE = "en"
PDF_FILE_PATH = "data/test_pdf.pdf"
WORDS_TO_REMOVE_FILE_PATH = "data/test_words_to_remove.txt"


class TestPdfWordCounter(unittest.TestCase):

    def test_given_pdf_when_getting_counter_with_excel_save_then_excel_file_created(self):
        counter = PdfWordCounter()
        excel_file_path = f"result/{str(uuid.uuid4())}result.xlsx"
        counter.get_words_count_from_pdf_and_save_to_excel(
            PDF_FILE_PATH, excel_file_path, LANGUAGE, WORDS_TO_REMOVE_FILE_PATH
        )

        self.assertTrue(path.isfile(excel_file_path))

    def test_given_pdf_when_getting_counter_with_cleanup_then_correct_number_of_unique_words_returned(self):
        counter = PdfWordCounter()
        data = counter.get_words_count_from_pdf(PDF_FILE_PATH, LANGUAGE, WORDS_TO_REMOVE_FILE_PATH)

        self.assertEqual(487, len(data), "incorrect number of unique word")


if __name__ == '__main__':
    unittest.main()
