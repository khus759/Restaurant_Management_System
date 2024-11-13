
import json
from Src.Utility.path_manager import users_file

class Authentication:
    @staticmethod
    def load_data(file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []

    @staticmethod
    def authenticate_user():
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()
        users = Authentication.load_data(users_file)
        for user in users:
            if user['email'] == email and user['password'] == password:
                print("Authentication successful")
                return user
        print("Invalid credentials. Check email and password and try again.")
        return None
