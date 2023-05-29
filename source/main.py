from source.textWordCounter.text_word_counter import TextWordCounter

LANGUAGE = "en"
PDF_FILE_PATH = "data/frankenstein-1818-text.pdf"
EXCEL_FILE_PATH = "result/result.xlsx"

counter = TextWordCounter()
counter.get_words_count_and_save_to_excel(PDF_FILE_PATH, EXCEL_FILE_PATH, LANGUAGE)
