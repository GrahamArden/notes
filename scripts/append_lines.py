### A short python script to add the 'up' and 'top' links to the end of each page


import os

def add_extra_lines_to_files(folder_path, lines_to_add):
    for root, dirs, files in os.walk(folder_path):
        for filename in files:
            if filename.endswith(".md"):
                file_path = os.path.join(root, filename)
                with open(file_path, 'r+') as file:
                    content = file.read()
                    if not all(line in content for line in lines_to_add):
                        file.write('\n'.join(lines_to_add) + '\n')

# Example usage:
folder_path = '.'
extra_lines = ['[up](README.md)', '[top](../README.md)']

add_extra_lines_to_files(folder_path, extra_lines)
