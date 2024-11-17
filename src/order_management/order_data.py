import json
import uuid
from Src.Utility.path_manager import menu_file, order_file, users_file
from Src.Messages.order import OrderOutputHandler

handle = OrderOutputHandler()

def load_menu():
    with open(menu_file, 'r') as file:
        menu_data = json.load(file)
        return menu_data[0]

def load_orders():
    try:
        with open(order_file, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def save_orders(orders):
    with open(order_file, 'w') as file:
        json.dump(orders, file, indent=4)

def generate_order_id():
    try:
        return f"{str(uuid.uuid4().hex[:6])}"
    except Exception as e:
        handle.generate_message()
        return None

def load_current_user():
    try:
        with open(users_file, 'r') as file:
            users = json.load(file)
            # Assume the first user in users.json is the current logged-in user for this example
            return users[0] if users else {}
    except FileNotFoundError:
        return {}
