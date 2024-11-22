import json
from datetime import datetime, timedelta
from Src.Utility.path_manager import menu_file
from Src.Messages.reports import Report

class ExpirationReport:
    def __init__(self, menu_file=menu_file, days_until_expiration=3, low_stock_threshold=5):
        self.menu_file = menu_file
        self.days_until_expiration = days_until_expiration
        self.low_stock_threshold = low_stock_threshold
        self.menu_data = self.load_menu_data()
        self.report = Report()

    def load_menu_data(self):
        with open(self.menu_file, 'r') as file:
            return json.load(file)

    def generate_report(self):
        threshold_date = datetime.now() + timedelta(days=self.days_until_expiration)
        expiring_ingredients = []
        low_stock_ingredients = []

        for category_data in self.menu_data:
            category = category_data.get("category", "Unknown Category")
            items = category_data.get("items", [])

            for item in items:
                item_name = item.get("item name")
                stock_ingredients = item.get("stock_ingredients", {})

                for ingredient, details in stock_ingredients.items():
                    expiration_date = datetime.strptime(details["expiration_date"], "%Y-%m-%d")
                    quantity = details.get("quantity", 0)

                    if expiration_date <= threshold_date:
                        expiring_ingredients.append({
                            "item_name": item_name,
                            "ingredient": ingredient,
                            "expiration_date": details["expiration_date"],
                            "category": category
                        })

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

        if expiring_ingredients:
            self.report.show_expiring_ingredients_header(self.days_until_expiration)
            for entry in expiring_ingredients:
                self.report.show_expiring_ingredient_entry(entry)
        else:
            self.report.no_expiring_ingredients(self.days_until_expiration)

        if low_stock_ingredients:
            self.report.show_low_stock_header(self.low_stock_threshold)
            for entry in low_stock_ingredients:
                self.report.show_low_stock_entry(entry)
        else:
            self.report.no_low_stock_ingredients(self.low_stock_threshold)

        if expiring_ingredients or low_stock_ingredients:
            self.report.show_summary_header()
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
                self.report.show_summary_category(category)
                for item_name, ingredients in items.items():
                    self.report.show_summary_item(item_name, ingredients)
        else:
            self.report.no_summary()
