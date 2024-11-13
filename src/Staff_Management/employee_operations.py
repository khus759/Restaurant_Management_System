
# employee_operations.py
import json
from Src.Utility.path_manager import employee_file
from Src.staff_management.employee import Employee
from Src.staff_management.authentication import Authentication

class EmployeeOperations:
    @staticmethod
    def load_data(file_path):
        try:
            with open(file_path, 'r') as f:
                return json.load(f)
        except FileNotFoundError:
            return []
    
    @staticmethod
    def save_data(file_path, data):
        with open(file_path, 'w') as f:
            json.dump(data, f, indent=4)

    @staticmethod
    def add_employee():
        user = Authentication.authenticate_user()
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
        # Prompt for additional information
        employee.designation = input("Enter designation: ").title()
        employee.country = input("Enter country: ").title()
        employee.state = input("Enter state: ")
        employee.district = input("Enter district: ").title()
        employee.city_village = input("Enter city/village: ").title()
        employee.pincode = input("Enter pincode: ")
        employee.joining_date = input("Enter joining date (YYYY-MM-DD): ")
        employee.salary = input("Enter salary: ")

        employees = EmployeeOperations.load_data(employee_file)
        employees.append(employee.to_dict())
        EmployeeOperations.save_data(employee_file, employees)
        print("\nEmployee added successfully.\n")
    
    @staticmethod
    def delete_employee():
        user = Authentication.authenticate_user()
        if not user:
            return
        
        users = EmployeeOperations.load_data(users_file)
        employees = EmployeeOperations.load_data(employee_file)

        users = [u for u in users if u['email'] != user['email']]
        EmployeeOperations.save_data(users_file, users)

        for emp in employees:
            if emp['email'] == user['email']:
                emp['status'] = "inactive"
                emp['resign_date'] = datetime.now().strftime("%Y-%m-%d")
        EmployeeOperations.save_data(employee_file, employees)
        print("\nEmployee deleted successfully.\n")
