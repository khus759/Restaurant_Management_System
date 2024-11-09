from datetime import datetime
def validate_name(name):
    if not name.strip():
        return "Name cannot be blank."
    if any(char.isdigit() for char in name):
        return "Name cannot contain numbers."
    if any(not char.isalpha() and not char.isspace() for char in name):
        return "Name cannot contain special characters."
    return None


def validate_password(password):
    if not password.strip():
        return "Password cannot be blank."
    if len(password) < 6:
        return "Password must be at least 6 characters long."
    return None

def validate_role(role):
    role = role.upper()
    if not role.strip():
        return "Role cannot be blank."
    if role                                                                                                                                                        not in ['OWNER', 'STAFF']:
        return "Role must be either 'Owner' or 'Staff'."
    return None

def validate_quantity( quantity):
    if not quantity.strip():
        return "Quantity cannot be blank."
    if not quantity.isdigit():
        return "Quantity cannot contain special characters or letters. Only numbers are allowed."
    return None

def validate_price(price):
    if not price.strip():
        return "Price cannot be blank."
    if any(char.isalpha() for char in price):
        return "Price cannot contain letters."
    if any(not char.isdigit() and char != '.' for char in price):
        return "Price cannot contain special characters."
    try:
        float(price)
    except ValueError:
        return "Price must be a valid number."
    return None

# def validate_item_id(item_id):
#     if not item_id.strip():
#         return "Item ID cannot be blank."
#     if any(char.isalpha() for char in item_id):
#         return "Item ID cannot contain letters."
#     if any(not char.isdigit() for char in item_id):
#         return "Item ID must be numeric."
#     return None  


def validate_phone_number(phone_number):
    """Validate phone number (must be exactly 10 digits)."""
    if not phone_number.strip():
        return "Phone number cannot be blank."
    if not phone_number.isdigit():
        return "Phone number can only contain digits."
    if len(phone_number) != 10:
        return "Phone number must be exactly 10 digits."
    return None

def validate_email( email):
    if not email.strip():
        return "Email cannot be blank."
    
    if "@" not in email or "." not in email:
        return "Invalid email format."
    # Check position of "@" and "."
    at_index = email.index("@")
    dot_index = email.rfind(".")
    # Ensure "@" comes before "." and neither are at the start or end
    if at_index == 0 or dot_index == len(email) - 1 or at_index > dot_index:
        return "Invalid email format."
    # Ensure at least one character between "@" and "."
    if dot_index - at_index < 2:
        return "Invalid email format."
    return None

def validate_date_of_birth(dob):
        try:
            dob_date = datetime.strptime(dob, "%Y-%m-%d")
            age = (datetime.now() - dob_date).days // 365
            if dob_date >= datetime.now():
                return "Date of birth cannot be in the future."
            if age < 18:
                return "Minimum age requirement is 18 years." 
            if age > 60:
                return "Maximum age requirement is 60 years."
            return None
        except ValueError:
            return "Invalid date format. Please enter as YYYY-MM-DD."
        
# table_booking

OPENING_TIME = 10  # Restaurant opening hour (10 AM)
CLOSING_TIME = 22  # Restaurant closing hour (10 PM)
HOLIDAYS = ['Tuesday'] 

def parse_date_time(date_time_str):
    """Parse date-time in the 'YYYY-MM-DD HH:MM AM/PM' format."""
    try:
        return datetime.strptime(date_time_str, '%Y-%m-%d %I:%M %p')
    except ValueError:
        return None

def validate_booking_date_time(date_time_str):
    """Validate the reservation date and time."""
    reservation_time = parse_date_time(date_time_str)
    if not reservation_time:
        return "Invalid date-time format. Please use 'YYYY-MM-DD HH:MM AM/PM'."

    current_time = datetime.now()
    if reservation_time <= current_time:
        return "Reservation time must be in the future."

    if reservation_time.strftime('%A') in HOLIDAYS:
        return "Restaurant is closed on the selected day."

    if not (OPENING_TIME <= reservation_time.hour < CLOSING_TIME):
        return "Reservation time must be between 10 AM and 10 PM."
    
    return None

def validate_seats(seats):
    try:
        seats = int(seats)
        if seats <= 0:
            return "Seats must be a positive number."  # Ensures only positive numbers are valid
        return seats
    except ValueError:
        return "Invalid input. Please enter a valid number of seats."

def validate_booking_id(booking_id):
    """Validate that the booking ID is not blank."""
    if not booking_id.strip():  # Check if the string is empty or just whitespace
        return "Booking ID cannot be blank."
    return None  # Return None if the input is valid
