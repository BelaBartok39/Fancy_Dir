# Fancy Directory Sort ⛵

## ✨ Features ✨

- Basic sorting into main categories (archive, audio, document, image, language, video)
- Extreme sorting into subcategories based on specific file extensions
- Configurable categorization through JSON files
- Test file generation for easy testing and demonstration


### Installation
### Debian/Ubuntu
```python
git clone https://github.com/BelaBartok39/Fancy_Dir.git
cd Fancy_Dir
pip install -r requirements.txt
'text/plain'
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




