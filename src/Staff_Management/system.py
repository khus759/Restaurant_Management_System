import json
from datetime import datetime
from Src.Utility.path_manager import users_file , employee_file
users_file = 'users.json'
employee_file = 'employee.json'

class Employee:
    def __init__(self, id, name, email, password, phone, date_of_birth, role, **kwargs):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.role = role
        self.designation = kwargs.get("designation", "")
        self.country = kwargs.get("country", "")
        self.state = kwargs.get("state", "")
        self.district = kwargs.get("district", "")
        self.city_village = kwargs.get("city_village", "")
        self.pincode = kwargs.get("pincode", "")
        self.joining_date = kwargs.get("joining_date", "")
        self.salary = kwargs.get("salary", "")
        self.status = "active"  # Default status
        self.resign_date = None
        self.salary_records = {}  # Dictionary to store salary payment records

    def to_dict(self):
        return self._dict_

class StaffManagementSystem:
    def load_data(self, file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    def save_data(self, file_path, data):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    def authenticate_user(self):
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()
        users = self.load_data(users_file)
        for user in users:
            if user['email'] == email and user['password'] == password:
                print("Authentication successful")
                return user
        print("Invalid credentials. Check email and password and try again.")
        return None

    def add_employee(self):
        user = self.authenticate_user()
        if not user:
            return
        
        employee = Employee(
            id=user['id'],
            name=user['name'],
            email=user['email'],
            password=user['password'],
            phone=user['phone'],
            date_of_birth=user['date_of_birth'],
            role=user['role']
        )

        employee.designation = input("Enter designation: ").title()
        employee.country = input("Enter country: ").title()
        employee.state = input("Enter state: ")
        employee.district = input("Enter district: ").title()
        employee.city_village = input("Enter city/village: ").title()
        employee.pincode = input("Enter pincode: ")
        employee.joining_date = input("Enter joining date (YYYY-MM-DD): ")
        employee.salary = input("Enter salary: ")

        employees = self.load_data(employee_file)
        employees.append(employee.to_dict())
        self.save_data(employee_file, employees)
        print("\nEmployee added successfully.\n")

    def display_profile(self):
        user = self.authenticate_user()
        if not user:
            return
        
        employees = self.load_data(employee_file)
        for emp in employees:
            if emp['email'] == user['email']:
                print("\n" + "="*30)
                print("Employee Profile".center(30))
                print("="*30)
                for key, value in emp.items():
                    print(f"{key.capitalize()}: {value or ''}")
                print("="*30 + "\n")
                return
        print("Employee not found.\n")

    def delete_employee(self):
        user = self.authenticate_user()
        if not user:
            return
        
        users = self.load_data(users_file)
        employees = self.load_data(employee_file)

        users = [u for u in users if u['email'] != user['email']]
        self.save_data(users_file, users)

        for emp in employees:
            if emp['email'] == user['email']:
                emp['status'] = "unactive"
                emp['resign_date'] = datetime.now().strftime("%Y-%m-%d")
        self.save_data(employee_file, employees)
        print("\nEmployee deleted successfully.\n")

    def display_all_profiles(self):
        employees = self.load_data(employee_file)
        if not employees:
            print("No employees found.\n")
            return
        
        print("\n" + "="*30)
        print("All Employee Profiles".center(30))
        print("="*30)
        for emp in employees:
            print("\n-----------------------")
            for key, value in emp.items():
                print(f"{key.capitalize()}: {value or ''}")
        print("="*30 + "\n")

    def display_report(self):
        employees = self.load_data(employee_file)
        if not employees:
            print("No employees found.\n")
            return

        # Displaying selected fields
        print("\n" + "="*50)
        print("Employee Report".center(50))
        print("="*50)
        # Adjust column width and header formatting
        print("-" * 130)
        print(f"{'S.No':<5} {'ID':<10} {'Name':<30} {'Phone':<18} {'Designation':<20} {'Status':<10} {'Joining Date':<15} {'Resigning Date':<15}")
        print("-" * 130)
        for idx, emp in enumerate(employees, start=1):  # Adding index for serial number
            # Convert each field to a string to avoid NoneType errors
            print(f"{str(idx):<5} {str(emp.get('id', '')):<10} {str(emp.get('name', '')):<30} {str(emp.get('phone', '')):<15} {str(emp.get('designation', '')):<20} {str(emp.get('status', '')):<10} {str(emp.get('joining_date', '')):<15} {str(emp.get('resign_date', '')):<15}")
        print("="*130 + "\n")


    def manage_salary(self):
        user = self.authenticate_user()
        if not user or user['role'].lower() != 'owner':
            print("Access denied. Only owners can manage salaries.\n")
            return
        
        employees = self.load_data(employee_file)
        print("\nSelect an employee to manage salary:")
        for i, emp in enumerate(employees):
            print(f"{i + 1}. {emp.get('name', '')} ({emp.get('email', '')})")

        choice = int(input("Enter employee number: ")) - 1
        if choice < 0 or choice >= len(employees):
            print("Invalid choice.\n")
            return

        employee = employees[choice]
        print(f"\nManaging salary for {employee.get('name', '')}\n")

        while True:
            print("\nSalary Management Options:")
            print("1. Mark month as paid")
            print("2. View unpaid months")
            print("3. Exit")
            option = input("Choose an option: ")

            if option == '1':
                month = input("Enter month to mark as paid (YYYY-MM): ")
                if 'salary_records' not in employee:
                    employee['salary_records'] = {}
                employee['salary_records'][month] = "Paid"
                print(f"\nMarked {month} as paid.")
            elif option == '2':
                unpaid_months = [m for m, status in employee.get('salary_records', {}).items() if status != "Paid"]
                print("\nUnpaid Months:", unpaid_months if unpaid_months else "All months are paid.")
            elif option == '3':
                break
            else:
                print("Invalid option. Try again.")

        self.save_data(employee_file, employees)
        print("\nSalary management completed.\n")

# Main program loop
if __name__ == "__main__":
    sms = StaffManagementSystem()
    while True:
        print("\nStaff Management System")
        print("1. Add Employee")
        print("2. Display Profile")
        print("3. Delete Employee")
        print("4. Display All Profiles")
        print("5. Display Employee Report")  # New option for report
        print("6. Manage Salary (Owner Only)")
        print("7. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            sms.add_employee()
        elif choice == '2':
            sms.display_profile()
        elif choice == '3':
            sms.delete_employee()
        elif choice == '4':
            sms.display_all_profiles()
        elif choice == '5':
            sms.display_report()  # Call the new report method
        elif choice == '6':
            sms.manage_salary()
        elif choice == '7':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")