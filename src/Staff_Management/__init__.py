# main.py
from Src.staff_management.employee_operations import EmployeeOperations
from Src.staff_management.profile_operations import ProfileOperations
from Src.staff_management.report_operations import ReportOperations
from Src.staff_management.salary_management import SalaryManagement

def main():
    while True:
        print("\n=== Staff Management System ===")
        print("1. Add Employee")
        print("2. Delete Employee")
        print("3. Display Profile")
        print("4. Display All Profiles")
        print("5. Display Report")
        print("6. Manage Salary")
        print("7. Exit")

        choice = input("Choose an option: ")
        if choice == '1':
            EmployeeOperations.add_employee()
        elif choice == '2':
            EmployeeOperations.delete_employee()
        elif choice == '3':
            ProfileOperations.display_profile()
        elif choice == '4':
            ProfileOperations.display_all_profiles()
        elif choice == '5':
            ReportOperations.display_report()
        elif choice == '6':
            SalaryManagement.manage_salary()
        elif choice == '7':
            print("Exiting Staff Management System.")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
