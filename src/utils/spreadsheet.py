from pathlib import Path
from src import log
from typing import Union
import json

from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
import tomli, msgpack

MOD_LIST_ID = '1lgQD8o7qhdWmrwdJjbRv3u_bwdrXmpOzaixWFzLR8r4'
MOD_LIST_RANGE = 'Mod List'
SCOPES = ['https://www.googleapis.com/auth/spreadsheets.readonly']
with open(Path.cwd() / 'config.toml', 'rb') as f:
	config = tomli.load(f) 
	CREDENTIALS = config['settings']['google_oauth_credentials'] 

def fetch_mod_list() -> None:
	creds = None
	token_path = Path.cwd() / 'cache' / 'auth_user.msgpack'
	
	if token_path.exists():
		with open(token_path, 'rb') as f:
			msgpack_data = f.read()
			json_data = msgpack.unpackb(msgpack_data)
			token_data = json.loads(json_data)
		
		creds = Credentials.from_authorized_user_info(token_data, SCOPES)
	
	if not creds or not creds.valid:
		if creds and creds.expired and creds.refresh_token:
			creds.refresh(Request())
		else:
			flow = InstalledAppFlow.from_client_config(CREDENTIALS, SCOPES)
			creds = flow.run_local_server(port=0)

		with open(token_path, 'wb') as f:
			token_data = creds.to_json()
			msgpack_data = msgpack.packb(token_data)
			f.write(msgpack_data)

	service_sheets = build('sheets', 'v4', credentials=creds)

	sheet = service_sheets.spreadsheets()
	result = sheet.get(spreadsheetId=MOD_LIST_ID, ranges=MOD_LIST_RANGE, includeGridData=True).execute()
		
	mod_list_path = Path.cwd() / 'cache' / 'mod_list.msgpack'
	
	with open(mod_list_path, 'wb') as f:
		msgpack_data = msgpack.packb(result['sheets'][0]['data'][0]['rowData'])
		f.write(msgpack_data)

def parse_mod_list() -> dict:
	'''
	Loads the Mod List and returns an ordered dictionary of every single mod there
	'''
	mod_list_path = Path.cwd() / 'cache' / 'mod_list.msgpack'
	
	if not mod_list_path.exists():
		raise FileNotFoundError('The Mod List has not been fetched before, and therefore does not exist.')
	with open(mod_list_path, 'rb') as f:
		msgpack_data = f.read()
		mod_list = msgpack.unpackb(msgpack_data)

	mod_range = len(mod_list) - 1
	mod_dict = {1: {
		'mod_name': 'Doki Doki Literature Club',
		'logo': '',
		'pc_download': 'https://teamsalvato.itch.io/ddlc',
		'android_download': '',
		'author': 'Team Salvato',
		'genre': 'Psychological Horror',
		'focus': 'All',
		'description':	'Hi, Monika here!'\
						'Welcome to the Literature Club! It\'s always been a dream of mine to make something special out of the things I love. Now that you\'re a club member, you can help me make that dream come true in this cute game!'\
						'Every day is full of chit-chat and fun activities with all of my adorable and unique club members:'\
						'Sayori, the youthful bundle of sunshine who values happiness the most;'\
						'Natsuki, the deceivingly cute girl who packs an assertive punch;'\
						'Yuri, the timid and mysterious one who finds comfort in the world of books;'\
						'...And, of course, Monika, the leader of the club! That\'s me!'\
						'I\'m super excited for you to make friends with everyone and help the Literature Club become a more intimate place for all my members. But I can tell already that you\'re a sweetheart—will you promise to spend the most time with me? ♥',
		'length': 'Long',
		'status': '',
		'notes': '',
		'release_date': 'sometime'
	}}
	for i in range(mod_range):
		mod_dict[i+2] = get_mod_info(mod_list, i+2)
	
	return mod_dict

def get_mod_info(mod_list: dict, mod_index: int) -> dict:
	'''
	Returns a dictionary about a specific mod
	'''

	# lord forgive me
	mod_info = mod_list[mod_index-1]['values']

	return {
		'mod_name': extract_mod_info_field(mod_info, 'mod_name'),
		'logo': extract_mod_info_field(mod_info, 'logo'),
		'pc_download': extract_mod_info_field(mod_info, 'pc_download'),
		'android_download': extract_mod_info_field(mod_info, 'android_download'),
		'author': extract_mod_info_field(mod_info, 'author'),
		'genre': extract_mod_info_field(mod_info, 'genre'),
		'focus': extract_mod_info_field(mod_info, 'focus'),
		'description': extract_mod_info_field(mod_info, 'description'),
		'length': extract_mod_info_field(mod_info, 'length'),
		'status': extract_mod_info_field(mod_info, 'status'),
		'notes': extract_mod_info_field(mod_info, 'notes'),
		'release_date': extract_mod_info_field(mod_info, 'release_date')
	}

def extract_mod_info_field(mod_info: dict, key: str) -> Union[str, int]:
	string_keys = ['mod_name', 'author', 'genre', 'focus', 'description', 'length', 'status', 'notes']
	formula_keys = ['logo', 'release_date']
	hyperlink_keys = ['pc_download', 'android_download']
	keys = ['mod_name', 'logo', 'pc_download', 'android_download', 'author', 'genre', 'focus', 'description', 'length', 'status', 'notes', 'release_date']
	
	column = keys.index(key)

	try:
		if key in string_keys:
			return mod_info[column]['userEnteredValue']['stringValue']
		if key in formula_keys:
			if key == 'logo':
				return mod_info[column]['userEnteredValue']['formulaValue'][8:-2]
			if key == 'release_date':
				return mod_info[column]['userEnteredValue']['formulaValue'][6:-1]
		if key in hyperlink_keys:
			return mod_info[column]['hyperlink']
	except KeyError:
		return ''
