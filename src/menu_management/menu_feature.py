from Src.Menu_management.menu import MenuItem
from Src.Utility.validation import *
import os
import json

class MenuManagement:
    def __init__(self, path='src/database/menu.json'):
        self.path = path
        self.menu_items = {}
        self.load_menu()

    def load_menu(self):
        if os.path.isfile(self.path):
            try:
                with open(self.path, 'r') as file:
                    menu_data = json.load(file)
                    if isinstance(menu_data, list) and len(menu_data) > 0:
                        self.menu_items = menu_data[0]
                    else:
                        raise ValueError("Invalid menu data format.")
            except (json.JSONDecodeError, ValueError):
                print("Error loading menu. Initializing to default menu.")
                self.initialize_menu()
        else:
            self.initialize_menu()

    def initialize_menu(self):
        self.menu_items = {
            "Veg": [],
            "Non-Veg": [],
            "Starter": [],
            "Drink": [],
            "Ice Cream": [],
            "Sweet": [],
            "Roti":[],
            "Rice":[],
            "Paratha":[]
        }

    def save_menu(self):
        try:
            with open(self.path, 'w') as file:
                json.dump([self.menu_items], file, indent=2)
        except Exception as e:
            print(f"An error occurred while saving the menu: {e}")

    def generate_item_id(self, category):
        prefix = {
            "Veg": "VG",
            "Non-Veg": "NV",
            "Starter": "ST",
            "Drink": "DR",
            "Ice Cream": "IC",
            "Sweet": "SW",
            "Roti":"RT",
            "Rice":"RI",
            "Paratha":"PR"

        }
        count = len(self.menu_items[category]) + 1
        return f"{prefix[category]}{count:02d}"

    def add_menu_item(self):
        while True:
            category = input("Enter category (Veg/Non-Veg/Starter/Drink/Ice Cream/Sweet/Roti/Rice/Paratha): ").title()
            if category not in self.menu_items:
                print("Invalid category.")
                continue
            
            name = validate_name(input("Enter item name: ").strip())
            while True:
                try:
                    price = float(input("Enter item price: "))
                    if price <=0:
                        print("please enter valid price")
                        continue
                    break
                except ValueError:
                    print("Invalid price. Please enter a number.")

            item_id = self.generate_item_id(category)

            new_item = MenuItem(item_id, name, price)
            self.menu_items[category].append(new_item.to_dict())
            self.save_menu()
            print("Menu item added successfully.")
            
            if input("Do you want to add another item? (yes/no): ").lower() != "yes":
                break

    def update_menu_item(self):
        while True:
            category = input("Enter category (Veg/Non-Veg/Starter/Drink/Ice Cream/Sweet/Roti/Rice/Paratha): ").title()
            if category not in self.menu_items:
                print("Invalid category.")
                continue

            item_id = input("Enter item ID to update: ")
            for item in self.menu_items[category]:
                if item["item id"] == item_id:
                    item["item name"] = input("Enter new item name: ").strip()
                    while True:
                        try:
                            item["price"] = float(input("Enter new item price: "))
                            break
                        except ValueError:
                            print("Invalid price. Please enter a number.")
                    self.save_menu()
                    print("Menu item updated successfully.")
                    break
            else:
                print("Menu item not found.")
            
            if input("Do you want to update another item? (yes/no): ").lower() != "yes":
                break

    def delete_menu_item(self):
        while True:
            category = input("Enter category (Veg/Non-Veg/Starter/Drink/Ice Cream/Sweet): ").title()
            if category not in self.menu_items:
                print("Invalid category.")
                continue

            item_id = input("Enter item ID to delete: ")
            self.menu_items[category] = [item for item in self.menu_items[category] if item["item id"] != item_id]
            self.save_menu()
            print("Menu item deleted successfully.")
            
            if input("Do you want to delete another item? (yes/no): ").lower() != "yes":
                break

    def show_menu(self):
        print("\nCurrent Menu:")
        for category, items in self.menu_items.items():
            print(f"{category}:")
            for item in items:
                print(f"  - ID: {item['item id']}, Name: {item['item name']}, Price: {item['price']:.2f}")