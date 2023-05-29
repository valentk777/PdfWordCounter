from source.services.excel_service import ExcelService
from source.services.text_cleaning_service import TextCleaningService
from source.text_word_counter.text_word_counter import TextWordCounter

LANGUAGE = "en"
WORDS_TO_REMOVE = "words_to_remove.txt"
SELECTED_WORDS = "selected_words.txt"

counter = TextWordCounter()

for _from, _to in [
    # ("data/conferences.txt", "result/result-conferences.xlsx"),
    # ("data/data_intensive_applications.txt", "result/result-data_intensive_applications.xlsx"),
    # ("data/ddd.txt", "result/result-DDD.xlsx"),
    # ("data/frankenstein.txt", "result/result-frankenstein.xlsx"),
    # ("data/how_to_decide.txt", "result/result-how_to_decide.xlsx"),
    # ("data/pragmatic_programmer.txt", "result/result-pragmatic_programmer.xlsx"),
    # ("data/rust.txt", "result/result-rust.xlsx"),
    # ("data/sapiens.txt", "result/result-sapiens.xlsx"),
    # ("data/second_brain.txt", "result/result-second_brain.xlsx"),
    # ("data/witcher.txt", "result/result-witcher.xlsx"),

    ("data/all_joined.txt", "result/result-all_joined.xlsx"),
]:
    data = counter.get_words_count(_from)

    data = TextCleaningService.clean_custom_word(data, WORDS_TO_REMOVE)
    data = TextCleaningService.clean_custom_word(data, SELECTED_WORDS)

    sheet_name = _from.split("/")[-1]

    ExcelService.write(data, _to, sheet_name)
