
class Reservation:
    def __init__(self, reservation_id, name, phone, date_time, seats, table_id, status="Reserved"):
        self.reservation_id = reservation_id
        self.name = name
        self.phone = phone
        self.date_time = date_time
        self.seats = seats
        self.table_id = table_id
        self.status = status

    def __repr__(self):
        return f"Reservation {self.reservation_id} for {self.name} on {self.date_time} at Table {self.table_id}"
