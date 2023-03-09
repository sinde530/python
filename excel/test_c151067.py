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
# print(result_df_filter)

# 0  151067.0  패션잡화, 가방, 여성가방, 백팩  가방/잡화, 백팩/캐쥬얼가방, 백팩  상품_2.0   2.0  10000.0  ...           2.0    557349.0  176511.0        True      664345.0  true, S, 2023-03-08, 2023-05-18, 500, PR, 10, RT

result_column = ["카테고리1","카테고리2","카테고리3"]
result_data = result_df_filter[result_column]
print(result_data)

'''
result_df_name은 True값을 반환함. / cle
index중 True된 row 위치 찾기. / cle
array형식 columns 객체 뽑기 / cle
Columns Data Parameterized
'''

mock_data = "패션잡화, 가방, 여성가방, 백팩"

fd = result_data == mock_data
print("1111111111111111", fd)

#https://bigdaheta.tistory.com/41 여기 보니까 뭐 조건 설정해서 할수있던데 불러오는거
def test_c151067():
    print("tqtqtqtq")


#이거 집에서도 할수 있어여? 그대???????????????????????????????