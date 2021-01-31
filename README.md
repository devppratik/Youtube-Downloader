## Youtube Video & Playlist Downloader

This is a command line python script to download youtube videos & playlist. Made using the pytube library.
Working on a GUI version

### Usage
- #### For Unix based systems
    1. Create a `.scripts` folder in your home directory 
    2. Add the script inside this folder & rename it to youtube.py
    3. Add an alias in your .bashrc/.zshrc file as<br>
      `  alias youtube="python ~/.scripts/youtube.py" `
    4. Source your .bashrc/.zshrc file
    5. Now you can run the script anywhere by just typing `youtube`

- #### For Windows based systems
	1. Make sure you have python installes
    2. Move the script to a folder of your desired location
	3. Open the folder in powershell or command prompt and run ` python .\script.py ` to launch the script
	

#### Note
The default download location is the user's download directory. <br> 
You can change it by altering the following code fragment in the script
```
def get_download_location():
    if os.name == 'nt':
        download_location = os.path.join(home, 'Downloads')  # For Windows
    else:
        download_location = os.path.join(
            os.path.expanduser('~'), 'Downloads') # For Unix Systems
    return download_location
```
