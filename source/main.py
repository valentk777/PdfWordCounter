from source.textWordCounter.text_word_counter import TextWordCounter

LANGUAGE = "en"
FILE_PATH = "data/rust.txt"
EXCEL_FILE_PATH = "result/result.xlsx"

counter = TextWordCounter()
counter.get_words_count_and_save_to_excel(FILE_PATH, EXCEL_FILE_PATH, LANGUAGE)
