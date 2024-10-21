
import json

def load_users(users_file):
    try:
        with open(users_file, 'r') as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        print(f"Error: {users_file} not found or is corrupt. Creating a new file.")
        return []

def save_users(users_file, users):
    try:
        with open(users_file, 'w') as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving users: {e}")
