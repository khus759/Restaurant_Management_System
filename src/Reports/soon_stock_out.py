import json
from datetime import datetime, timedelta
from Src.Utility.path_manager import menu_file

class ExpirationReport:
    def __init__(self, menu_file=menu_file, days_until_expiration=3, low_stock_threshold=5):
        self.menu_file = menu_file
        self.days_until_expiration = days_until_expiration
        self.low_stock_threshold = low_stock_threshold  # Quantity threshold to consider low stock
        self.menu_data = self.load_menu_data()

    def load_menu_data(self):
        with open(self.menu_file, 'r') as file:
            return json.load(file)

    def generate_report(self):
        threshold_date = datetime.now() + timedelta(days=self.days_until_expiration)
        expiring_ingredients = []
        low_stock_ingredients = []

        for category_data in self.menu_data:  # assuming menu_data is a list
            category = category_data.get("category", "Unknown Category")
            items = category_data.get("items", [])

            for item in items:
                item_name = item.get("item name")
                stock_ingredients = item.get("stock_ingredients", {})

                for ingredient, details in stock_ingredients.items():
                    expiration_date = datetime.strptime(details["expiration_date"], "%Y-%m-%d")
                    quantity = details.get("quantity", 0)

                    # Check if ingredient is nearing expiration
                    if expiration_date <= threshold_date:
                        expiring_ingredients.append({
                            "item_name": item_name,
                            "ingredient": ingredient,
                            "expiration_date": details["expiration_date"],
                            "category": category
                        })

                    # Check if ingredient stock is low
                    if quantity <= self.low_stock_threshold:
                        low_stock_ingredients.append({
                            "item_name": item_name,
                            "ingredient": ingredient,
                            "quantity": quantity,
                            "category": category
                        })

        return expiring_ingredients, low_stock_ingredients

    def display_report(self):
        expiring_ingredients, low_stock_ingredients = self.generate_report()

        # Display expiring ingredients report
        if expiring_ingredients:
            print("Ingredients Nearing Expiration:")
            for entry in expiring_ingredients:
                print(f"Category: {entry['category']}, Item: {entry['item_name']}, Ingredient: {entry['ingredient']}, Expiration Date: {entry['expiration_date']}")
        else:
            print(f"No ingredients nearing expiration in the next {self.days_until_expiration} days.")

        # Display low stock ingredients report
        if low_stock_ingredients:
            print("\nIngredients Soon Going Out of Stock:")
            for entry in low_stock_ingredients:
                print(f"Category: {entry['category']}, Item: {entry['item_name']}, Ingredient: {entry['ingredient']}, Quantity: {entry['quantity']}")
        else:
            print(f"No ingredients are low in stock (below {self.low_stock_threshold} units).")

        # Summary of soon-expiring and low-stock ingredients
        print("\nSummary of Ingredients Nearing Expiration and Low Stock:")
        summary = {}
        for entry in expiring_ingredients + low_stock_ingredients:
            category = entry['category']
            item_name = entry['item_name']
            ingredient = entry['ingredient']

            if category not in summary:
                summary[category] = {}
            if item_name not in summary[category]:
                summary[category][item_name] = []
            summary[category][item_name].append(ingredient)

        for category, items in summary.items():
            print(f"\nCategory: {category}")
            for item_name, ingredients in items.items():
                ingredients_list = ', '.join(ingredients)
                print(f"  Item: {item_name}, Ingredients: {ingredients_list}")
