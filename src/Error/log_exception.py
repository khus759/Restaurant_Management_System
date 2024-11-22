<<<<<<< HEAD
import logging

# Define the log file location
log_filename = r"Src\Database\error.log"

# Configure the logging
logging.basicConfig(
    level=logging.DEBUG,
    filename=log_filename,
    filemode='a',  # Append mode
=======

import logging

log_filename = f"Src\Database\error.log"

logging.basicConfig(
    level=logging.DEBUG,
    filename=log_filename,
    filemode='a',
>>>>>>> 597947d82c3e954d75a4aeac3fd5bef5c55f8eab
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)

<<<<<<< HEAD
# Example of logging an error when loading data
try:
    # Simulate loading data
    raise FileNotFoundError("Failed to load the required database file.")
except FileNotFoundError as e:
    logging.error("Error occurred while loading data: %s", str(e))
=======

# # Example log messages
# # logging.debug("This is a debug message.")
# # logging.info("This is an info message.")
# # logging.warning("This is a warning message.")
#logging.error("This is an error message.")
# # logging.critical("This is a critical message.")


>>>>>>> 597947d82c3e954d75a4aeac3fd5bef5c55f8eab
