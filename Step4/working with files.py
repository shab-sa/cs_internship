import requests
# import io
# import pathlib
# import pandas as pd
# import warnings
import xlrd
import datetime
import zipfile
import urllib.request


# url='https://www.histdata.com/download-free-forex-historical-data/?/excel/1-minute-bar-quotes/eurusd/2018'
# urllib.request.urlretrieve(url,'TEST.txt')


# warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

# url='https://s17.picofile.com/d/8428234626/92fce4fb-232e-4624-87cf-338e4c444148/BarsaServiceClient.zip'
# r = requests.get(url, stream=True)
# io.BytesIO(r.content)

z = zipfile.ZipFile('HISTDATA_COM_XLSX_EURUSD_M12018.zip')
z.extractall()

xlrd.xlsx.ensure_elementtree_imported(False, None)
xlrd.xlsx.Element_has_iter = True

workbook = xlrd. open_workbook('DAT_XLSX_EURUSD_M1_2018.xlsx')
worksheet = workbook. sheet_by_index(0)
row_count = worksheet.nrows
col_count = worksheet.ncols
for cur_row in range(0, 10):  # row_count):
    row = worksheet.row_values(cur_row, start_colx=0, end_colx=None)
    row[0] = datetime.datetime(
        *xlrd.xldate_as_tuple(row[0], workbook.datemode)).strftime('%Y-%m-%d %H:%M:%S')
    print(row)


# for cur_path in pathlib.Path('.').glob('*.xlsx'):
#     print(cur_path)
#     df = pd.read_excel(io=cur_path.name, sheet_name='2018', names=[
#                        'DateTime Stamp', 'Bar OPEN Bid Quote', 'Bar HIGH Bid Quote', 'Bar LOW Bid Quote', 'Bar CLOSE Bid Quote', 'Volume'])
#     print(df.head(5))
