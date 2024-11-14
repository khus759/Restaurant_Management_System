class Menu_Message:
    # Define color codes
    GREEN = "\033[92m"
    RED = "\033[91m"
    BLUE = "\033[94m"
    YELLOW = "\033[93m"
    RESET = "\033[0m"

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
        print(header)
        print(f"{self.BLUE}{'=' * 130}{self.RESET}")

    def print_category_header(self, category):
        print(f"\n{self.YELLOW}Category: {category}{self.RESET}")
        print(f"{self.YELLOW}{'-' * 130}{self.RESET}")

    def print_item_details(self, item_id, item_name, price_details, ingredients):
        print(f"{self.YELLOW}{item_id:<10}{item_name:<30}{price_details:<40}{ingredients:<50}{self.RESET}")

    def print_invalid_input_error(self, error_message):
        print(f"{self.RED}Error: {error_message}{self.RESET}")
