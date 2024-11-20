from Src.Utility.color import Colors
class Menu_Message:
    def __init__(self):
        self.color = Colors()
    

    def print_item_added(self, name, category, item_id):
        print(f"{Colors.GREEN}✔️ Item '{name}' added successfully under '{category}' category with ID '{item_id}'.{Colors.RESET}")

    def print_item_updated(self, item_id):
        print(f"{Colors.GREEN}✔️ Item '{item_id}' updated successfully.{Colors.RESET}")

    def print_item_deleted(self, item_id, category):
        print(f"{Colors.GREEN}✔️ Item '{item_id}' deleted successfully from '{category}' category.{Colors.RESET}")

    def print_item_not_found(self, item_id, category):
        print(f"{Colors.RED}❌ Item '{item_id}' not found in '{category}' category.{Colors.RESET}")

    def print_invalid_category(self, category):
        print(f"{Colors.RED}❌ Invalid category: {category}{Colors.RESET}")

    def print_menu_header(self):
        print(f"\n{Colors.BLUE}Menu:{Colors.RESET}")
        header = f"{Colors.CYAN}{'ID':<10}{'Name':<30}{'Prices':<40}{'Ingredients':<50{Colors.RESET}}"
        print(f"{Colors.BRIGHT_CYAN}{header}{Colors.RESET}")
        print(f"{Colors.BLUE}{'=' * 130}{Colors.RESET}")

    def print_category_header(self, category):
        print(f"\n{Colors.YELLOW}Category: {category}{Colors.RESET}")
        print(f"{Colors.BRIGHT_MAGENTA}{'-' * 130}{Colors.RESET}")

    def print_item_details(self, item_id, item_name, price_details, ingredients):
        print(f"{Colors.YELLOW}{item_id:<10}{item_name:<30}{price_details:<40}{ingredients:<50}{Colors.RESET}")

    def print_invalid_input_error(self, error_message):
        print(f"{Colors.RED}Error: {error_message}{Colors.RESET}")

    def exit_message(self):
        print(f"{Colors.LIGHT_ORANGE}  Thank you for using the Menu Management System. Goodbye!{Colors.RESET}")

    def welcome_message(self):
        print(f"{Colors.LIGHT_PEACH}  Welcome to the Menu Management System! Please follow the prompts to continue.{Colors.RESET}")

    def print_ingredient_added(self, ingredient, item_id):
        print(f"{Colors.GREEN}✔️ Ingredient '{ingredient}' added successfully to item '{item_id}'.{Colors.RESET}")

    def print_ingredient_not_in_item(self, ingredient, item_id):
        print(f"{Colors.RED}❌ Ingredient '{ingredient}' not found in item '{item_id}' ingredients.{Colors.RESET}")

    def print_expiry_date_added(self, ingredient, expiry_date, item_id):
        print(f"{Colors.GREEN}✔️ Expiry date '{expiry_date}' added successfully for ingredient '{ingredient}' in item '{item_id}'.{Colors.RESET}")

    def print_invalid_expiry_date(self, expiry_days):
        print(f"{Colors.RED}❌ Invalid expiry days: '{expiry_days}'. It must be a positive integer.{Colors.RESET}")

    def print_stock_ingredients_check(self, expired_ingredients, item_id):
        if expired_ingredients:
            print(f"{Colors.RED}❌ Expired ingredients for item '{item_id}': {', '.join(expired_ingredients)}{Colors.RESET}")
        else:
            print(f"{Colors.GREEN}✔️ All ingredients are in stock for item '{item_id}'.{Colors.RESET}")

    def print_ingredient_not_listed(self, ingredient, item_id):
        print(f"{Colors.RED}❌ Ingredient '{ingredient}' is not listed in the ingredients of item '{item_id}'.{Colors.RESET}")

    def print_no_stock_data(self, item_id):
        print(f"{Colors.RED}❌ No stock data available for item '{item_id}'.{Colors.RESET}")

    def print_item_not_found_for_category(self, category, item_id):
        print(f"{Colors.RED}❌ Item '{item_id}' not found in '{category}' category.{Colors.RESET}")

    def print_no_expired_ingredients(self, item_id):
        print(f"{Colors.GREEN}✔️ No expired ingredients found for item '{item_id}'.{Colors.RESET}")

    def print_ingredient_found_in_item(self, ingredient, item_id):
        print(f"{Colors.GREEN}✔️ Ingredient '{ingredient}' found in item '{item_id}' ingredients.{Colors.RESET}")
