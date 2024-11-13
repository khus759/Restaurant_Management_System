import json
from Src.Utility.user_input import get_valid_input
from Src.Utility.validation import validate_category, validate_name, validate_price, validate_ingredient_input, validate_has_portion_sizes, validate_item_id
from Src.Messages.menu import Menu_Message

class ItemOperations:
    def __init__(self, menu_data, json_file):
        self.menu_data = menu_data
        self.json_file = json_file
        self.menu_handle = Menu_Message()

    def generate_item_id(self, category):
        prefix = category[:2].upper()
        count = len(self.menu_data[0].get(category, [])) + 1
        return f"{prefix}{count:02d}"

    def add_item(self):
        # Loop until a valid category is entered
        category = get_valid_input("Enter category: ", lambda value: validate_category(value, self.menu_data)).title()
        item_id = self.generate_item_id(category).upper()
        name = get_valid_input("Enter item name: ", validate_name).title()

        try:
            
            while True:
                try:
                    has_portion_sizes = input("Does this item have half and full portions? (yes/no): ").strip().lower()
                    valid_response = validate_has_portion_sizes(has_portion_sizes)  # This will validate the input
                    break  
                except ValueError as e:
                    print(e)  

            prices = {}
            if valid_response == 'yes':
                prices["half"] = get_valid_input("Enter half portion price: ", validate_price)
                prices["full"] = get_valid_input("Enter full portion price: ", validate_price)
            else:
                prices["single"] = get_valid_input("Enter item price: ", validate_price)

        except ValueError as e:
            print(f"Error in price input: {e}")
            return

        try:
            
            while True:
                add_ingredients = input("Would you like to add ingredients? (yes/no): ").strip().lower()
                if add_ingredients in ['yes', 'no']:
                    break
                else:
                    print("Invalid input. Please enter 'yes' or 'no'.")

            ingredients = []
            if add_ingredients == 'yes':
                # Prompt for ingredients only if 'yes' was answered
                ingredients_input = get_valid_input("Enter ingredients (comma-separated): ",validate_ingredient_input).strip()
                ingredients = [ingredient.strip() for ingredient in ingredients_input.split(',')]

        except Exception as e:
            print(f"Error adding ingredients: {e}")
            return

        new_item = {
            "item id": item_id,
            "item name": name,
            "prices": prices,
            "ingredients": ingredients
        }

        if category in self.menu_data[0]:
            self.menu_data[0][category].append(new_item)
        else:
            self.menu_data[0][category] = [new_item]

        with open(self.json_file, 'w') as file:
            json.dump(self.menu_data, file, indent=4)
        
        self.menu_handle.print_item_added(name,item_id,category)
        

    def update_item(self):
        category = get_valid_input("Enter category: ", lambda value: validate_category(value, self.menu_data)).title()
        item_id = get_valid_input("Enter item ID to update: ", lambda value: validate_item_id(value, self.menu_data, category)).upper()

        for item in self.menu_data[0].get(category, []):
            if item['item id'] == item_id:
                name = input("Enter new item name (leave blank to keep current): ")
                if name:
                    item['item name'] = name

                price = input("Enter new price (leave blank to keep current): ")
                if price is not None:
                    item['prices'] = {"price": price}

                ingredients = input("Enter new ingredients (comma-separated, leave blank to keep current): ")
                if ingredients:
                    item['ingredients'] = [ingredient.strip() for ingredient in ingredients.split(',')]

                with open(self.json_file, 'w') as file:
                    json.dump(self.menu_data, file, indent=4)
                self.menu_handle.print_item_updated(item_id)
                return
        self.menu_handle.print_item_not_found(item_id,category)
        
    def delete_item(self):
        category = get_valid_input("Enter category: ", lambda value: validate_category(value, self.menu_data)).title()
        item_id = get_valid_input("Enter item ID to delete: ", lambda value: validate_item_id(value, self.menu_data, category)).upper()

        items = self.menu_data[0].get(category, [])
        for item in items:
            if item['item id'] == item_id:
                items.remove(item)
                with open(self.json_file, 'w') as file:
                    json.dump(self.menu_data, file, indent=4)

                self.menu_handle.print_item_deleted(item_id,category)   
                return

        self.menu_handle.print_item_not_found(item_id,category)

    def show_menu(self):
        print("\nMenu:")
        header = f"{'ID':<10}{'Name':<30}{'Prices':<40}{'Ingredients':<50}"
        print(header)
        print("=" * 130)  # Adjust the length of the separator as needed
        for category, items in self.menu_data[0].items():
            self.menu_handle.print_category_header(category)
            for item in items:
                item_id = item['item id']
                item_name = item['item name']
                prices = item['prices']
                price_details = ', '.join([f"{size}: {price}" for size, price in prices.items()])
                ingredients = item.get('ingredients', 'No ingredients listed')
                if isinstance(ingredients, list):
                    ingredients = ', '.join(ingredients)  # Convert list to string
                print(f"{item_id:<10}{item_name:<30}{price_details:<40}{ingredients:<50}")
            print("=" * 130)
