
import logging

log_filename = f"Src\Database\error.log"

logging.basicConfig(
    level=logging.DEBUG,
    filename=log_filename,
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


# # Example log messages
# # logging.debug("This is a debug message.")
# # logging.info("This is an info message.")
# # logging.warning("This is a warning message.")
#logging.error("This is an error message.")
# # logging.critical("This is a critical message.")


