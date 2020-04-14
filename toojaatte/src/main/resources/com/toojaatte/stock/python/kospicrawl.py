#  자동 크롤링 스케줄러
# 금융 api 출처: https://github.com/FinanceData/FinanceDataReader/wiki/Users-Guide
# 스케줄러 : pyinstaller 설치, py를 exe파일로 저장, 스케줄러에서 exe파일을 돌린다. / 파일내 경로는 모두 절대경로로 변경

import matplotlib.pyplot as plt
import FinanceDataReader as fdr
import pandas as pd
from pandas import json_normalize

fdr.__version__

# # 주가지수, 2019년~현재
df_kospi = fdr.DataReader('KS11', '2019')
print(df_kospi)
df_kospi.to_json('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\kospi.json', orient='table')
# print(df_kospi.set_index(['Date', 'Close']))
# time_series_df_kospi = df_kospi[['Date','Close']]
# print(time_series_df_kospi)


df_kospi50 = fdr.DataReader('KS50', '2019')
df_kospi50.to_json('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\kospi50.json', orient='table')

df_kospi200 = fdr.DataReader('KS200', '2019')
df_kospi200.to_json('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\kospi200.json', orient='table')

df_kosdaq = fdr.DataReader('KQ11', '2019')
df_kosdaq.to_json('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\kosdaq.json', orient='table')

df_kosdaq150 = fdr.DataReader('KQ150', '2019')
df_kosdaq150.to_json('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\kosdaq150.json', orient='table')


# 미국지수, 2019년~현재
df_dowjones = fdr.DataReader('DJI', '2019')
df_dowjones.to_json('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\dowjones.json', orient='table')

df_nasdaq = fdr.DataReader('IXIC', '2019')
df_nasdaq.to_json('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\nasdaq.json', orient='table')


# 환율, 1995년~현재
df_usdkrw = fdr.DataReader('USD/KRW','2019')
df_usdkrw.to_json('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\usdkrw.json', orient='table')

df_cnykrw = fdr.DataReader('CNY/KRW','2019')
df_cnykrw.to_json('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\cnykrw.json', orient='table')

df_jpykrw = fdr.DataReader('JPY/KRW','2019')
df_jpykrw.to_json('C:\\Users\\hong\\Documents\\GitHub\\Java_Spring\\toojaatte\\toojaatte\\src\\main\\resources\\com\\toojaatte\\stock\\crawlingtest\\jpykrw.json', orient='table')

# print(df)


