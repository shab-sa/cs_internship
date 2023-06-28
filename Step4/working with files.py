import requests, zipfile, io, pathlib
import pandas as pd
import warnings

warnings.filterwarnings('ignore', category=UserWarning, module='openpyxl')

# url='https://s17.picofile.com/d/8428234626/92fce4fb-232e-4624-87cf-338e4c444148/BarsaServiceClient.zip'
# r = requests.get(url, stream=True)
# io.BytesIO(r.content)

z = zipfile.ZipFile('HISTDATA_COM_XLSX_EURUSD_M12018.zip')
z.extractall()

for cur_path in pathlib.Path('.').glob('*.xlsx'):
    print(cur_path)
    df = pd.read_excel(io=cur_path.name,sheet_name='2018',names=['DateTime Stamp','Bar OPEN Bid Quote','Bar HIGH Bid Quote','Bar LOW Bid Quote','Bar CLOSE Bid Quote','Volume'])
    print(df.head(5))