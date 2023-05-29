from source.textWordCounter.text_word_counter import TextWordCounter

LANGUAGE = "en"
TEXT_WORD_COUNTER = "words_to_remove.txt"
FILE_PATH = "data/conferences.txt"
EXCEL_FILE_PATH = "result/result-conferences.xlsx"

counter = TextWordCounter()
counter.get_words_count_and_save_to_excel(FILE_PATH, EXCEL_FILE_PATH, LANGUAGE, TEXT_WORD_COUNTER)
