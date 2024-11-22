import json
from datetime import datetime
from Src.Staff_Management.utils import load_data, save_data, employee_file
from Src.Utility.validation import get_valid_float_input, get_valid_int_input
from Src.Messages.staff import *
from Src.Error.log_exception import logging


class SalaryManagement:
    def __init__(self):
        self.employees = load_data(employee_file)
        
    def pay_salary(self):
        """Method to process and record an employee's salary payment."""
        user_id = input("Enter Employee ID to pay salary: ").strip()
        emp = next((e for e in self.employees if e['id'] == user_id), None)
        
        if emp:
            if emp.get('status') == 'unactive':
                inactive_employee()
                return
            
            # Calculate the daily salary based on monthly salary and days worked
            try:
                days_worked = get_valid_int_input(f"Enter number of days {emp['name']} worked in the past 30 days: ")
                total_days_in_month = 30
                daily_salary = float(emp['salary']) / total_days_in_month
                salary_for_days_worked = daily_salary * days_worked
            except ValueError:
                logging.exception("exception details")
                print("Invalid salary format.")
                return

            # Get additional details such as bonus and calculate total payment
            bonus = get_valid_int_input(f"Enter the bonus amount for {emp['name']} (or 0 if none): ")
            reduction_days = total_days_in_month - days_worked
            total_payment = salary_for_days_worked + bonus
            payment_date = datetime.now().strftime("%Y-%m-%d")
            
            # Create the payment record
            payment_record = {
                'date': payment_date,
                'amount': total_payment,
                'bonus': bonus,
                'reduction_days': reduction_days
            }

            # Append payment record to the employee's salary payment history
            emp['salary_payment_history'] = emp.get('salary_payment_history', [])
            emp['salary_payment_history'].append(payment_record)

            # Save updated employee data back to the file
            save_data(employee_file, self.employees)

            # Print confirmation message
            salary_paid_success(emp['name'], payment_date, total_payment)
        else:
            employee_not_found()
    
    def show_salary_history(self):
        """Method to display the salary payment history of an employee from their joining date."""
        user_id = input("Enter Employee ID to view salary history: ").strip()
        emp = next((e for e in self.employees if e['id'] == user_id), None)
        
        if emp:
            print(f"\nSalary Payment History for {emp['name']} (ID: {emp['id']}):")
            if 'salary_payment_history' in emp and emp['salary_payment_history']:
                for record in emp['salary_payment_history']:
                    print(f"Date: {record['date']}, Amount: {record['amount']}, "
                          f"Bonus: {record['bonus']}, Days Reduced: {record['reduction_days']}")
            else:
                print("No salary payment history found.")
        else:
            employee_not_found()

