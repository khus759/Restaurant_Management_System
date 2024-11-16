class Menu_Message:
    # Define color codes
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"
    BRIGHT_CYAN = "\033[96m"

    def print_item_added(self, name, category, item_id):
        print(f"{self.GREEN}✔️ Item '{name}' added successfully under '{category}' category with ID '{item_id}'.{self.RESET}")

    def print_item_updated(self, item_id):
        print(f"{self.GREEN}✔️ Item '{item_id}' updated successfully.{self.RESET}")

    def print_item_deleted(self, item_id, category):
        print(f"{self.GREEN}✔️ Item '{item_id}' deleted successfully from '{category}' category.{self.RESET}")

    def print_item_not_found(self, item_id, category):
        print(f"{self.RED}❌ Item '{item_id}' not found in '{category}' category.{self.RESET}")

    def print_invalid_category(self, category):
        print(f"{self.RED}❌ Invalid category: {category}{self.RESET}")

    def print_menu_header(self):
        print(f"\n{self.BLUE}Menu:{self.RESET}")
        header = f"{'ID':<10}{'Name':<30}{'Prices':<40}{'Ingredients':<50}"
        print(f"{self.BRIGHT_CYAN}{header}{self.RESET}")
        print(f"{self.BLUE}{'=' * 130}{self.RESET}")

    def print_category_header(self, category):
        print(f"\n{self.YELLOW}Category: {category}{self.RESET}")
        print(f"{self.YELLOW}{'-' * 130}{self.RESET}")

    def print_item_details(self, item_id, item_name, price_details, ingredients):
        print(f"{self.YELLOW}{item_id:<10}{item_name:<30}{price_details:<40}{ingredients:<50}{self.RESET}")

    def print_invalid_input_error(self, error_message):
        print(f"{self.RED}Error: {error_message}{self.RESET}")

    def exit_message(self):
        print(f"{self.BLUE} 😀 Thank you for using the Menu Management System. Goodbye!{self.RESET}")

    def welcome_message(self):
        print(f"{self.BLUE} 😀 Welcome to the Menu Management System! Please follow the prompts to continue.😜{self.RESET}")

    def print_ingredient_added(self, ingredient, item_id):
        print(f"{self.GREEN}✔️ Ingredient '{ingredient}' added successfully to item '{item_id}'.{self.RESET}")

    def print_ingredient_not_in_item(self, ingredient, item_id):
        print(f"{self.RED}❌ Ingredient '{ingredient}' not found in item '{item_id}' ingredients.{self.RESET}")

    def print_expiry_date_added(self, ingredient, expiry_date, item_id):
        print(f"{self.GREEN}✔️ Expiry date '{expiry_date}' added successfully for ingredient '{ingredient}' in item '{item_id}'.{self.RESET}")

    def print_invalid_expiry_date(self, expiry_days):
        print(f"{self.RED}❌ Invalid expiry days: '{expiry_days}'. It must be a positive integer.{self.RESET}")

    def print_stock_ingredients_check(self, expired_ingredients, item_id):
        if expired_ingredients:
            print(f"{self.RED}❌ Expired ingredients for item '{item_id}': {', '.join(expired_ingredients)}{self.RESET}")
        else:
            print(f"{self.GREEN}✔️ All ingredients are in stock for item '{item_id}'.{self.RESET}")

    def print_ingredient_not_listed(self, ingredient, item_id):
        print(f"{self.RED}❌ Ingredient '{ingredient}' is not listed in the ingredients of item '{item_id}'.{self.RESET}")

    def print_no_stock_data(self, item_id):
        print(f"{self.RED}❌ No stock data available for item '{item_id}'.{self.RESET}")

    def print_item_not_found_for_category(self, category, item_id):
        print(f"{self.RED}❌ Item '{item_id}' not found in '{category}' category.{self.RESET}")

    def print_no_expired_ingredients(self, item_id):
        print(f"{self.GREEN}✔️ No expired ingredients found for item '{item_id}'.{self.RESET}")

    def print_ingredient_found_in_item(self, ingredient, item_id):
        print(f"{self.GREEN}✔️ Ingredient '{ingredient}' found in item '{item_id}' ingredients.{self.RESET}")
