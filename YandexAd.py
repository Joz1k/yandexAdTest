import pandas as pd
import numpy as np

df = pd.read_excel('C:/Users/evgen/PycharmProjects/AI/data/yandex.xlsx', sheet_name='data')
df['CTR'] = round(df['Clicks'] / df['Shows'] * 100, 1).fillna(0)
df['CPC'] = round(df['Cost']/df['Clicks'], 2).fillna(0)
df['CR'] = round(df['Conversions']/df['Clicks'] * 100, 2).fillna(0)
df['CPA'] = round(df['Cost']/df['Conversions']).fillna(np.inf)
df.replace([np.inf, -np.inf], 0, inplace=True)
data = pd.DataFrame(df[(df['Client'] == 'Сигма') & (df['Month'] >= "2022-06-01") & (df["Month"] <= "2022-09-01")])
data.sort_values(by='Month', ascending=True, inplace=True)
data.to_csv('C:/Users/evgen/PycharmProjects/AI/data/yandex.csv', encoding="utf-8-sig", index=False)

