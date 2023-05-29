from typing import Dict

import pandas as pd


class ExcelService:
    @staticmethod
    def write(words_by_count: Dict[str, int], excel_file_path: str, sheet_name: str) -> None:
        print("save_results_to_excel - started")

        df_dict = {"words": words_by_count.keys(), "count": words_by_count.values()}
        df = pd.DataFrame.from_dict(df_dict)

        df.to_excel(excel_file_path, sheet_name=sheet_name, index=False, header=False)
