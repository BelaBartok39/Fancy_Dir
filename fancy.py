"""
Fancy File Organizer

Copyright (c) 2024 bAbYnIcKy

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""

import os
import shutil
import sys
import argparse
import json
import logging
from logging.handlers import RotatingFileHandler

def load_configs(config_folder):
    configs = {}
    for filename in os.listdir(config_folder):
        if filename.endswith('_config.json'):
            category = filename.split('.')[0] 
            with open(os.path.join(config_folder, filename), 'r') as f:
                configs[category] = json.load(f)
    return configs

def organize_files(directory, configs, extreme_sort=False):
    extension_to_category = {}
    for category, extensions in configs.items():
        base_category = category.split('_')[0]
        for ext in extensions:
            extension_to_category[ext] = base_category

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
           
            category = extension_to_category.get(extension, 'misc')
            category_folder = os.path.join(directory, category)
            
            if not os.path.exists(category_folder):
                os.makedirs(category_folder, exist_ok=True)
                logging.debug(f"Created category folder: {category_folder}")
           
            if extreme_sort and category != 'misc':
                config_key = f"{category}_config"
                sub_category = configs[config_key].get(extension, 'other')
                sub_category_folder = os.path.join(category_folder, sub_category)
                os.makedirs(sub_category_folder, exist_ok=True)
                logging.debug(f"Created subcategory folder: {sub_category_folder}")
                dest_folder = sub_category_folder
            else:
                dest_folder = category_folder
           
            if os.path.dirname(file_path) != dest_folder:
                shutil.move(file_path, os.path.join(dest_folder, filename))
                logging.info(f"Moved {filename} to {dest_folder}")
            else:
                logging.debug(f"{filename} is already in the correct folder")

    logging.info("File organization complete!")

def add_extension(config_folder, extension, category):
    config_file = os.path.join(config_folder, f"{category}_config.json")
    
    if os.path.exists(config_file):
        with open(config_file, 'r+') as f:
            config = json.load(f)
            if extension not in config:
                config.append(extension)
                f.seek(0)
                json.dump(config, f, indent=4)
                f.truncate()
                logging.info(f"Added '{extension}' to '{category}' category.")
            else:
                logging.warning(f"'{extension}' already exists in '{category}' category.")
    else:
        with open(config_file, 'w') as f:
            json.dump([extension], f, indent=4)
        logging.info(f"Created new category '{category}' and added '{extension}' to it.")

def setup_logging(verbose):
    log_level = logging.DEBUG if verbose else logging.INFO
    
    # Get the user's home directory
    home_dir = os.path.expanduser("~")
    log_dir = os.path.join(home_dir, ".fancy_sort")
    
    # Create the log directory if it doesn't exist
    os.makedirs(log_dir, exist_ok=True)
    
    log_file = os.path.join(log_dir, "fancy_sort.log")

    # Set up file handler with rotation
    file_handler = RotatingFileHandler(log_file, maxBytes=1024*1024, backupCount=5)
    file_handler.setLevel(logging.DEBUG)  # Always log everything to file
    
    # Set up console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(log_level)

    # Create formatters and add them to the handlers
    file_formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s')
    console_formatter = logging.Formatter('%(levelname)s: %(message)s')
    file_handler.setFormatter(file_formatter)
    console_handler.setFormatter(console_formatter)

    # Get the root logger and add handlers
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # Capture all levels
    root_logger.addHandler(file_handler)
    root_logger.addHandler(console_handler)

def uninstall():
    # Remove the log directory
    home_dir = os.path.expanduser("~")
    log_dir = os.path.join(home_dir, ".fancy_sort")
    if os.path.exists(log_dir):
        shutil.rmtree(log_dir)
        print(f"Removed log directory: {log_dir}")

    # Remove the script directory
    script_dir = os.path.dirname(os.path.realpath(__file__))
    if os.path.exists(script_dir):
        shutil.rmtree(script_dir)
        print(f"Removed script directory: {script_dir}")

    # Remove the executable from PATH
    # This part is tricky and depends on how the script was installed
    # For this example, we'll assume it was installed in /usr/local/bin
    executable_path = "/usr/local/bin/fancy"
    if os.path.exists(executable_path):
        os.remove(executable_path)
        print(f"Removed executable: {executable_path}")

    print("Fancy Directory Sort has been uninstalled.")
    print("Note: You may need to manually remove the 'fancy' command from your PATH if it was added there.")

def main():
    parser = argparse.ArgumentParser(description='Fancy File Organizer')
    parser.add_argument('directory', nargs='?', default='.',
                        help='Directory to organize (default: current directory)')
    parser.add_argument('--extreme', action='store_true',
                        help='Enable extreme sorting by individual extensions')
    parser.add_argument('-add', nargs=2, metavar=('EXT', 'CATEGORY'),
                        help='Add a file extension to a category')
    parser.add_argument('-v', '--verbose', action='store_true',
                        help='Enable verbose logging')
    parser.add_argument('--uninstall', action='store_true',
                            help='Uninstall Fancy Directory Sort')
    args = parser.parse_args()
    
    setup_logging(args.verbose)

    script_dir = os.path.dirname(os.path.realpath(__file__))
    config_folder = os.path.join(script_dir, 'config')

    if args.add:
        extension, category = args.add
        add_extension(config_folder, extension, category)
    elif args.uninstall:
        uninstall()
        sys.exit(0)
    else:
        directory = os.path.abspath(args.directory)
        extreme_sort = args.extreme

        if not os.path.isdir(directory):
            logging.error(f"'{directory}' is not a valid directory.")
            sys.exit(1)
        
        logging.info(f"Organizing files in: {directory}")
        extension_map = load_configs(config_folder)
        organize_files(directory, extension_map, extreme_sort)
 
if __name__ == '__main__':
    main() 


