# Fancy Directory Sort
<img src="./static/fancy_logo.png">


✨ Features ✨

- Basic sorting into main categories (archive, audio, document, image, language, video)
- Extreme sorting into subcategories based on specific file extensions
- Configurable categorization through JSON files
- Test file generation for easy testing and demonstration
- Ability to add new file extensions to existing or new categories via command-line
- Sort files in a specific directory
- Executable command for quick sorting of the current directory
- Uninstall with command


### Installation
### Debian/Ubuntu
```bash
git clone https://github.com/BelaBartok39/Fancy_Dir.git
cd Fancy_Dir
pip install -r requirements.txt
chmod +x fancy
echo 'export PATH="$PATH:$PWD"' >> ~/.bashrc
source ~/.bashrc
```

### Usage

Quick sort (current directory):
```bash
fancy
```
Basic Sort(Specific Directory):
```bash
fancy /path/to/directory
```
Extreme Sort:
```bash
fancy /path/to/directory --extreme
```
Add a new file extension to a category:
```bash
fancy --add [file_extension] [category]
```
Uninstall all traces of Fancy:
```bash
fancy --uninstall
```

### Configuration
File Organizer uses JSON configuration files to determine how to categorize files. These are located in the config directory:

- archive_config.json
- audio_config.json
- document_config.json
- image_config.json
- language_config.json
- video_config.json

You can modify these files to customize the categorization of your files.

### Troubleshooting

- 'FileNotFoundError': Make sure the directory you're trying to organize exists.
- 'PermissionError': Ensure you have the necessary permissions to read from and write to the directory.
- NOTE: The config directory must be in the same directory as the fancy.py script.
- If the 'fancy' command is not found, make sure you've added the project directory to your PATH and sourced your .bashrc or .zshrc file.
- If you encounter a "No such file or directory: './config'" error, ensure that the config directory is present in the same directory as the fancy.py script.
- NOTE: The uninstall function assumes a certain installation structure. You may need to adjust it based on how your script is actually installed and where configuration files are stored.

