# Fancy Directory Sort
<img src="https://external-content.duckduckgo.com/iu/?u=http%3A%2F%2Fchriscarey.com%2Fwordpress%2Fwp-content%2Fuploads%2F2008%2F02%2FScreen-Shot-2014-08-17-at-4.22.57-PM.png&f=1&nofb=1&ipt=e581bcd003d7dde39a2aad2f1ce50606e7f98e82e2d0c690c777beca21b067df&ipo=images">


✨ Features ✨

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




