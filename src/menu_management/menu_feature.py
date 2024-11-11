
import json
from datetime import datetime, timedelta
from Src.Menu_management.iteam_operations import ItemOperations
from Src.Menu_management.stock_operations import StockOperations
from Src.Utility.path_manager import menu_file

class MenuManagement:
    def __init__(self, json_file = menu_file):
        self.json_file = json_file
        self.menu_data = self.load_data()
        self.item_operations = ItemOperations(self.menu_data, self.json_file)
        self.stock_operations = StockOperations(self.menu_data, self.json_file)

    def load_data(self):
        try:
            with open(self.json_file, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print(f"Error: {self.json_file} file not found.")
            return [{}]

    def save_data(self):
        try:
            with open(self.json_file, 'w') as file:
                json.dump(self.menu_data, file, indent=4)
            print("Data saved successfully.")
        except Exception as e:
            print(f"An unexpected error occurred: {e}")

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
