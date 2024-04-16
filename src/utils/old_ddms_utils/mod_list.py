'''
	Contains anything related to the DDLC Mod List Spreadsheet
	https://docs.google.com/spreadsheets/d/1lgQD8o7qhdWmrwdJjbRv3u_bwdrXmpOzaixWFzLR8r4/edit?usp=sharing
'''
from pathlib import Path
import logging as log
log.basicConfig(level=log.NOTSET)

def get_spreadsheet() -> None:
	# Does not work with merged cells so this is useless right now
	gc = gspread.service_account()
	spreadsheet = gc.open_by_key("1lgQD8o7qhdWmrwdJjbRv3u_bwdrXmpOzaixWFzLR8r4")
	worksheet = spreadsheet.get_worksheet(1)
	modlist = worksheet.get_all_values(value_render_option=ValueRenderOption.formula)
	with open(get_work_dir("downloads") / "modlist.json", "w") as json_file:
		json.dump(modlist, json_file)

def get_from_spreadsheet(mod_name: str, collumn: str) -> str:
	# This too
	collumn_offset = {
		"mod_name": 0,
		"logo": 1,
		"downloadLink": 2,
		"downloadLinkAndroid": 3,
		"author": 4,
		"genre": 5,
		"focus": 6,
		"description": 7,
		"length": 8,
		"status": 9,
		"additionalNotes": 10,
		"releaseDate": 11
	}
	hyperlink_regex = r'=HYPERLINK\("(.*?)", ?"(.*?)"\)' # thanks github issues
	image_regex = r'=IMAGE\("(.*?)", ?"(.*?)"\)'

	modlist_file = get_work_dir("downloads") / "modlist.json"
	if not modlist_file.exists():
		log.error(f" The DDLC Mod List Spreadsheet has not been found. Please download it again")
	modlist = pd.read_json(str(modlist_file))
	
	# searchResults = modlist[modlist.astype(str).apply(lambda row: mod_name in row, axis=1)]
	# print(searchResults)
	# print( modlist.loc[mod_name] )