from datetime import datetime, timedelta
import json
from Src.Menu_management.iteam_operations import ItemOperations
from Src.Menu_management.stock_operations import StockOperations
from Src.Utility.path_manager import menu_file
from Src.Messages.menu import Menu_Message  

class MenuManagement:
    def __init__(self, json_file=menu_file):
        self.json_file = json_file
        self.menu_data = self.load_data()
        self.item_operations = ItemOperations(self.menu_data, self.json_file)
        self.stock_operations = StockOperations(self.menu_data, self.json_file)
        self.message = Menu_Message() 

    def load_data(self):
        try:
            with open(self.json_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            self.message.print_invalid_input_error(f"{self.json_file} file not found.")
            return [{}]

    def save_data(self):
        try:
            with open(self.json_file, 'w') as file:
                json.dump(self.menu_data, file, indent=4)
            self.message.print_item_updated("Data")  # Reuse print_item_updated for save confirmation
        except Exception as e:
            self.message.print_invalid_input_error(f"An unexpected error occurred: {e}")

    def add_item(self):
        self.item_operations.add_item()

    def update_item(self):
        self.item_operations.update_item()

    def delete_item(self):
        self.item_operations.delete_item()

    def add_stock_ingredient(self):
        self.stock_operations.add_stock_ingredient()

    def check_stock_ingredients(self):
        self.stock_operations.check_stock_ingredients()

    def show_menu(self):
        self.item_operations.show_menu()

    def welcome(self):
        self.message.welcome_message()

    def exit(self):
        self.message.exit_message()
