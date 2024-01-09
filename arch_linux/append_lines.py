import os

def add_extra_lines_to_files(folder_path, lines_to_add):
    for filename in os.listdir(folder_path):
        if filename.endswith(".md"):
            file_path = os.path.join(folder_path, filename)
            with open(file_path, 'a') as file:
                file.write('\n'.join(lines_to_add) + '\n')

# Example usage:
folder_path = './arch_linux'
extra_lines = ['[up](README.md)', '[top](../README.md)']

add_extra_lines_to_files(folder_path, extra_lines)
