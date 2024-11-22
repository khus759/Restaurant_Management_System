import json
from Src.Utility.user_input import get_valid_input
from Src.Utility.validation import (
    validate_category, validate_name, validate_price,
     validate_item_id
)
from Src.Messages.menu import Menu_Message
from Src.Utility.color import Colors
from Src.Error.log_exception import logging

class ItemOperations:
    def __init__(self, menu_data, json_file):
        self.menu_data = menu_data
        self.json_file = json_file
        self.menu_handle = Menu_Message()

    def generate_item_id(self, category):
        # Generates a unique item ID based on the category and item count
        prefix = category[:2].upper()
        count = len(self.menu_data[0].get(category, [])) + 1
        return f"{prefix}{count:02d}"

    def get_yes_no_input(self, prompt):
        # Helper function to validate yes/no input
        while True:
            response = input(prompt).strip().lower()
            if response in ['yes', 'no']:
                return response
            else:
                print("Invalid input. Please enter 'yes' or 'no'.")

    def add_item(self):
        # Adds a new item to the menu
        category = get_valid_input("Enter category: ", lambda value: validate_category(value, self.menu_data)).title()
        item_id = self.generate_item_id(category).upper()
        name = get_valid_input("Enter item name: ", validate_name).title()

        # Prompt for portion sizes with validation for "yes" or "no"
        has_portion_sizes = self.get_yes_no_input("Does this item have half and full portions? (yes/no): ")

        prices = {}
        if has_portion_sizes == 'yes':
            prices["half"] = int(get_valid_input("Enter half portion price (integer): ", validate_price))
            prices["full"] = int(get_valid_input("Enter full portion price (integer): ", validate_price))
        else:
            prices["single"] = int(get_valid_input("Enter item price (integer): ", validate_price))

        # Prompt for adding ingredients with validation
        add_ingredients = self.get_yes_no_input("Would you like to add ingredients? (yes/no): ")
        ingredients = []
        if add_ingredients == 'yes':
            ingredients_input = input("Enter ingredients (comma-separated): ").strip()
            ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',') if ingredient.strip()]

        # Set ingredients to "------------" if the list is empty
        new_item = {
            "item id": item_id,
            "item name": name,
            "prices": prices,
            "ingredients": ingredients if ingredients else "------------"
        }

        # Append the new item to the menu data
        if category in self.menu_data[0]:
            self.menu_data[0][category].append(new_item)
        else:
            self.menu_data[0][category] = [new_item]

        # Save the updated menu to the JSON file
        with open(self.json_file, 'w') as file:
            json.dump(self.menu_data, file, indent=4)

        self.menu_handle.print_item_added(name, item_id, category)

    def update_item(self):
        # Updates an existing item in the menu
        category = get_valid_input("Enter category: ", lambda value: validate_category(value, self.menu_data)).title()
        item_id = get_valid_input("Enter item ID to update: ", lambda value: validate_item_id(value, self.menu_data, category)).upper()
    
        for item in self.menu_data[0].get(category, []):
            if item['item id'] == item_id:
                name = input("Enter new item name (leave blank to keep current): ").strip()
                if name:
                    item['item name'] = name

                print("Current prices:", item['prices'])
                new_prices = {}
                for portion, current_price in item['prices'].items():
                    new_price = input(f"Enter new price for {portion} (integer, leave blank to keep current): ").strip()
                    if new_price:
                        try:
                            validated_price = validate_price(new_price)
                            if isinstance(validated_price, int):
                                new_prices[portion] = validated_price
                            else:
                                print(validated_price)
                                new_prices[portion] = current_price
                        except ValueError as e:
                            logging.exception("exception details")
                            print(f"Invalid price input: {e}. Keeping the current price for {portion}.")
                            new_prices[portion] = current_price
                    else:
                        new_prices[portion] = current_price
                item['prices'] = new_prices

                ingredients = input("Enter new ingredients (comma-separated, leave blank to keep current): ").strip()
                if ingredients:
                    item['ingredients'] = [ingredient.strip() for ingredient in ingredients.split(',')]
                elif not item['ingredients']:
                    item['ingredients'] = "------------"

                with open(self.json_file, 'w') as file:
                    json.dump(self.menu_data, file, indent=4)
                self.menu_handle.print_item_updated(item_id)
                return

        self.menu_handle.print_item_not_found(item_id, category)

    def delete_item(self):
        # Deletes an item from the menu
        category = get_valid_input("Enter category: ", lambda value: validate_category(value, self.menu_data)).title()
        item_id = get_valid_input("Enter item ID to delete: ", lambda value: validate_item_id(value, self.menu_data, category)).upper()

        items = self.menu_data[0].get(category, [])
        for item in items:
            if item['item id'] == item_id:
                items.remove(item)
                with open(self.json_file, 'w') as file:
                    json.dump(self.menu_data, file, indent=4)
                self.menu_handle.print_item_deleted(item_id, category)
                return

        self.menu_handle.print_item_not_found(item_id, category)

    def show_menu(self):
        print("\nMenu:")
        header = f"{'ID':<10}{'Name':<30}{'Prices':<40}{'Ingredients':<50}"
        print(header)
        print("=" * 130)
        for category, items in self.menu_data[0].items():
            self.menu_handle.print_category_header(category)
            for item in items:
                item_id = item['item id']
                item_name = item['item name']
                prices = item['prices']
                price_details = ', '.join([f"{size}: {price}" for size, price in prices.items()])
                ingredients = item.get('ingredients', "------------")
                if isinstance(ingredients, list):
                    ingredients = ', '.join(ingredients) if ingredients else "------------"
                print(f"{Colors.LIGHT_CORAL}{item_id:<10}{Colors.RESET}{Colors.LIGHT_SKY_BLUE}{Colors.LIGHT_AQUA}{item_name:<30}{Colors.RESET}{Colors.LIGHT_ORANGE}{price_details:<40}{Colors.RESET}{Colors.LIGHT_PINK}{ingredients:<50}{Colors.RESET}")
            print(f"{Colors.LIGHT_VIOLET}*" * 130)

