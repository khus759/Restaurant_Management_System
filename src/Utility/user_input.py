def get_valid_input(prompt, validation_func):
    while True:
        value = input(prompt).strip()
        error_message = validation_func(value)
        if isinstance(error_message, str):  # Check if error_message is a string (meaning invalid input)
            print(error_message)
        else:
            return value
