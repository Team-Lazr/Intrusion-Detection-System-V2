from Google import Create_Service
from datetime import datetime
import os
import sys

API_NAME = 'sheets'
API_VERSION = 'v4'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets']

dt_now = (datetime.now().strftime('%b %d %Y , %H:%M'))





def sheetsupdate(fname,lname,ID,Tag_ID,Remark):
	try:
		CLIENT_SECRET_FILE_data_log = (os.path.join(sys.path[0], "creds.json"))
		service_data_log = Create_Service(CLIENT_SECRET_FILE_data_log, API_NAME, API_VERSION, SCOPES)

		spreadsheet_id_data_log = '1yw0D4twDhJYP7iXHPpQ8MLLKlTUfaGIUsTUAhMMMVls'
		mySpreadsheets = service_data_log.spreadsheets().get(spreadsheetId=spreadsheet_id_data_log).execute()

		worksheet_name = 'Sheet1!'
		cell_range_insert = 'A1'
		values = ((dt_now,fname,lname,ID,Tag_ID,Remark),())

		value_range_body = {
		'majorDimension': 'ROWS',
		'values': values
		}
		service_data_log.spreadsheets().values().append(
		spreadsheetId=spreadsheet_id_data_log,
		valueInputOption='USER_ENTERED',
		range=worksheet_name + cell_range_insert,
		body=value_range_body
		).execute()

		print("End of Updating Sheets")

	except Exception as e:
		print("[INFO] caught a RuntimeError : ")
		print(e)



# sheetsupdate("ABC","def","GhI")