# Dossier
Dossier will be a mod manager for the game Doki Doki Literature Club, made in Qt6. I currently have 0 motivation for this, so here is the unfinished source code.

I will continue working on this, but for now I really don't want to

## Making it do stuff

The only way you can actually run and install nods is by editing the linked main.py file. I don't even know if this works on Windows like this.

1. Install the necessary packages via pip from src/requirements.txt
2. Uncomment the Qt code
3. Import the necessary functions
4. Run the Python script

It should look something like this:
```python
from utils.mod_utils import install_mod, setup_mod, launch_mod
from utils.directories import symlink_mod 

install_mod('/home/bulb/Downloads/Exit Music Redux 1.1.zip', 'Exit Music Redux')
symlink_mod('Exit Music Redux')
setup_mod('Exit Music Redux')
launch_mod('Exit Music Redux')
```
I removed the Qt code for simplicity.
* install_mod() extracts a mod archive and places it in the mod/ directory;
* symlink_mod() symlinks the nonexistant DDLC files to the mod;
* setup_mod() creates a config file and deletes the lib/ folder within lib/linux-x64_86/ so it doesn't error out
* launch_mod() runs the mod with parameters provided from the config file.

## Future plans for Dossier
* For it to work 🙏🙏
* Asset Viever - With the help of rpatool and unrpyc, we can look inside the guts of any Ren'py game. I plan to extract a whole mod to a different directory and let you look inside the nod. Maybe even make it so you can directly edit the mod itself
* A Store - With the help of gspread, I can just download the Mod List Spreadsheet and get the images, links, names, whatever from there and display them. However merged cells act REALLY weird with gspread so unless I can make it work correctly I can't do much
