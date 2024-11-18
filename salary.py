import json
from datetime import datetime

# Define global file paths
USER_FILE_PATH = 'user.json'
EMPLOYEE_FILE_PATH = 'employee.json'

class Employee:
    def __init__(self, id, name, email, password, phone, date_of_birth, role, gender, **kwargs):
        self.id = id
        self.name = name
        self.email = email
        self.password = password
        self.phone = phone
        self.date_of_birth = date_of_birth
        self.role = role
        self.gender = gender
        self.designation = kwargs.get("designation", "")
        self.country = kwargs.get("country", "")
        self.state = kwargs.get("state", "")
        self.district = kwargs.get("district", "")
        self.city_village = kwargs.get("city_village", "")
        self.pincode = kwargs.get("pincode", "")
        self.joining_date = kwargs.get("joining_date", "")
        self.salary = kwargs.get("salary", "")
        self.status = "active"
        self.resign_date = None
        self.salary_payment_history = []

    def to_dict(self):
        return self.__dict__

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

    def add_employee(self):
        user_id = input("Enter User ID: ").strip()
        
        users = self.load_data(USER_FILE_PATH)
        user = next((u for u in users if u['id'] == user_id), None)
        if not user:
            print("User ID not found. Please try again.")
            return

        employees = self.load_data(EMPLOYEE_FILE_PATH)
        if any(emp['id'] == user_id for emp in employees):
            print("Employee with this User ID already exists.")
            return

        while True:
            gender = input("Enter gender (Male/Female/Other): ").strip().capitalize()
            if gender in ["Male", "Female", "Other"]:
                break
            else:
                print("Invalid input. Please enter 'Male', 'Female', or 'Other'.")

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

        employees.append(employee.to_dict())
        self.save_data(EMPLOYEE_FILE_PATH, employees)
        print("Employee added successfully.")

    def display_profile(self):
        user_id = input("Enter User ID: ").strip()
        employees = self.load_data(EMPLOYEE_FILE_PATH)
        for emp in employees:
            if emp['id'] == user_id:
                print("\n=== Employee Profile ===")
                print("--------------------------------")
                print(f"   Name           : {emp.get('name', 'N/A')}")
                print(f"   Gender         : {emp.get('gender', 'N/A')}")
                print(f"   Date of Birth  : {emp.get('date_of_birth', 'N/A')}")
                print(f"   Email          : {emp.get('email', 'N/A')}")
                print(f"   Phone          : {emp.get('phone', 'N/A')}")
                print(f"   Role           : {emp.get('role', 'N/A')}")
                print(f"   Designation    : {emp.get('designation', 'N/A')}")
                print(f"   Joining Date   : {emp.get('joining_date', 'N/A')}")
                print(f"   Salary         : {emp.get('salary', 'N/A')}")
                print(f"   Status         : {emp.get('status', 'N/A')}")
                if emp.get('status', 'active') == 'unactive':
                    print(f"   Resign Date    : {emp.get('resign_date', 'N/A')}")
                print("\n   Salary Payment History")
                print("   --------------------")
                if emp.get('salary_payment_history'):
                    for payment in emp['salary_payment_history']:
                        print(f"   Paid on: {payment['date']}, Amount: {payment['amount']}, "
                              f"Bonus: {payment.get('bonus', 0)}, Reduction Days: {payment.get('reduction_days', 0)}")
                else:
                    print("   No salary paid yet.")
                return
        print("Employee not found.")

    def delete_employee(self):
        user_id = input("Enter User ID: ").strip()
        employees = self.load_data(EMPLOYEE_FILE_PATH)
        for emp in employees:
            if emp['id'] == user_id:
                emp['status'] = "unactive"
                emp['resign_date'] = datetime.now().strftime("%Y-%m-%d")
                self.save_data(EMPLOYEE_FILE_PATH, employees)
                print("Employee marked as inactive.")
                return
        print("Employee not found.")

    def pay_salary(self):
        user_id = input("Enter Employee ID to pay salary: ").strip()
        employees = self.load_data(EMPLOYEE_FILE_PATH)
        emp = next((e for e in employees if e['id'] == user_id), None)
        
        if emp:
            days_worked = int(input(f"Enter number of days {emp['name']} worked in the past 30 days: ").strip())
            total_days_in_month = 30
            daily_salary = float(emp['salary']) / total_days_in_month
            salary_for_days_worked = daily_salary * days_worked

            bonus = float(input(f"Enter the bonus amount for {emp['name']} (or 0 if none): ").strip())
            reduction_days = total_days_in_month - days_worked
            total_payment = salary_for_days_worked + bonus
            payment_date = datetime.now().strftime("%Y-%m-%d")
            
            # Ensure all required fields are in the payment record
            payment_record = {
                'date': payment_date,
                'amount': total_payment,
                'bonus': bonus,  # Ensure bonus is added here
                'reduction_days': reduction_days  # Ensure reduction_days is added here
            }

            # Append payment record to the employee's salary payment history
            emp['salary_payment_history'].append(payment_record)

            self.save_data(EMPLOYEE_FILE_PATH, employees)
            print(f"Salary paid to {emp['name']} successfully on {payment_date}. Total: {total_payment}.")
        else:
            print("Employee not found.")

    def display_all_profiles(self):
        employees = self.load_data(EMPLOYEE_FILE_PATH)
        if not employees:
            print("No employees found.")
            return
        
        print("\n=== All Employee Profiles ===")
        for i, emp in enumerate(employees, start=1):
            print("\n--------------------------------")
            print(f"       Employee {i}")
            print("--------------------------------")
            print(f"   Name           : {emp.get('name', 'N/A')}")
            print(f"   Gender         : {emp.get('gender', 'N/A')}")
            print(f"   Date of Birth  : {emp.get('date_of_birth', 'N/A')}")
            print(f"   Role           : {emp.get('role', 'N/A')}")
            print(f"   Designation    : {emp.get('designation', 'N/A')}")
            print(f"   Joining Date   : {emp.get('joining_date', 'N/A')}")
            print(f"   Salary         : {emp.get('salary', 'N/A')}")
            print(f"   Status         : {emp.get('status', 'N/A')}")
            if emp.get('status', 'active') == 'unactive':
                print(f"   Resign Date    : {emp.get('resign_date', 'N/A')}")
            
            print("\n   Salary Payment History")
            print("   --------------------")
            if emp.get('salary_payment_history'):
                for payment in emp['salary_payment_history']:
                    print(f"   Paid on: {payment['date']}, Amount: {payment['amount']}, "
                          f"Bonus: {payment.get('bonus', 0)}, Reduction Days: {payment.get('reduction_days', 0)}")
            else:
                print("   No salary paid yet.")

# Main function to interact with the system
if __name__ == "__main__":
    sms = StaffManagementSystem()
    
    while True:
        print("\n=== Staff Management System ===")
        print("1. Add Employee")
        print("2. Display Employee Profile")
        print("3. Delete Employee")
        print("4. Pay Salary")
        print("5. Display All Employee Profiles")
        print("6. Exit")
        choice = input("Enter your choice: ").strip()
        
        if choice == '1':
            sms.add_employee()
        elif choice == '2':
            sms.display_profile()
        elif choice == '3':
            sms.delete_employee()
        elif choice == '4':
            sms.pay_salary()
        elif choice == '5':
            sms.display_all_profiles()
        elif choice == '6':
            break
        else:
            print("Invalid choice. Please try again.")
