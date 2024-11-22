import json

from Src.Utility.path_manager import users_file, employee_file


def load_data(file_path):
    try:
        with open(file_path, 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return []

def save_data(file_path, data):
    with open(file_path, 'w') as f:
        json.dump(data, f, indent=4)
