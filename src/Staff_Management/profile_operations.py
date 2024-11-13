
# profile_operations.py
from Src.staff_management.authentication import Authentication

class ProfileOperations:
    @staticmethod
    def display_profile():
        user = Authentication.authenticate_user()
        if not user:
            return
        
        employees = EmployeeOperations.load_data(employee_file)
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
    
    @staticmethod
    def display_all_profiles():
        employees = EmployeeOperations.load_data(employee_file)
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
