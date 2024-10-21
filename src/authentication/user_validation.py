
import re

def validate_name(name):
    if not name.strip():
        return "Name cannot be blank."
    if any(char.isdigit() for char in name):
        return "Name cannot contain numbers."
    if re.search(r'[^a-zA-Z\s]', name):
        return "Name cannot contain special characters."
    return None

def validate_username(username):
    if not username.strip():
        return "UserName cannot be blank."
    if len(username) < 6:
        return "Username must be at least 6 characters long."
    return None

def validate_password(password):
    if not password.strip():
        return "Password cannot be blank."
    if len(password) < 6:
        return "Password must be at least 6 characters long."
    return None

def validate_role(role):
    role = role.upper()
    if not role.strip():
        return "Role cannot be blank."
    if role not in ['OWNER', 'STAFF']:
        return "Role must be either 'Owner' or 'Staff'."
    return None
