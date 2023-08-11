import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import datetime
import zipfile
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')


def SMA(S, L):
    n = np.size(S)
    M = np.zeros(n)
    for i in range(0, n):
        if i < L-1:
            M[i] = np.NaN
        else:
            M[i] = np.mean(S[i-L+1:i+1])
    return M


z = zipfile.ZipFile('HISTDATA_COM_XLSX_EURUSD_M12018.zip')
z.extractall()

df = pd.read_excel('DAT_XLSX_EURUSD_M1_2018.xlsx', sheet_name='2018', header=None, names=[
    'DateTime Stamp', 'Bar OPEN Bid Quote', 'Bar HIGH Bid Quote', 'Bar LOW Bid Quote', 'Bar CLOSE Bid Quote', 'Volume'])
# print(df.head(5))

df['MA1'] = SMA(df['Bar CLOSE Bid Quote'], 5)

df['MA2'] = df.rolling(window=10)['Bar CLOSE Bid Quote'].mean()
df['MA3'] = df.rolling(window=15)['Bar CLOSE Bid Quote'].mean()
df['MA4'] = df.rolling(window=30)['Bar CLOSE Bid Quote'].mean()

print(df.head(40))



