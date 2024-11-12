import json
from datetime import datetime
from Src.Utility.path_manager import reservations_file
from Src.Messages.booking_table import BookingHandler

class ReservationReport:
    def __init__(self, reservation_file=reservations_file):
        self.reservation_file = reservation_file
        self.reservations = self.load_reservations()
        self.booking_handler = BookingHandler()

    def load_reservations(self):
        with open(self.reservation_file, 'r') as file:
            return json.load(file)

    def show_reservations_by_date(self):
        # Taking user input for date or month
        date_input = input("Enter date (YYYY-MM-DD) or month (YYYY-MM): ")
        is_specific_date = len(date_input) == 10  # Checking if the input is for a specific date

        reservations_on_date = []
        
        for reservation in self.reservations:
            # Parse the date from the reservation entry
            reservation_date = datetime.strptime(reservation['date_time'], '%Y-%m-%d %I:%M %p')
            formatted_date = reservation_date.strftime('%Y-%m-%d')
            formatted_month = reservation_date.strftime('%Y-%m')

            # Check if the reservation date or month matches the input
            if (is_specific_date and formatted_date == date_input) or (not is_specific_date and formatted_month == date_input):
                reservations_on_date.append({
                    "name": reservation["name"],
                    "phone": reservation["phone"],
                    "time": reservation_date.strftime('%I:%M %p'),
                    "table_id": reservation["table_id"],
                    "status": reservation["status"]
                })

        # Display results using PrintHandler
        self.booking_handler.display_reservations_on_date(date_input, reservations_on_date)

    def show_canceled_reservations(self):
        # Taking user input for date or month (optional)
        date_input = input("Enter date (YYYY-MM-DD) or month (YYYY-MM) to filter, or leave empty to show all: ").strip()
        is_specific_date = len(date_input) == 10

        canceled_reservations = []

        for reservation in self.reservations:
            if reservation['status'] == 'Canceled':
                reservation_date = datetime.strptime(reservation['date_time'], '%Y-%m-%d %I:%M %p')
                formatted_date = reservation_date.strftime('%Y-%m-%d')
                formatted_month = reservation_date.strftime('%Y-%m')

                # Check if reservation matches the date/month filter or if no filter is applied
                if not date_input or (is_specific_date and formatted_date == date_input) or (not is_specific_date and formatted_month == date_input):
                    canceled_reservations.append({
                        "name": reservation["name"],
                        "phone": reservation["phone"],
                        "time": reservation_date.strftime('%I:%M %p'),
                        "table_id": reservation["table_id"],
                        "date": formatted_date
                    })

        # Display results using PrintHandler
        self.booking_handler.display_canceled_reservations(canceled_reservations)
