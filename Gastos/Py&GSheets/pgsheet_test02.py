from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google.oauth2 import service_account

SCOPES = ['https://www.googleapis.com/auth/spreadsheets']
KEY = '/data/Shared/00.Aprendiendo/Py_Gsheets/pygsheet-400010-80dfa986bb46.json'
# Escribe aquí el ID de tu documento:
SPREADSHEET_ID = '16U-0YBEO7iyUW86Lj6U2ANMIPiItxYMlrE68FafnSdI'

creds = None
creds = service_account.Credentials.from_service_account_file(KEY, scopes=SCOPES)

service = build('sheets', 'v4', credentials=creds)
sheet = service.spreadsheets()

# Llamada a la api
result = sheet.values().get(spreadsheetId=SPREADSHEET_ID, range='Hoja 1!A1:A8').execute()
# Extraemos values del resultado
values = result.get('values',[])
print(values)