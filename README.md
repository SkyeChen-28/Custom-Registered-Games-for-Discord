# Custom Registered Games for Discord

Set a custom game name to display as the game you're currently playing on Discord

## Requirements

Python Version: 3.11.1

### Required packages

Enter the following command in a terminal to install all required packages:

```{bash}
pip install -Ur requirements.txt
```

## Usage

### Windows Executable

1. Download the `Custom.Registered.Games.for.Discord.exe` file from the [latest release page](https://github.com/SkyeChen-28/Custom-Registered-Games-for-Discord/releases)
2. (Optional) Verify that the SHA-512 hash matches using a program like [QuickHash](https://www.quickhash-gui.org/)
3. Run the program `Custom.Registered.Games.for.Discord.exe`. Let Windows Defender know that this program is safe.
4. Follow the instructions in the newly opened Window

### Command Line / Terminal

1. Download the file [`main.py`](https://github.com/SkyeChen-28/Custom-Registered-Games-for-Discord/blob/main/main.py)
2. To run this script from the command line, enter the following commands as specified in the next few steps
3. First, you must change the directory to be at the same folder where you downloaded `main.py`. If you're using Windows, open up Command Prompt (not PowerShell) and type in:

```{bash}
cd %USERPROFILE%\Downloads
```

4. Enter the following command

```{bash}
python main.py
```

5. Follow the instructions in the newly opened Window

### Build the executable from the source code

1. Download [`main.py`](https://github.com/SkyeChen-28/Custom-Registered-Games-for-Discord/blob/main/main.py)
2. Install all required packages:

```{bash}
pip install -Ur requirements.txt
```

3. Execute the following build command:
```{bash}
pyinstaller --noconfirm --onefile --windowed --name "Custom.Registered.Games.for.Discord" --paths <PATH-TO-PYTHON-PACKAGES> --collect-all "sv_ttk" <PATH-TO-MAIN.PY>
```

4. Run the program `Custom.Registered.Games.for.Discord.exe`
5. Follow the instructions in the newly opened Window

Enjoy!

I just discovered that you can just rename games on Discord. So this is now the most useless repo on my GitHub...
