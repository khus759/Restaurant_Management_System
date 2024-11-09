
# from .table_booking_system import TableBookingSystem

# def main():
#     booking_system = TableBookingSystem()

#     while True:
#         print("\n--- Table Booking System ---")
#         print("1. Reserve a table")
#         print("2. Cancel a reservation")
#         print("3. Update a reservation")
#         print("4. View table availability")
#         print("5. Exit")
#         choice = input("Choose an option (1-5): ")

#         if choice == "1":
#             name = input("Enter your name: ")
#             phone = input("Enter your phone number: ")
#             date_time = input("Enter reservation date and time (YYYY-MM-DD HH:MM AM/PM): ")
#             seats = int(input("Enter number of seats required: "))
#             booking_system.reserve_table(name, phone, date_time, seats)

#         elif choice == "2":
#             booking_id = input("Enter the booking ID to cancel: ")
#             booking_system.cancel_reservation(booking_id)

#         elif choice == "3":
#             booking_id = input("Enter the booking ID to update: ")
#             new_date_time = input("Enter new reservation date and time (YYYY-MM-DD HH:MM AM/PM): ")
#             booking_system.update_reservation(booking_id, new_date_time)

#         elif choice == "4":
#             date_time = input("Enter the date and time to check availability (YYYY-MM-DD HH:MM AM/PM): ")
#             seats = int(input("Enter number of seats required: "))
#             booking_system.view_availability(date_time, seats)

#         elif choice == "5":
#             print("Exiting the Table Booking System.")
#             break

#         else:
#             print("Invalid choice. Please select a valid option.")

# if __name__ == "__main__":
#     main()
