

class ReportOperations:
    @staticmethod
    def display_report():
        employees = EmployeeOperations.load_data(employee_file)
        if not employees:
            print("No employees found.\n")
            return

        print("\n" + "="*50)
        print("Employee Report".center(50))
        print("="*50)
        print("-" * 130)
        print(f"{'S.No':<5} {'ID':<10} {'Name':<30} {'Phone':<18} {'Designation':<20} {'Status':<10} {'Joining Date':<15} {'Resigning Date':<15}")
        print("-" * 130)
        for idx, emp in enumerate(employees, start=1):
            print(f"{str(idx):<5} {str(emp.get('id', '')):<10} {str(emp.get('name', '')):<30} {str(emp.get('phone', '')):<15} {str(emp.get('designation', '')):<20} {str(emp.get('status', '')):<10} {str(emp.get('joining_date', '')):<15} {str(emp.get('resign_date', '')):<15}")
        print("="*130 + "\n")
