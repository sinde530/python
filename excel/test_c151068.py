# -*- coding: utf-8 -*-
# pip install openpyxl pandas numpy

# IndexError: too many indices for array: array is 1-dimensional, but 2 were indexed
# result_rows = result_df.index[result_df_name].rank(axis=0

# ValueError: Cannot index with multidimensional key
# result_rows = result_df.loc[result_df_name].index.rank(axis=0)

# result_rows = result_df[result_df_name].index.rank(axis=0)
# AttributeError: 'Int64Index' object has no attribute 'rank'

# result_rows = result_df[result_df_name].index.rank(axis=0)
# ValueError: Index data must be 1-dimensional

# result_rows = result_df[result_df_name].index.rank(axis=0)
# AttributeError: 'Int64Index' object has no attribute 'rank'

# result_rows = result_df[result_df_name].reset_index(drop=True).index.rank(method='min')
# AttributeError: 'RangeIndex' object has no attribute 'rank'

# module
import time
import os,re
import json
import pandas as pd
import numpy as np

run_file_name = os.path.basename(__file__)
current_case = int(re.findall(r'\d+', run_file_name)[0])
print(current_case)

excel_url = 'https://docs.google.com/spreadsheets/d/182g6QXuxEi7ATfrFf4vj9MqPQbtW5saoZYrDyo1cjHs/export?format=xlsx'
excel_df = pd.read_excel(excel_url, sheet_name='Sheet 1')
# print("excel_df", excel_df) # All rows

rows_name = "함수번호"

result_df = excel_df.loc[excel_df[rows_name].notnull(), :]
# print("result_df", result_df) # A열 horizontal

result_df_name = result_df[rows_name] == current_case
# print(result_df_name)

result_df_filter = result_df[result_df_name]
print(result_df_filter)

result_column = ["카테고리1","카테고리2","판매기간"]
result_data = result_df_filter[result_column]
print(result_data)

#https://bigdaheta.tistory.com/41 여기 보니까 뭐 조건 설정해서 할수있던데 불러오는거
def test_c151068():
    print("tqtqtqtq")
