import pygsheets
import pandas as pd
#authorization
#gc = pygsheets.authorize(service_file='/Users/erikrood/desktop/QS_Model/creds.json')
gc = pygsheets.authorize(service_file='/data/Shared/00.Aprendiendo/Py_Gsheets/pygsheet-400010-80dfa986bb46.json')

# Create empty dataframe
df = pd.DataFrame()

# Create a column
df['name'] = ['Martin', 'Mai', 'Nacho']

#open the google spreadsheet (where 'PY to Gsheet Test' is the name of my sheet)
#sh = gc.open('PY to Gsheet Test')
sh = gc.open('test_py')

#select the first sheet 
wks = sh[0]

#update the first sheet with df, starting at cell B2. 
wks.set_dataframe(df,(1,1))