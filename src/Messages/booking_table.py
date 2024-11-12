
class BookingHandler():

    def display_no_tables_found(self):
        print("Table data file not found or corrupted. No tables loaded.")

    def display_no_reservations(self):
        print("Reservations file not found or corrupted. Initializing with an empty list.")

    def display_save_error(self, e):
        print(f"Error saving reservations: {e}")

    def display_reservation_success(self, reservation_id):
        print(f"Reservation successful! Booking ID: {reservation_id}")

    def display_no_available_tables(self,seats, date_time):
        print(f"No available tables for {seats} seats at {date_time}.")
        
    def display_no_active_reservation(self):
        print("No active reservation found with the specified ID.")

    def display_reservation_canceled(self, booking_id):
        print(f"Reservation {booking_id} has been canceled.")

    def display_update_success(self, booking_id):
        print(f"Reservation {booking_id} has been updated.")

    def display_no_reservations_found(self):
        print("No reservations found.")

    def display_all_reservations(self, reservations):
        print("All Reservations:")
        for reservation in reservations:
            print(f"Booking ID: {reservation.reservation_id}")
            print(f"-" * 40)
            print(f"Name: {reservation.name}")
            print(f"Phone: {reservation.phone}")
            print(f"Date and Time: {reservation.date_time}")
            print(f"Seats: {reservation.seats}")
            print(f"Table ID: {reservation.table_id}")
            print(f"Status: {reservation.status}")
            print("=" * 40)

    def display_reservation_found(self, reservation):
        print("=" * 40)
        print("Reservation found:")
        print(f"Booking ID: {reservation.reservation_id}")
        print(f"-" * 40)
        print(f"Name: {reservation.name}")
        print(f"Phone: {reservation.phone}")
        print(f"Date and Time: {reservation.date_time}")
        print(f"Seats: {reservation.seats}")
        print(f"Table ID: {reservation.table_id}")
        print(f"Status: {reservation.status}")
        print("=" * 40)

    def display_no_reservation_found(self):
        print("No reservation found with the specified booking ID.")

    def display_reservations_on_date(self, date_input, reservations_on_date):
        if reservations_on_date:
            print(f"\nReservations on {date_input}:")
            for res in reservations_on_date:
                print(f"Name: {res['name']}, Phone: {res['phone']}, Time: {res['time']}, Table: {res['table_id']}, Status: {res['status']}")
        else:
            print(f"No reservations found on {date_input}.")
    
    def display_canceled_reservations(self, canceled_reservations):
        if canceled_reservations:
            print("\nCanceled Reservations:")
            for res in canceled_reservations:
                print(f"Date: {res['date']}, Name: {res['name']}, Phone: {res['phone']}, Time: {res['time']}, Table: {res['table_id']}")
        else:
            print("No canceled reservations found for the specified date or month.")
    
