import os
import datetime

LOG_FILE = 'src/exception_log.csv'

# File paths
files_to_check = {
    'Users': 'Src/Database/users.json',
    'Reservations': 'Src/Database/reservations.json',
    'Table': 'Src/Database/table.json',
    'Menu': 'Src/Database/menu.json',
    'Order': 'Src/Database/order.json',
    'Bill': 'Src/Database/billing.json',
    'Employee': 'Src/Database/employee.json'
}

# Function to log exceptions to CSV
def log_exception(err_msg):
    current_time = datetime.datetime.now()
    # Check if the log file exists; if not, create it with headers
    if os.path.exists(LOG_FILE):
        with open(LOG_FILE, 'a') as file:
            file.write(f'\n{current_time},{err_msg}')
    else:
        with open(LOG_FILE, 'w') as file:
            file.write('Date,Exception Message\n')
            file.write(f'{current_time},{err_msg}\n')

# Function to check files and handle exceptions
def check_files():
    for file_label, file_path in files_to_check.items():
        try:
            # Attempt to open each file in read mode
            with open(file_path, 'r') as file:
                print(f"{file_label} file is accessible.")
        except Exception as e:
            # Log exception if the file cannot be opened
            error_message = f"Error accessing {file_label} file at '{file_path}': {str(e)}"
            print(error_message)  # Print error for debugging
            log_exception(error_message)

# Run the file check
# check_files()
