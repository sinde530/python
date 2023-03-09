# -*- coding: utf-8 -*-

# pip install openpyxl pandas numpy
# module
import time
import os,re
import json
import pandas as pd
import numpy as np

# 아맞다 이거 파일 돌려서 해당 파일 True나는지 봐보실랴여
run_file_name = os.path.basename(__file__)
current_case = int(re.findall(r'\d+', run_file_name)[0])
print(current_case)

#잠시만요???
excel_url = 'https://docs.google.com/spreadsheets/d/182g6QXuxEi7ATfrFf4vj9MqPQbtW5saoZYrDyo1cjHs/export?format=xlsx'
excel_df = pd.read_excel(excel_url, sheet_name='Sheet 1')
# print("excel_df", excel_df) # All rows
rows_name = "함수번호"

result_df = excel_df.loc[excel_df[rows_name].notnull(), [rows_name]]
# print("result_df", result_df) # A열 horizontal

result_df_name = [result_df == current_case]
print("해당값 True", result_df_name)

#result_rows = result_df[result_df_name].index.rank(axis=0) #이쪽에러
#print("result_rows", result_rows)

# print(result_df_name)
# print("result_df_name", result_df_name)

# result_rows = result_df[result_df_name].index.rank(axis=0)
# print("result_rows", result_rows)

# x = np.array([result_df_name]) 
# print("x", x)

def test_c151068():
    print("tjqif")
