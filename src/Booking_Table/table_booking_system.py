import json
import uuid
from Src.Booking_Table.table import Table
from Src.Booking_Table.reservation_model import Reservation
from Src.Utility.user_input import get_valid_input
from Src.Utility.validation import (validate_name, validate_phone_number, validate_booking_date_time, parse_date_time, validate_seats, validate_booking_id)


class TableBookingSystem:
    def __init__(self, reservations_file='Src/Database/reservations.json', table_file='Src/Database/table.json'):
        self.reservations_file = reservations_file
        self.table_file = table_file
        self.load_tables()
        self.load_reservations()

    def load_tables(self):
        """Load tables from the JSON file."""
        try:
            with open(self.table_file, 'r') as file:
                self.tables = [Table(**table) for table in json.load(file)['tables']]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Table data file not found or corrupted. No tables loaded.")
            self.tables = []

    def load_reservations(self):
        """Load reservations from the file."""
        try:
            with open(self.reservations_file, 'r') as file:
                self.reservations = [Reservation(**res) for res in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            print("Reservations file not found or corrupted. Initializing with an empty list.")
            self.reservations = []

    def save_reservations(self):
        """Save reservations to the file."""
        try:
            with open(self.reservations_file, 'w') as file:
                json.dump([res.__dict__ for res in self.reservations], file, indent=4)
        except Exception as e:
            print(f"Error saving reservations: {e}")

    def find_available_table(self, seats, date_time):
        """Find an available table for the given number of seats and time."""
        available_tables = [
            table for table in self.tables
            if table.seats == seats and not any(
                reservation.table_id == table.table_id and reservation.date_time == date_time and reservation.status == 'Reserved'
                for reservation in self.reservations
            )
        ]
        return available_tables

    def reserve_table(self):
        """Reserve a table if available."""
        while True:
            name = get_valid_input("Enter your name: ", validate_name)
            phone = get_valid_input("Enter your phone number: ", validate_phone_number)
            date_time = get_valid_input("Enter reservation date and time (YYYY-MM-DD HH:MM AM/PM): ", validate_booking_date_time)
            
            seats = get_valid_input("Enter number of seats required: ", validate_seats)
            seats = int(seats)  # Convert validated input to integer

            # Find available tables for the specified seat count and date-time
            available_tables = self.find_available_table(seats, date_time)
            
            if not available_tables:
                print(f"No available tables for {seats} seats at the specified time.")
                return

            # Proceed with the reservation for the first available table
            table = available_tables[0]
            phone_prefix = phone[:4]
            reserve_id = f"{phone_prefix}{str(uuid.uuid4())[:4]}"
            
            reservation = Reservation(
                reservation_id=reserve_id,
                name=name,
                phone=phone,
                date_time=date_time,
                seats=seats,
                table_id=table.table_id
            )
            self.reservations.append(reservation)
            self.save_reservations()
            print(f"Reservation successful! Booking ID: {reservation.reservation_id}")
            return

    def cancel_reservation(self):
        """Cancel a reservation based on booking ID."""
        while True:
            booking_id = get_valid_input("Enter the booking ID to cancel: ",validate_booking_id)
            for reservation in self.reservations:
                if reservation.reservation_id == booking_id and reservation.status == 'Reserved':
                    reservation.status = 'Canceled'
                    self.save_reservations()
                    print(f"Reservation {booking_id} has been canceled.")
                    return
            print("No active reservation found with the specified ID.")

    def update_reservation(self):
        """Update the reservation time for an existing booking."""
        while True:
            booking_id = get_valid_input("Enter the booking ID to update: ",validate_booking_id)
            new_date_time = get_valid_input("Enter new reservation date and time (YYYY-MM-DD HH:MM AM/PM): ", validate_booking_date_time)
            
            for reservation in self.reservations:
                if reservation.reservation_id == booking_id and reservation.status == 'Reserved':
                    available_tables = self.find_available_table(reservation.seats, new_date_time)
                    if not available_tables:
                        print("No available table for the specified time.")
                        return

                    reservation.date_time = new_date_time
                    reservation.table_id = available_tables[0].table_id
                    self.save_reservations()
                    print(f"Reservation {booking_id} has been updated.")
                    return
            print("No active reservation found with the specified ID.")

    def view_availability(self):
        """Check if tables are available for a specific date, time, and group size."""
        while True:
            date_time = get_valid_input("Enter the date and time to check availability (YYYY-MM-DD HH:MM AM/PM): ", validate_booking_date_time)
            seats = int(get_valid_input("Enter number of seats required: ", validate_seats))

            available_tables = self.find_available_table(seats, date_time)
            if available_tables:
                print(f"Available tables for {seats} seats at {date_time}:")
                for table in available_tables:
                    print(table)
            else:
                print(f"No available tables for {seats} seats at {date_time}.")
