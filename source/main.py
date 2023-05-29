from source.services.excel_service import ExcelService
from source.services.text_cleaning_service import TextCleaningService
from source.services.txt_service import TxtService
from source.text_word_counter.text_word_counter import TextWordCounter

LANGUAGE = "en"
WORDS_TO_REMOVE = "words_to_remove.txt"
SELECTED_WORDS = "selected_words.txt"


def clean_all_joined():
    all_data = TxtService.read("data/all_joined.txt")

    with open(WORDS_TO_REMOVE, encoding="utf-8") as f:
        words_to_remove = f.readlines()

    for word in words_to_remove:
        if word == "\n":
            continue

        all_data = all_data.replace(word, "")

    with open(r"data\temp_result2.txt", "a", encoding="utf-8") as f:
        f.write(all_data)


def convert():
    counter = TextWordCounter()

    for _from, _to in [
        # ("data/conferences.txt", "result/result-conferences.xlsx"),
        # ("data/frankenstein.txt", "result/result-frankenstein.xlsx"),
        # ("data/sapiens.txt", "result/result-sapiens.xlsx"),
        # ("data/witcher.txt", "result/result-witcher.xlsx"),

        ("data/all_joined.txt", "result/result-all_joined.xlsx"),
    ]:
        data = counter.get_words_count(_from)

        data = TextCleaningService.clean_custom_word(data, WORDS_TO_REMOVE)
        data = TextCleaningService.clean_custom_word(data, SELECTED_WORDS)

        sheet_name = _from.split("/")[-1]

        ExcelService.write(data, _to, sheet_name)


if __name__ == "__main__":
    # clean_all_joined()
    convert()
