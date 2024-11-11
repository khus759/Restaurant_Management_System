import json
import uuid
from Src.Utility.path_manager import menu_file, order_file

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
    return f"{str(uuid.uuid4().hex[:6])}"