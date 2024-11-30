import re

def parse_error_logs():
    # Regular expression to match the log pattern
    log_pattern = re.compile(
        r"(?P<time>\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}) - .+ - ERROR - .+\n"
        r"Traceback \(most recent call last\):\n"
        r".+File \"(?P<filename>[^\"]+)\", line (?P<line>\d+), in (?P<function>\w+).*\n"
        r"(?P<error_type>[^\:]+): (?P<error_msg>.+)"
    )

    try:
        # Open the file and parse its contents
        with open("Src/Database/error.log", "r") as file:
            log_data = file.read()
        
        # Find all matches using the regex
        matches = log_pattern.finditer(log_data)
        
        # Print formatted output
        print("\nParsed Log Details:\n")
        for match in matches:
            print("-" * 140)
            print(f"Time       : {match.group('time')}")
            print(f"File       : {match.group('filename')}")
            print(f"Line       : {match.group('line')}")
            print(f"Function   : {match.group('function')}")
            print(f"Error Type : {match.group('error_type')}")
            print(f"Error Msg  : {match.group('error_msg')}")
    except FileNotFoundError:
        print(f"The file {"Src/Database/error.log"} does not exist.")
    except Exception as e:
        print(f"An error occurred: {e}")
