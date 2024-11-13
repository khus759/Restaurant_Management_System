
# salary_management.py

class SalaryManagement:
    @staticmethod
    def manage_salary():
        user = Authentication.authenticate_user()
        if not user or user['role'].lower() != 'owner':
            print("Access denied. Only owners can manage salaries.\n")
            return
        
        employees = EmployeeOperations.load_data(employee_file)
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

        EmployeeOperations.save_data(employee_file, employees)
        print("\nSalary management completed.\n")
