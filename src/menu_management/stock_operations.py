import json
from datetime import datetime, timedelta
import re
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

        ingredients = []
        print("Enter ingredient names one by one. Type 'done' when finished.")
        while True:
            ingredient = input("Enter ingredient name: ").strip().lower()  # Lowercase and strip any extra spaces
            if ingredient == 'done':  # Stop when the user types 'done'
                break
            try:
                validate_ingredient_input(ingredient)  # Validate the ingredient input
                ingredients.append(ingredient)  # Collect valid ingredients
            except ValueError as e:
                print(e)  # Notify the user about validation errors

        if not ingredients:
            print("No ingredients were added.")
            return

        # Process the collected ingredients
        for item in self.menu_data[0].get(category, []):
            if item['item id'].lower() == item_id.lower():  # Compare item IDs case insensitively
                # Normalize ingredient names in the item to lowercase for comparison
                item_ingredients = [ingredient.lower() for ingredient in item.get('ingredients', [])]
                if not set(ingredients).issubset(set(item_ingredients)):  # Check if entered ingredients are a subset of item ingredients
                    self.message.print_invalid_input_error(
                        f"Some ingredients are not listed in the ingredients of item '{item_id}'."
                    )
                    print(f"Item ingredients: {item_ingredients}")
                    print(f"Entered ingredients: {ingredients}")
                    return

                expiry_days = int(get_valid_input("Enter expiry days from today: ", lambda x: int(x) >= 0))
                expiry_date = datetime.now() + timedelta(days=expiry_days)

                # Add expiry dates for each ingredient
                for ingredient in ingredients:
                    item.setdefault('stock_ingredients', {})[ingredient] = expiry_date.strftime("%Y-%m-%d")

                # Save changes to the JSON file
                with open(self.json_file, 'w') as file:
                    json.dump(self.menu_data, file, indent=4)

                print(f"Ingredients {', '.join(ingredients)} have been added to item '{item_id}' under category '{category}'.")
                return

        self.message.print_item_not_found(item_id, category)

    def check_stock_ingredients(self):
        category = get_valid_input("Enter category: ", lambda value: validate_category(value, self.menu_data)).title()
        item_id = get_valid_input("Enter item ID : ", lambda value: validate_item_id(value, self.menu_data, category)).upper()

        current_date = datetime.now().date()
        for item in self.menu_data[0].get(category, []):
            if item['item id'].lower() == item_id.lower():  # Compare item IDs case insensitively
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


def validate_ingredient_input(value):
    """Validate the ingredients input."""
    value = value.strip()  # Remove leading/trailing spaces

    # Check if the input is not empty
    if not value:
        raise ValueError("Ingredient input cannot be blank.")

    # Allow alphabetic characters and spaces (e.g., "ground pepper", "rice flour")
    if not re.match(r'^[a-zA-Z\s\-]+$', value):
        raise ValueError("Ingredient names should only contain letters, spaces, or hyphens.")

    return value
