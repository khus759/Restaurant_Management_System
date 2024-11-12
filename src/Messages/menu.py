class Menu_Message():
    
    def print_item_added(self, name, category, item_id):
        print(f"Item '{name}' added successfully under '{category}' category with ID '{item_id}'.")

    def print_item_updated(self, item_id):
        print(f"Item '{item_id}' updated successfully.")

    def print_item_deleted(self, item_id, category):
        print(f"Item '{item_id}' deleted successfully from '{category}' category.")

    def print_item_not_found(self,item_id, category):
        print(f"Item '{item_id}' not found in '{category}' category.")

    def print_invalid_category(self, category):
        print(f"Invalid category: {category}")

    def print_menu_header(self):
        print("\nMenu:")
        header = f"{'ID':<10}{'Name':<30}{'Prices':<40}{'Ingredients':<50}"
        print(header)
        print("=" * 130)  

    def print_category_header(self, category):
        print(f"\nCategory: {category}")
        print("-" * 130)

    def print_item_details(self, item_id, item_name, price_details, ingredients):
        print(f"{item_id:<10}{item_name:<30}{price_details:<40}{ingredients:<50}")

    def print_invalid_input_error(self, error_message):
        print(f"Error: {error_message}")
    