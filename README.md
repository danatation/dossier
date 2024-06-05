# Dossier
Dossier is a mod manager for the DDLC. Updating readme later

## Making it do stuff

The only way you can actually run and install mods is by editing the linked main.py file. I don't even know if this works on Windows like this.

1. Install the necessary packages via pip from src/requirements.txt
3. Modify the main.py file
4. Run the Python script

It should look something like this:
```python 
extract_game('/home/bulb/Downloads/Exit Music Redux 1.1.zip')
copy_game_files('/home/bulb/Downloads/Exit Music Redux 1.1.zip')
setup_game('/home/bulb/Downloads/Exit Music Redux 1.1.zip')
launch_mod('/home/bulb/Downloads/Exit Music Redux 1.1.zip')
```
* extract_mod() extracts a mod's archive and places it in the mod/ directory;
* copy_game_files() copies the nonexistant DDLC files to the mod;
* setup_game() creates a config file and deletes the lib/ folder within lib/linux-x64_86/ so it doesn't error out
* launch_game() runs the mod with parameters provided from the config file.

## Future plans for Dossier
* For ~~it~~ the GUI to work 🙏🙏
* Asset Viever - With the help of rpatool and unrpyc, we can look inside the guts of any Ren'Py game. I plan to extract a whole mod to a different directory and let you look inside the mod. Maybe even make it so you can directly edit the mod itself(partially working)
* A Store - With the help of ~~gspread~~the official Google API, I can just download the Mod List Spreadsheet and get the ~~images~~(some images fail to get fetched), links, names, whatever from there and display them. ~~However merged cells act REALLY weird with gspread so unless I can make it work correctly I can't do much~~(I made merged cells work by simply not using gspread)
