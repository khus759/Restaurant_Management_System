from Src.Messages.staff import (
    invalid_credentials,
    employee_added,
    employee_not_found,
    employee_deleted,
    no_employees_found,
    display_profile,
    display_all_profiles,
    profile_updated,
    welcome_message,
    exit_message
)
from Src.Staff_Management.utils import load_data, save_data, users_file, employee_file
from Src.Staff_Management.employee import Employee
from Src.Utility.validation import validate_date_of_birth



class StaffManagementSystem:
    def validate_text(self, field_name):
        while True:
            value = input(f"Enter {field_name}: ").strip().title()
            if all(c.isalpha() or c.isspace() for c in value) and value:
                return value
            print(f"Invalid {field_name}. It must contain only alphabets and spaces.")

    def validate_pincode(self):
        while True:
            pincode = input("Enter pincode: ").strip()
            if pincode.isdigit() and len(pincode) == 6:
                return pincode
            print("Invalid pincode. Please enter a 6-digit number.")

    def validate_salary(self):
        while True:
            salary = input("Enter salary: ").strip()
            if salary.replace('.', '', 1).isdigit():
                return float(salary)
            print("Invalid salary. Please enter a numeric value.")

    def validate_gender(self):
        while True:
            gender = input("Enter gender (Male/Female/Other): ").strip().capitalize()
            if gender in ["Male", "Female", "Other"]:
                return gender
            print("Invalid gender. Please enter 'Male', 'Female', or 'Other'.")

    def add_employee(self):
        user_id = input("Enter User ID: ").strip()

        # Check if user ID exists in user.json
        users = load_data(users_file)
        user = next((u for u in users if u['id'] == user_id), None)
        if not user:
            print("User ID not found. Please try again.")
            return

        # Check if user ID already exists in employee.json
        employees = load_data(employee_file)
        if any(emp['id'] == user_id for emp in employees):
            print("Employee with this User ID already exists.")
            return

        gender = self.validate_gender()

        # Create the Employee object
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

        employee.designation = self.validate_text("designation")
        employee.country = self.validate_text("country")
        employee.state = self.validate_text("state")
        employee.district = self.validate_text("district")
        employee.city_village = self.validate_text("city/village")
        employee.pincode = self.validate_pincode()

        while True:
            joining_date = input("Enter joining date (YYYY-MM-DD): ").strip()
            if validate_date_of_birth(joining_date):
                employee.joining_date = joining_date
                break
            print("Invalid date format. Please use YYYY-MM-DD.")

        employee.salary = self.validate_salary()

        # Add employee to list and save
        employees.append(employee.to_dict())
        save_data(employee_file, employees)
        employee_added()

    def display_profile(self):
        email = input("Enter your email: ").strip()

        employees = load_data(employee_file)
        for emp in employees:
            if emp['email'] == email:
                display_profile(emp)
                return

        employee_not_found()

    def update_profile(self):
        email = input("Enter your email: ").strip()

        employees = load_data(employee_file)
        for emp in employees:
            if emp['email'] == email:
                print("Leave a field blank to keep the current value.")

                emp['name'] = input(f"Enter new name (current: {emp['name']}): ") or emp['name']
                emp['phone'] = input(f"Enter new phone (current: {emp['phone']}): ") or emp['phone']
                emp['designation'] = input(f"Enter new designation (current: {emp['designation']}): ") or emp['designation']
                emp['country'] = input(f"Enter new country (current: {emp['country']}): ") or emp['country']
                emp['state'] = input(f"Enter new state (current: {emp['state']}): ") or emp['state']
                emp['district'] = input(f"Enter new district (current: {emp['district']}): ") or emp['district']
                emp['city_village'] = input(f"Enter new city/village (current: {emp['city_village']}): ") or emp['city_village']
                emp['pincode'] = input(f"Enter new pincode (current: {emp['pincode']}): ") or emp['pincode']
                emp['salary'] = input(f"Enter new salary (current: {emp['salary']}): ") or emp['salary']

                save_data(employee_file, employees)
                profile_updated()
                return

        employee_not_found()

    def delete_employee(self):
        email = input("Enter the email of the employee to delete: ").strip()
        employees = load_data(employee_file)
        updated_employees = [emp for emp in employees if emp['email'] != email]

        if len(employees) == len(updated_employees):
            employee_not_found()
            return

        save_data(employee_file, updated_employees)
        employee_deleted()

    def display_all_profiles(self):
        employees = load_data(employee_file)
        if not employees:
            no_employees_found()
            return

        for i, emp in enumerate(employees, start=1):
            display_all_profiles(emp, i)

    def exit_system(self):
        exit_message()

    def welcome_system(self):
        welcome_message()


