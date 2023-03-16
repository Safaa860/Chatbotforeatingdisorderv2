import pandas as pd

SHEET_ID = '1lEh1HoFPIRIDTJFgyDNJNGju7CPYf2DcFSKBflZU'
SHEET_NAME = 'Sheet1'
url = f'https://docs.google.com/spreadsheets/d/{SHEET_ID}/gviz/tq?tqx=out:csv&sheet={SHEET_NAME}'
df = pd.read_csv(url)
print(df.head())
