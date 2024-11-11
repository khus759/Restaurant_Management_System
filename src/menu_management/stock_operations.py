import json
from datetime import datetime, timedelta
from Src.Utility.user_input import get_valid_input
from Src.Utility.validation import *

class StockOperations:
    def __init__(self, menu_data, json_file):
        self.menu_data = menu_data
        self.json_file = json_file

    def add_stock_ingredient(self):
        category = get_valid_input("Enter category: ",validate_category)
        item_id = get_valid_input("Enter item ID: ",validate_item_id)
        ingredient = input("Enter ingredient name: ")

        for item in self.menu_data[0].get(category, []):
            if item['item id'] == item_id:
                if ingredient not in item.get('ingredients', []):
                    print(f"The ingredient '{ingredient}' is not listed in the ingredients of item '{item_id}'.")
                    return

                while True:
                    try:
                        expiry_days = int(input("Enter expiry days from today: "))
                        if expiry_days < 0:
                            raise ValueError("Expiry days cannot be negative.")
                        break
                    except ValueError as e:
                        print(f"Invalid input for expiry days: {e}")

                expiry_date = datetime.now() + timedelta(days=expiry_days)
                if 'stock_ingredients' not in item:
                    item['stock_ingredients'] = {}
                item['stock_ingredients'][ingredient] = expiry_date.strftime("%Y-%m-%d")
                
                with open(self.json_file, 'w') as file:
                    json.dump(self.menu_data, file, indent=4)

                print(f"Ingredient '{ingredient}' with expiry added to item '{item_id}'.")
                return

        print(f"Item '{item_id}' not found in '{category}' category.")

    def check_stock_ingredients(self):
        category = get_valid_input("Enter category: ",validate_category)
        item_id = get_valid_input("Enter item ID: ",validate_item_id)

        current_date = datetime.now().date()
        for item in self.menu_data[0].get(category, []):
            if item['item id'] == item_id:
                expired_ingredients = []
                if 'stock_ingredients' in item:
                    for ingredient, expiry_str in item['stock_ingredients'].items():
                        if ingredient not in item.get('ingredients', []):
                            print(f"The ingredient '{ingredient}' is not listed in the ingredients of item '{item_id}'.")
                            return

                        expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d").date()
                        if expiry_date < current_date:
                            expired_ingredients.append(ingredient)
                    if expired_ingredients:
                        print(f"Out-of-stock ingredients for item '{item_id}': {expired_ingredients}")
                    else:
                        print(f"All ingredients in stock for item '{item_id}'.")
                else:
                    print(f"No stock data for item '{item_id}'.")
                return

        print(f"Item '{item_id}' not found in '{category}' category.")
