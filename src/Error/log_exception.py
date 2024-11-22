import logging

# Define the log file location
log_filename = r"Src\Database\error.log"

# Configure the logging
logging.basicConfig(
    level=logging.DEBUG,
    filename=log_filename,
    filemode='a',  # Append mode
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

# Example of logging an error when loading data
try:
    # Simulate loading data
    raise FileNotFoundError("Failed to load the required database file.")
except FileNotFoundError as e:
    logging.error("Error occurred while loading data: %s", str(e))
