
from Src.Utility.color import Colors
colour = Colors()

def profile_updated():
    print(f"{Colors.GREEN} ✔️ Profile updated successfully.{Colors.RESET}")

def invalid_credentials():
    print(f"{Colors.RED}❌ Invalid credentials.{Colors.RESET}")

def employee_added():
    print(f"{Colors.GREEN}✔️ Employee added successfully.{Colors.RESET}")

def employee_not_found():
    print(f"{Colors.RED}❌ Employee not found.{Colors.RESET}")

def employee_deleted():
    print(f"{Colors.GREEN}✔️ Employee deleted successfully.{Colors.RESET}")

def no_employees_found():
    print("No employees found.")

def display_profile(emp):
    print(f"\n{Colors.CYAN}=== Employee Profile ==={Colors.RESET}")
    print("--------------------------------")
    print(f"{Colors.BRIGHT_MAGENTA}   Personal Information {Colors.RESET}")
    print("   --------------------")
    print(f"   Name           : {emp.get('name', 'N/A')}")
    print(f"   Gender         : {emp.get('gender', 'N/A')}")
    print(f"   Date of Birth  : {emp.get('date_of_birth', 'N/A')}")
    print(f"   Email          : {emp.get('email', 'N/A')}")
    print(f"   Phone          : {emp.get('phone', 'N/A')}")
    
    print(f"\n{Colors.BRIGHT_MAGENTA}   Job Information {Colors.RESET}")
    print("   --------------------")
    print(f"   Role           : {emp.get('role', 'N/A')}")
    print(f"   Designation    : {emp.get('designation', 'N/A')}")
    print(f"   Joining Date   : {emp.get('joining_date', 'N/A')}")
    print(f"   Salary         : {emp.get('salary', 'N/A')}")
    print(f"   Status         : {emp.get('status', 'N/A')}")
    if emp.get('status') == 'inactive':
        print(f"   Resign Date    : {emp.get('resign_date', 'N/A')}")

    print(f"\n{Colors.BRIGHT_MAGENTA}   Address Information {Colors.RESET}")
    print("   --------------------")
    print(f"   Country        : {emp.get('country', 'N/A')}")
    print(f"   State          : {emp.get('state', 'N/A')}")
    print(f"   District       : {emp.get('district', 'N/A')}")
    print(f"   City/Village   : {emp.get('city_village', 'N/A')}")
    print(f"   Pincode        : {emp.get('pincode', 'N/A')}")
    print(f"{Colors.GREEN}--------------------------------{Colors.RESET}\n")

def display_all_profiles(emp, index):
    print("\n--------------------------------")
    print(f"{Colors.YELLOW}       Employee {index}{Colors.RESET}")
    print("--------------------------------")
    display_profile(emp)

def welcome_message():
    print(f"{Colors.LIGHT_TEAL} 😀 Welcome to the Staff Management System! Please follow the prompts to continue.😜{Colors.RESET}")

def exit_message():
    print(f"{Colors.LIGHT_MAGENTA} 😀 Thank you for using the Staff Management System. Goodbye!{Colors.RESET}")
