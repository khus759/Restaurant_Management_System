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
        date_input = input("Enter date (YYYY-MM-DD) or month (YYYY-MM): ").strip()
        is_specific_date = len(date_input) == 10

        reservations_on_date = []
        
        for reservation in self.reservations:
            # Parse the date from the reservation entry
            reservation_date = datetime.strptime(reservation['date_time'], '%Y-%m-%d %I:%M %p')
            formatted_date = reservation_date.strftime('%Y-%m-%d')
            formatted_month = reservation_date.strftime('%Y-%m')

            if (is_specific_date and formatted_date == date_input) or (not is_specific_date and formatted_month == date_input):
                reservations_on_date.append({
                    "name": reservation["name"],
                    "phone": reservation["phone"],
                    "time": reservation_date.strftime('%I:%M %p'),
                    "table_id": reservation["table_id"],
                    "status": reservation["status"],
                    "booking_date": formatted_date  # Adds the booking date
                })

        # Display reservations on the specified date or month
        if reservations_on_date:
            print(f"\nReservations on {date_input}:")
            for res in reservations_on_date:
                print(f"Name: {res['name']}, Phone: {res['phone']}, Booking Date: {res['booking_date']}, Time: {res['time']}, Table: {res['table_id']}, Status: {res['status']}")
        else:
            print(f"No reservations found for {date_input}.")

    def show_canceled_reservations(self):
        date_input = input("Enter date (YYYY-MM-DD) or month (YYYY-MM) to filter, or leave empty to show all canceled reservations: ").strip()
        is_specific_date = len(date_input) == 10

        canceled_reservations = []

        for reservation in self.reservations:
            if reservation['status'] == 'Canceled':
                reservation_date = datetime.strptime(reservation['date_time'], '%Y-%m-%d %I:%M %p')
                formatted_date = reservation_date.strftime('%Y-%m-%d')
                formatted_month = reservation_date.strftime('%Y-%m')

                if not date_input or (is_specific_date and formatted_date == date_input) or (not is_specific_date and formatted_month == date_input):
                    canceled_reservations.append({
                        "name": reservation["name"],
                        "phone": reservation["phone"],
                        "time": reservation_date.strftime('%I:%M %p'),
                        "table_id": reservation["table_id"],
                        "date": formatted_date,      # Adds the booking date
                        "cancellation_date": formatted_date  # Adds the cancellation date
                    })

        # Display canceled reservations
        if canceled_reservations:
            print(f"\nCanceled Reservations:")
            for res in canceled_reservations:
                print(f"Name: {res['name']}, Phone: {res['phone']}, Cancellation Date: {res['cancellation_date']}, Time: {res['time']}, Table: {res['table_id']}")
        else:
            print("No canceled reservations found for the specified date or month.")
