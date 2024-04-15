# pip install openpyxl
# pip install pandas
import pandas as pd
import numpy as np

# df = pd.read_csv('converted.csv', header=None)
# df.to_csv('converted-copia.csv')
# df.to_excel('converted-copia-excel.xlsx', sheet_name='valuaciones',
#           engine='openpyxl')
# print(df.head())
df = pd.read_csv('converted.csv')
# print(df.head)

# print(df.iloc[1:5, 0: 15])
# print(df['Modelo'])
# print(df[df['C.Marca'] > 0])
print(df[df['Marca'].isin(['TRACTOR DE CARRETERA'])])
