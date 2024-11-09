
class Table:
    def __init__(self, table_id, seats):
        self.table_id = table_id
        self.seats = seats

    def __repr__(self):
        return f"Table {self.table_id} ({self.seats} seats)"
