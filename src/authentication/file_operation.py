import json
from Src.Messages.authentication import AuthHandler

message_handler = AuthHandler()

def load_users(users_file):
    try:
        with open(users_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        message_handler.user_data_file_not_found()
        return []
    except json.JSONDecodeError:
        message_handler.user_data_read_error()
        return []

def save_users(users_file, users):
    try:
        with open(users_file, 'w') as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        message_handler.user_save_error(e)
