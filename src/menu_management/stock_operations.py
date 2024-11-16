
import json
from datetime import datetime, timedelta
from Src.Utility.user_input import get_valid_input
from Src.Utility.validation import *
from Src.Messages.menu import Menu_Message  

class StockOperations:
    def __init__(self, menu_data, json_file):
        self.menu_data = menu_data
        self.json_file = json_file
        self.message = Menu_Message()  

    def add_stock_ingredient(self):
        category = get_valid_input("Enter category: ", lambda value: validate_category(value, self.menu_data)).title()
        item_id = get_valid_input("Enter item ID : ", lambda value: validate_item_id(value, self.menu_data, category)).upper()
        ingredient = get_valid_input("Enter ingredient name: ", validate_ingredient_input).title()

        for item in self.menu_data[0].get(category, []):
            if item['item id'] == item_id:
                if ingredient not in item.get('ingredients', []):
                    self.message.print_invalid_input_error(f"The ingredient '{ingredient}' is not listed in the ingredients of item '{item_id}'.")
                    return

                expiry_days = int(get_valid_input("Enter expiry days from today: ", lambda x: int(x) >= 0))
                expiry_date = datetime.now() + timedelta(days=expiry_days)
                item.setdefault('stock_ingredients', {})[ingredient] = expiry_date.strftime("%Y-%m-%d")

                with open(self.json_file, 'w') as file:
                    json.dump(self.menu_data, file, indent=4)
                self.message.print_item_added(ingredient, category, item_id)
                return

        self.message.print_item_not_found(item_id, category)

    def check_stock_ingredients(self):
        category = get_valid_input("Enter category: ", lambda value: validate_category(value, self.menu_data)).title()
        item_id = get_valid_input("Enter item ID : ", lambda value: validate_item_id(value, self.menu_data, category)).upper()

        current_date = datetime.now().date()
        for item in self.menu_data[0].get(category, []):
            if item['item id'] == item_id:
                expired_ingredients = []
                for ingredient, expiry_str in item.get('stock_ingredients', {}).items():
                    expiry_date = datetime.strptime(expiry_str, "%Y-%m-%d").date()
                    if expiry_date < current_date:
                        expired_ingredients.append(ingredient)

                if expired_ingredients:
                    self.message.print_invalid_input_error(f"Out-of-stock ingredients for item '{item_id}': {expired_ingredients}")
                else:
                    self.message.print_item_updated(item_id)
                return

        self.message.print_item_not_found(item_id, category)
