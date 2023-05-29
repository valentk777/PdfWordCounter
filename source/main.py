from source.textWordCounter.text_word_counter import TextWordCounter

LANGUAGE = "en"
TEXT_WORD_COUNTER = "words_to_remove.txt"
FILE_PATH = "data/conferences.txt"
EXCEL_FILE_PATH = "result/result-conferences.xlsx"

counter = TextWordCounter()

for _from, _to in [
    ("data/conferences.txt", "result/result-conferences.xlsx"),
    ("data/frankenstein.txt", "result/result-frankenstein.xlsx"),
    ("data/rust.txt", "result/result-rust.xlsx"),
    ("data/witcher.txt", "result/result-witcher.xlsx"),
]:
    counter.get_words_count_and_save_to_excel(_from, _to, LANGUAGE, TEXT_WORD_COUNTER)
