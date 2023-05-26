from source.pdfWordCounter.pdf_word_counter import PdfWordCounter

LANGUAGE = "en"
PDF_FILE_PATH = "data/frankenstein-1818-text.pdf"
EXCEL_FILE_PATH = "result/result.xlsx"

counter = PdfWordCounter()
counter.get_words_count_from_pdf_and_save_to_excel(PDF_FILE_PATH, EXCEL_FILE_PATH, LANGUAGE)
