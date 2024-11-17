import json
from datetime import datetime
from Src.Utility.path_manager import reservations_file
from Src.Messages.booking_table import BookingHandler
from Src.Messages.reports import Report
    
class ReservationReport:
    def __init__(self, reservation_file=reservations_file):
        self.reservation_file = reservation_file
        self.reservations = self.load_reservations()
        self.booking_handler = BookingHandler()
        self.report = Report()

    def load_reservations(self):
        with open(self.reservation_file, 'r') as file:
            return json.load(file)

    def show_reservations_by_date(self):
        date_input = input("Enter date (YYYY-MM-DD) or month (YYYY-MM): ").strip()
        is_specific_date = len(date_input) == 10

        reservations_on_date = []
        
        for reservation in self.reservations:
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
                    "booking_date": formatted_date
                })

        if reservations_on_date:
            self.report.show_reservations_header(date_input)
            for res in reservations_on_date:
                self.report.show_reservation_details(res)
        else:
            self.report.no_reservations_found(date_input)

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
                        "date": formatted_date,
                        "cancellation_date": formatted_date
                    })

        if canceled_reservations:
            self.report.show_canceled_reservations_header()
            for res in canceled_reservations:
                self.report.show_canceled_reservation_details(res)
        else:
            self.report.no_canceled_reservations_found()
