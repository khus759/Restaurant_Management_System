import json

def load_users(users_file):
    try:
        with open(users_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("User data file not found, creating a new one.")
        return []
    except json.JSONDecodeError:
        print("Error reading user data, resetting file.")
        return []

def save_users(users_file, users):
    try:
        with open(users_file, 'w') as file:
            json.dump(users, file, indent=4)
    except Exception as e:
        print(f"An error occurred while saving users: {e}")
