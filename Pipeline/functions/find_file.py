import os


def find_file(file_name, search_path):
    for root, dirs, files in os.walk(search_path):
        if file_name in files:
            return os.path.join(root, file_name)
        else:
            return f'file not found in {search_path}'

