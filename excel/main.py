# -*- coding: utf-8 -*-
# pip install openpyxl pandas

# IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
# result_rows = result_df.index[result_df_name].rank(axis=0

# ValueError: Cannot index with multidimensional key
# result_rows = result_df.loc[result_df_name].index.rank(axis=0)
                  ~~~~~~~~~~~~~^^^^^^^^^^^^^^^^

# module
import time
import os,re
import json
import pandas as pd

run_file_name = os.path.basename(__file__)
current_case = int(re.findall(r'\d+', run_file_name)[0])
print(current_case)

excel_url = 'https://docs.google.com/spreadsheets/d/182g6QXuxEi7ATfrFf4vj9MqPQbtW5saoZYrDyo1cjHs/export?format=xlsx'
excel_df = pd.read_excel(excel_url, sheet_name='Sheet 1')
# print("excel_df", excel_df) # All rows

rows_name = "함수번호"

result_df = excel_df.loc[excel_df[rows_name].notnull(), [rows_name]]
# print("result_df", result_df) # A열 horizontal

result_df_name = result_df == current_case
# print("result_df_name", result_df_name) # 해당 번호들이 True인지 체크

result_rows = result_df.loc[result_df_name].index.rank(axis=0)
print("result_rows", result_rows)
items = {}

def test_c151067():
    print("tjqif")
    