import logging

log_filename = f"Src\Database\error.txt"

logging.basicConfig(
    level=logging.DEBUG,
    filename=log_filename,
    filemode='a',
    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
    datefmt='%Y-%m-%d %H:%M:%S'
)


