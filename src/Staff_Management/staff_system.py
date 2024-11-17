

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
from Src.Utility.user_input import get_valid_input

class StaffManagementSystem:
    def authenticate_user(self):
        email = input("Enter email: ").strip()
        password = input("Enter password: ").strip()
        users = load_data(users_file)
        for user in users:
            if user['email'] == email and user['password'] == password:
                return user
        invalid_credentials()
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
        employee.joining_date = get_valid_input("Enter joining date (YYYY-MM-DD): ", validate_date_of_birth)
        employee.salary = input("Enter salary: ")

        employees = load_data(employee_file)
        employees.append(employee.to_dict())
        save_data(employee_file, employees)
        employee_added()

    def display_profile(self):
        user = self.authenticate_user()
        if not user:
            return

        employees = load_data(employee_file)
        for emp in employees:
            if emp['email'] == user['email']:
                display_profile(emp)
                return

        employee_not_found()

    def update_profile(self):
        user = self.authenticate_user()
        if not user:
            return

        employees = load_data(employee_file)
        for emp in employees:
            if emp['email'] == user['email']:
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

                # Save updated employee list back to file
                save_data(employee_file, employees)
                profile_updated()
                return

        employee_not_found()

    def delete_employee(self):
        email = input("Enter the email of the employee to delete: ")
        employees = load_data(employee_file)
        employees = [emp for emp in employees if emp['email'] != email]
        save_data(employee_file, employees)
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