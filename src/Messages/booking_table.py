from Src.Utility.color import Colors
class BookingHandler:
    def __init__(self):
        self.color = Colors()
    
    def display_no_tables_found(self):
        print(f"{Colors.RED}Table data file not found or corrupted. No tables loaded.{Colors.RESET}")

    def display_no_reservations(self):
        print(f"{Colors.RED}Reservations file not found or corrupted. Initializing with an empty list.{Colors.RESET}")

    def display_save_error(self, e):
        print(f"{Colors.RED}Error saving reservations: {e}{Colors.RESET}")

    def display_reservation_success(self, reservation_id):
        print(f"{Colors.GREEN}Reservation successful! Booking ID: {reservation_id}{Colors.RESET}")

    def display_no_available_tables(self, seats, date_time):
        print(f"{Colors.YELLOW}No available tables for {seats} seats at {date_time}.{Colors.RESET}")
        
    def display_no_active_reservation(self):
        print(f"{Colors.RED}No active reservation found with the specified ID.{Colors.RESET}")

    def display_reservation_canceled(self, booking_id):
        print(f"{Colors.GREEN}Reservation {booking_id} has been canceled.{Colors.RESET}")

    def display_update_success(self, booking_id):
        print(f"{Colors.GREEN}Reservation {booking_id} has been updated.{Colors.RESET}")

    def display_no_reservations_found(self):
        print(f"{Colors.YELLOW}No reservations found.{Colors.RESET}")

    def display_all_reservations(self, reservations):
        print(f"{Colors.BLUE}All Reservations:{Colors.RESET}")
        for reservation in reservations:
            print(f"{Colors.BRIGHT_MAGENTA}={Colors.RESET}" * 40)
            print(f"Booking ID: {reservation.reservation_id}")
            print(f"Name: {reservation.name}")
            print(f"Phone: {reservation.phone}")
            print(f"Date and Time: {reservation.date_time}")
            print(f"Seats: {reservation.seats}")
            print(f"Table ID: {reservation.table_id}")
            print(f"Status: {reservation.status}")
            print(f"{Colors.BRIGHT_MAGENTA}={Colors.RESET}" * 40)
        
    def display_reservation_found(self, reservation):
        print(f"{Colors.BLUE}Reservation found:{Colors.RESET}")
        print(f"{Colors.BRIGHT_MAGENTA}={Colors.RESET}" * 40)
        print(f"{Colors.YELLOW}Booking ID: {reservation.reservation_id}{Colors.RESET}")
        print(f"Name: {reservation.name}")
        print(f"Phone: {reservation.phone}")
        print(f"Date and Time: {reservation.date_time}")
        print(f"Seats: {reservation.seats}")
        print(f"Table ID: {reservation.table_id}")
        print(f"Status: {reservation.status}")
        print(f"{Colors.BG_MAGENTA}={Colors.RESET}" * 40)

    def display_no_reservation_found(self):
        print(f"{Colors.RED}No reservation found with the specified booking ID.{Colors.RESET}")

    def display_reservations_on_date(self, date_input, reservations_on_date):
        if reservations_on_date:
            print(f"{Colors.BLUE}Reservations on {date_input}:{Colors.RESET}")
            for res in reservations_on_date:
                print(f"Name: {res['name']}, Phone: {res['phone']}, Time: {res['time']}, Table: {res['table_id']}, Status: {res['status']}")
        else:
            print(f"{Colors.YELLOW}No reservations found on {date_input}.{Colors.RESET}")
    
    def display_canceled_reservations(self, canceled_reservations):
        if canceled_reservations:
            print(f"{Colors.BLUE}Canceled Reservations:{Colors.RESET}")
            for res in canceled_reservations:
                print(f"Date: {res['date']}, Name: {res['name']}, Phone: {res['phone']}, Time: {res['time']}, Table: {res['table_id']}")
        else:
            print(f"{Colors.YELLOW}No canceled reservations found for the specified date or month.{Colors.RESET}")
    
    def welcome_message(self):
        print(f"{Colors.LIGHT_CORAL} 😀 Welcome to the Booking Management System! Please follow the prompts to continue.😜{Colors.RESET}")

    def exit_message(self):
        print(f"{Colors.LIGHT_VIOLET} 😀 Thank you for using the Booking Management System. Goodbye!{Colors.RESET}")
 