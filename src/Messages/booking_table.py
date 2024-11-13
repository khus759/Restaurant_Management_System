class BookingHandler:
    
    RED = "\033[91m"
    GREEN = "\033[92m"
    YELLOW = "\033[93m"
    BLUE = "\033[94m"
    RESET = "\033[0m"

    def display_no_tables_found(self):
        print(f"{self.RED}Table data file not found or corrupted. No tables loaded.{self.RESET}")

    def display_no_reservations(self):
        print(f"{self.RED}Reservations file not found or corrupted. Initializing with an empty list.{self.RESET}")

    def display_save_error(self, e):
        print(f"{self.RED}Error saving reservations: {e}{self.RESET}")

    def display_reservation_success(self, reservation_id):
        print(f"{self.GREEN}Reservation successful! Booking ID: {reservation_id}{self.RESET}")

    def display_no_available_tables(self, seats, date_time):
        print(f"{self.YELLOW}No available tables for {seats} seats at {date_time}.{self.RESET}")
        
    def display_no_active_reservation(self):
        print(f"{self.RED}No active reservation found with the specified ID.{self.RESET}")

    def display_reservation_canceled(self, booking_id):
        print(f"{self.GREEN}Reservation {booking_id} has been canceled.{self.RESET}")

    def display_update_success(self, booking_id):
        print(f"{self.GREEN}Reservation {booking_id} has been updated.{self.RESET}")

    def display_no_reservations_found(self):
        print(f"{self.YELLOW}No reservations found.{self.RESET}")

    def display_all_reservations(self, reservations):
        print(f"{self.BLUE}All Reservations:{self.RESET}")
        for reservation in reservations:
            print("=" * 40)
            print(f"Booking ID: {reservation.reservation_id}")
            print(f"Name: {reservation.name}")
            print(f"Phone: {reservation.phone}")
            print(f"Date and Time: {reservation.date_time}")
            print(f"Seats: {reservation.seats}")
            print(f"Table ID: {reservation.table_id}")
            print(f"Status: {reservation.status}")
            print("=" * 40)

    def display_reservation_found(self, reservation):
        print(f"{self.BLUE}Reservation found:{self.RESET}")
        print("=" * 40)
        print(f"Booking ID: {reservation.reservation_id}")
        print(f"Name: {reservation.name}")
        print(f"Phone: {reservation.phone}")
        print(f"Date and Time: {reservation.date_time}")
        print(f"Seats: {reservation.seats}")
        print(f"Table ID: {reservation.table_id}")
        print(f"Status: {reservation.status}")
        print("=" * 40)

    def display_no_reservation_found(self):
        print(f"{self.RED}No reservation found with the specified booking ID.{self.RESET}")

    def display_reservations_on_date(self, date_input, reservations_on_date):
        if reservations_on_date:
            print(f"{self.BLUE}Reservations on {date_input}:{self.RESET}")
            for res in reservations_on_date:
                print(f"Name: {res['name']}, Phone: {res['phone']}, Time: {res['time']}, Table: {res['table_id']}, Status: {res['status']}")
        else:
            print(f"{self.YELLOW}No reservations found on {date_input}.{self.RESET}")
    
    def display_canceled_reservations(self, canceled_reservations):
        if canceled_reservations:
            print(f"{self.BLUE}Canceled Reservations:{self.RESET}")
            for res in canceled_reservations:
                print(f"Date: {res['date']}, Name: {res['name']}, Phone: {res['phone']}, Time: {res['time']}, Table: {res['table_id']}")
        else:
            print(f"{self.YELLOW}No canceled reservations found for the specified date or month.{self.RESET}")
