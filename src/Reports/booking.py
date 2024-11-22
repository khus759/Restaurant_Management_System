from datetime import datetime, timedelta
import json
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

    def get_last_week_date_range(self):
        """Return start and end date for the last week."""
        today = datetime.today()
        start_of_week = today - timedelta(days=today.weekday())  # Start of this week
        start_of_last_week = start_of_week - timedelta(weeks=1)  # Start of last week
        end_of_last_week = start_of_week - timedelta(days=1)  # End of last week
        return start_of_last_week, end_of_last_week

    def show_reservations_by_date(self):
        """Show reservations filtered by date input."""
        date_input = input("Enter date (YYYY-MM-DD), month (YYYY-MM), or 'last_week' for last week's reservations: ").strip()
        
        if date_input.lower() == "last_week":
            start_date, end_date = self.get_last_week_date_range()
            date_input = f"Last week: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
            reservations_on_date = self.filter_reservations_by_date_range(start_date, end_date)
        else:
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
        """Show canceled reservations filtered by date input."""
        date_input = input("Enter date (YYYY-MM-DD), month (YYYY-MM), 'last_week' for last week's canceled reservations, or leave empty to show all canceled reservations: ").strip()
        
        if date_input.lower() == "last_week":
            start_date, end_date = self.get_last_week_date_range()
            date_input = f"Last week: {start_date.strftime('%Y-%m-%d')} to {end_date.strftime('%Y-%m-%d')}"
            canceled_reservations = self.filter_canceled_reservations_by_date_range(start_date, end_date)
        else:
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

    def filter_reservations_by_date_range(self, start_date, end_date):
        """Filter reservations by the given date range."""
        reservations_in_range = []
        for reservation in self.reservations:
            reservation_date = datetime.strptime(reservation['date_time'], '%Y-%m-%d %I:%M %p')
            if start_date <= reservation_date <= end_date:
                reservations_in_range.append({
                    "name": reservation["name"],
                    "phone": reservation["phone"],
                    "time": reservation_date.strftime('%I:%M %p'),
                    "table_id": reservation["table_id"],
                    "status": reservation["status"],
                    "booking_date": reservation_date.strftime('%Y-%m-%d')
                })
        return reservations_in_range

    def filter_canceled_reservations_by_date_range(self, start_date, end_date):
        """Filter canceled reservations by the given date range."""
        canceled_reservations_in_range = []
        for reservation in self.reservations:
            if reservation['status'] == 'Canceled':
                reservation_date = datetime.strptime(reservation['date_time'], '%Y-%m-%d %I:%M %p')
                if start_date <= reservation_date <= end_date:
                    canceled_reservations_in_range.append({
                        "name": reservation["name"],
                        "phone": reservation["phone"],
                        "time": reservation_date.strftime('%I:%M %p'),
                        "table_id": reservation["table_id"],
                        "date": reservation_date.strftime('%Y-%m-%d'),
                        "cancellation_date": reservation_date.strftime('%Y-%m-%d')
                    })
        return canceled_reservations_in_range
