from datetime import datetime
from Src.Staff_Management.employee import Employee
from Src.Staff_Management.utils import load_data, save_data, users_file, employee_file

# Define color constants for text formatting
BRIGHT_RED = "\033[91m"
BRIGHT_GREEN = "\033[92m"
BRIGHT_YELLOW = "\033[93m"
BRIGHT_BLUE = "\033[94m"
BRIGHT_MAGENTA = "\033[95m"
BRIGHT_CYAN = "\033[96m"
BRIGHT_WHITE = "\033[97m"
RESET = "\033[0m"

class StaffManagementSystem:
    def authenticate_user(self):
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()
        users = load_data(users_file)
        for user in users:
            if user['email'] == email and user['password'] == password:
                return user
        print("Invalid credentials.")
        return None

    def add_employee(self):
        user = self.authenticate_user()
        if not user:
            return

        gender = input("Enter gender (Male/Female/Other): ").strip().capitalize()
        employee = Employee(
            id=user['id'],
            name=user['name'],
            email=user['email'],
            password=user['password'],
            phone=user['phone'],
            date_of_birth=user['date_of_birth'],
            role=user['role'],
            gender=gender
        )
        employee.designation = input("Enter designation: ").title()
        employee.country = input("Enter country: ").title()
        employee.state = input("Enter state: ").title()
        employee.district = input("Enter district: ").title()
        employee.city_village = input("Enter city/village: ").title()
        employee.pincode = input("Enter pincode: ")
        employee.joining_date = input("Enter joining date (YYYY-MM-DD): ")
        employee.salary = input("Enter salary: ")

        employees = load_data(employee_file)
        employees.append(employee.to_dict())
        save_data(employee_file, employees)
        print("Employee added successfully.")

    def display_profile(self):
        user = self.authenticate_user()
        if not user:
            return
        
        employees = load_data(employee_file)
        for emp in employees:
            if emp['email'] == user['email']:
                print("\n=== Employee Profile ===")
                print("--------------------------------")
                print("   Personal Information")
                print("   --------------------")
                print(f"   Name           : {emp.get('name', 'N/A')}")
                print(f"   Gender         : {emp.get('gender', 'N/A')}")
                print(f"   Date of Birth  : {emp.get('date_of_birth', 'N/A')}")
                print(f"   Email          : {emp.get('email', 'N/A')}")
                print(f"   Phone          : {emp.get('phone', 'N/A')}")
                
                print("\n   Job Information")
                print("   --------------------")
                print(f"   Role           : {emp.get('role', 'N/A')}")
                print(f"   Designation    : {emp.get('designation', 'N/A')}")
                print(f"   Joining Date   : {emp.get('joining_date', 'N/A')}")
                print(f"   Salary         : {emp.get('salary', 'N/A')}")
                print(f"   Status         : {emp.get('status', 'N/A')}")
                if emp.get('status') == 'inactive':
                    print(f"   Resign Date    : {emp.get('resign_date', 'N/A')}")

                print("\n   Address Information")
                print("   --------------------")
                print(f"   Country        : {emp.get('country', 'N/A')}")
                print(f"   State          : {emp.get('state', 'N/A')}")
                print(f"   District       : {emp.get('district', 'N/A')}")
                print(f"   City/Village   : {emp.get('city_village', 'N/A')}")
                print(f"   Pincode        : {emp.get('pincode', 'N/A')}")
                print("--------------------------------\n")
                return
        
        print("Employee not found.")

    def update_profile(self):
        email = input("Enter the email of the employee to update: ")
        employees = load_data(employee_file)
        for emp in employees:
            if emp['email'] == email:
                print("Updating employee profile. Leave fields blank to keep current values.")
                emp['designation'] = input(f"Designation [{emp['designation']}]: ") or emp['designation']
                emp['salary'] = input(f"Salary [{emp['salary']}]: ") or emp['salary']
                emp['status'] = input(f"Status (active/inactive) [{emp['status']}]: ") or emp['status']
                if emp['status'] == 'inactive':
                    emp['resign_date'] = input("Enter resign date (YYYY-MM-DD): ")
                save_data(employee_file, employees)
                print("Employee profile updated successfully.")
                return
        print("Employee not found.")

    def delete_employee(self):
        email = input("Enter the email of the employee to delete: ")
        employees = load_data(employee_file)
        employees = [emp for emp in employees if emp['email'] != email]
        save_data(employee_file, employees)
        print("Employee deleted successfully.")

    def display_all_profiles(self):
        employees = load_data(employee_file)
        if not employees:
            print("No employees found.")
            return

        print("\n=== All Employee Profiles ===")
        for i, emp in enumerate(employees, start=1):
            print("\n--------------------------------")
            print(f"       Employee {i}")
            print("--------------------------------")
            print("   Personal Information")
            print("   --------------------")
            print(f"   Name           : {emp.get('name', 'N/A')}")
            print(f"   Gender         : {emp.get('gender', 'N/A')}")
            print(f"   Date of Birth  : {emp.get('date_of_birth', 'N/A')}")
            print(f"   Email          : {emp.get('email', 'N/A')}")
            print(f"   Phone          : {emp.get('phone', 'N/A')}")

            print("\n   Job Information")
            print("   --------------------")
            print(f"   Role           : {emp.get('role', 'N/A')}")
            print(f"   Designation    : {emp.get('designation', 'N/A')}")
            print(f"   Joining Date   : {emp.get('joining_date', 'N/A')}")
            print(f"   Salary         : {emp.get('salary', 'N/A')}")
            print(f"   Status         : {emp.get('status', 'N/A')}")
            if emp.get('status', 'active') == 'inactive':
                print(f"   Resign Date    : {emp.get('resign_date', 'N/A')}")

            print("\n   Address Information")
            print("   --------------------")
            print(f"   Country        : {emp.get('country', 'N/A')}")
            print(f"   State          : {emp.get('state', 'N/A')}")
            print(f"   District       : {emp.get('district', 'N/A')}")
            print(f"   City/Village   : {emp.get('city_village', 'N/A')}")
            print(f"   Pincode        : {emp.get('pincode', 'N/A')}")
            print("--------------------------------\n")
