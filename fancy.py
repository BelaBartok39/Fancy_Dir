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

def load_configs(config_folder):
    configs = {}
    for filename in os.listdir(config_folder):
        if filename.endswith('_config.json'):
            category = filename.split('.')[0]  # This keeps the '_config' part
            with open(os.path.join(config_folder, filename), 'r') as f:
                configs[category] = json.load(f)
    return configs

def organize_files(directory, configs, extreme_sort=False):
    # Create a mapping from file extensions to their base categories
    extension_to_category = {}
    for category, extensions in configs.items():
        base_category = category.split('_')[0]  # Remove '_config' from the category name
        for ext in extensions:
            extension_to_category[ext] = base_category

    for filename in os.listdir(directory):
        file_path = os.path.join(directory, filename)
        if os.path.isfile(file_path):
            extension = os.path.splitext(filename)[1].lower()
            
            # First-tier sorting
            category = extension_to_category.get(extension, 'misc')
            category_folder = os.path.join(directory, category)
            os.makedirs(category_folder, exist_ok=True)
            
            if extreme_sort and category != 'misc':
                # Second-tier sorting (only for non-misc categories)
                config_key = f"{category}_config"
                sub_category = configs[config_key].get(extension, 'other')
                sub_category_folder = os.path.join(category_folder, sub_category)
                os.makedirs(sub_category_folder, exist_ok=True)
                dest_folder = sub_category_folder
            else:
                dest_folder = category_folder
            
            shutil.move(file_path, os.path.join(dest_folder, filename))
            print(f"Moved {filename} to {dest_folder}")

    print("File organization complete!")

def main():
    parser = argparse.ArgumentParser(description='Fancy File Organizer')
    parser.add_argument('directory', nargs='?', default='.',
                        help='Directory to organize')
    parser.add_argument('--extreme', action='store_true',
                        help='Enable extreme sorting by individual extensions')
    parser.add_argument('--config', default='./config',
                        help='Path to the config folder')
    
    args = parser.parse_args()

    directory = args.directory
    extreme_sort = args.extreme
    config_folder = args.config

    config_folder = 'config'
    extension_map = load_configs(config_folder)

    organize_files(directory, extension_map, extreme_sort)

if __name__ == '__main__':
    main() 


