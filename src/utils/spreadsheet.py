from pathlib import Path
from .. import log
from typing import Union
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import tomli, msgpack

MOD_LIST_ID = '1lgQD8o7qhdWmrwdJjbRv3u_bwdrXmpOzaixWFzLR8r4'
MOD_LIST_RANGE = 'Mod List'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly', 'https://www.googleapis.com/auth/drive.readonly']
with open(Path.cwd() / 'config.toml', 'rb') as f:
	config = tomli.load(f) 
	CREDENTIALS = config['settings']['google_oauth_credentials'] 

def fetch_mod_list() -> None:
	
	token_path = Path.cwd() / 'cache' / 'auth_user.msgpack'
	if token_path.exists():
		with open(token_path, 'rb') as f:
			msgpack_data = f.read()
			json_data = msgpack.unpackb(msgpack_data)
			token_data = json.loads(json_data)
		
		creds = Credentials.from_authorized_user_info(token_data, SCOPES)
	else:
		flow = InstalledAppFlow.from_client_config(CREDENTIALS, SCOPES)
		creds = flow.run_local_server(port=0)

		with open(token_path, 'wb') as f:
			token_data = creds.to_json()
			msgpack_data = msgpack.packb(token_data)
			f.write(msgpack_data)

	service_sheets = build('sheets', 'v4', credentials=creds)
	service_drive = build('drive', 'v3', credentials=creds)

	sheet = service_sheets.spreadsheets()
	result = sheet.get(spreadsheetId=MOD_LIST_ID, ranges=MOD_LIST_RANGE, includeGridData=True).execute()
		
	mod_list_path = Path.cwd() / 'cache' / 'mod_list.msgpack'
	
	with open(mod_list_path, 'wb') as f:
		msgpack_data = msgpack.packb(result)
		f.write(msgpack_data)

def parse_mod_list() -> dict:
	'''
	Loads the Mod List and returns an ordered dictionary of every single mod there
	'''
	mod_list_path = Path.cwd() / 'cache' / 'mod_list.msgpack'
	with open(mod_list_path, 'rb') as f:
		msgpack_data = f.read()
		mod_list = msgpack.unpackb(msgpack_data)

	mod_range = len(mod_list['sheets'][0]['data'][0]['rowData']) - 1
	mod_dict = {}
	for i in range(mod_range):
		mod_dict[i+2] = get_mod_info(mod_list, i+2)
	
	return mod_dict

def get_mod_info(mod_list: dict, mod_index: int) -> dict:
	'''
	Returns a dictionary about a specific mod
	'''

	# lord forgive me
	mod_info = mod_list['sheets'][0]['data'][0]['rowData'][mod_index-1]['values']
	try: mod_name = mod_info[0]['userEnteredValue']['stringValue']
	except KeyError: mod_name = ''
	try: logo = mod_info[1]['userEnteredValue']['formulaValue'][8:-2]
	except KeyError: logo = ''
	try: pc_download = mod_info[2]['hyperlink']
	except KeyError: pc_download = '' 
	try: android_download = mod_info[3]['hyperlink']
	except KeyError: android_download = ''
	try: author = mod_info[4]['userEnteredValue']['stringValue']
	except KeyError: author = ''
	try: genre = mod_info[5]['userEnteredValue']['stringValue']
	except KeyError: genre = ''
	try: focus = mod_info[6]['userEnteredValue']['stringValue']
	except KeyError: focus = ''
	try: description = mod_info[7]['userEnteredValue']['stringValue']
	except KeyError: description = ''
	try: length = mod_info[8]['userEnteredValue']['stringValue']
	except KeyError: length = ''
	try: status = mod_info[9]['userEnteredValue']['stringValue']
	except KeyError: status = ''
	try: notes = mod_info[10]['userEnteredValue']['stringValue']
	except KeyError: notes = ''
	try: release_date = mod_info[11]['userEnteredValue']['formulaValue'][6:-1]
	except KeyError: release_date = ''

	return {
		'mod_name': mod_name,
		'logo': logo,
		'pc_download': pc_download,
		'android_download': android_download,
		'author': author,
		'genre': genre,
		'focus': focus,
		'description': description,
		'length': length,
		'status': status,
		'notes': notes,
		'release_date': release_date
	}