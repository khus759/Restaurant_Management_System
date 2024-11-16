
import json
import uuid
from Src.Booking_Table.table import Table
from Src.Booking_Table.reservation_model import Reservation
from Src.Utility.user_input import get_valid_input
from Src.Utility.validation import (validate_name, validate_phone_number, validate_booking_date_time,
                                    parse_date_time, validate_seats, validate_booking_id)
from Src.Utility.path_manager import reservations_file, table_file
from Src.Messages.booking_table import BookingHandler

class TableBookingSystem:
    def __init__(self):
        self.reservations_file = reservations_file
        self.table_file = table_file
        self.load_tables()
        self.load_reservations()
        self.messages = BookingHandler()

    def load_tables(self):
        try:
            with open(self.table_file, 'r') as file:
                self.tables = [Table(**table) for table in json.load(file)['tables']]
        except (FileNotFoundError, json.JSONDecodeError):
            self.messages.display_no_tables_found()
            self.tables = []

    def load_reservations(self):
        try:
            with open(self.reservations_file, 'r') as file:
                self.reservations = [Reservation(**res) for res in json.load(file)]
        except (FileNotFoundError, json.JSONDecodeError):
            self.messages.display_no_reservations()
            self.reservations = []

    def save_reservations(self):
        try:
            with open(self.reservations_file, 'w') as file:
                json.dump([res.__dict__ for res in self.reservations], file, indent=4)
        except Exception as e:
            self.messages.display_save_error(e)

    def find_available_table(self, seats, date_time):
        available_tables = [
            table for table in self.tables
            if table.seats == seats and not any(
                reservation.table_id == table.table_id and reservation.date_time == date_time and reservation.status == 'Reserved'
                for reservation in self.reservations
            )
        ]
        return available_tables

    def reserve_table(self):
        while True:
            name = get_valid_input("Enter your name: ", validate_name)
            phone = get_valid_input("Enter your phone number: ", validate_phone_number)
            date_time = get_valid_input("Enter reservation date and time (YYYY-MM-DD HH:MM AM/PM): ", validate_booking_date_time)
            seats = int(get_valid_input("Enter number of seats required: ", validate_seats))

            available_tables = self.find_available_table(seats, date_time)
            
            if not available_tables:
                self.messages.display_no_available_tables(seats, date_time)
                return

            table = available_tables[0]
            reserve_id = f"{phone[:4]}{str(uuid.uuid4())[:4]}"
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
            self.messages.display_reservation_success(reservation.reservation_id)
            
            continue_prompt = input("Would you like to make another reservation? (yes/no): ").strip().lower()
            if continue_prompt != 'yes':
                break

    def cancel_reservation(self):
        booking_id = get_valid_input("Enter the booking ID to cancel: ", validate_booking_id)
        for reservation in self.reservations:
            if reservation.reservation_id == booking_id and reservation.status == 'Reserved':
                reservation.status = 'Canceled'
                self.save_reservations()
                self.messages.display_reservation_canceled(booking_id)
                return
        self.messages.display_no_active_reservation()

    def update_reservation(self):
        booking_id = get_valid_input("Enter the booking ID to update: ", validate_booking_id)
        new_date_time = get_valid_input("Enter new reservation date and time (YYYY-MM-DD HH:MM AM/PM): ", validate_booking_date_time)
        
        for reservation in self.reservations:
            if reservation.reservation_id == booking_id and reservation.status == 'Reserved':
                available_tables = self.find_available_table(reservation.seats, new_date_time)
                if not available_tables:
                    self.messages.display_no_available_tables(reservation.seats, new_date_time)
                    return

                reservation.date_time = new_date_time
                reservation.table_id = available_tables[0].table_id
                self.save_reservations()
                self.messages.display_update_success(booking_id)
                return
        self.messages.display_no_active_reservation()

    def view_availability(self):
        date_time = get_valid_input("Enter the date and time to check availability (YYYY-MM-DD HH:MM AM/PM): ", validate_booking_date_time)
        seats = int(get_valid_input("Enter number of seats required: ", validate_seats))

        available_tables = self.find_available_table(seats, date_time)
        if available_tables:
            print(f"Available tables for {seats} seats at {date_time}:")
            for table in available_tables:
                print(table)
        else:
            self.messages.display_no_available_tables(seats, date_time)

    def view_all_reservations(self):
        if not self.reservations:
            self.messages.display_no_reservations_found()
            return
        self.messages.display_all_reservations(self.reservations)

    def search_reservation_by_id(self):
        booking_id = get_valid_input("Enter the booking ID to search: ", validate_booking_id)
        found_reservation = next((res for res in self.reservations if res.reservation_id == booking_id), None)
        
        if found_reservation:
            self.messages.display_reservation_found(found_reservation)
        else:
            self.messages.display_no_reservation_found()
    
    def exit_system(self):
        self.messages.exit_message()

    def welcome_system(self):
        self.messages.welcome_message()    