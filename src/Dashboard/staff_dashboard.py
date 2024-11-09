
from Src.Menu_management.menu_feature import MenuManagement
from Src.Utility.ask_dashboard import ask_for_dashboard

class StaffDashboard:
    def __init__(self):
        self.menu_management = MenuManagement()

    def display_dashboard(self):
        while True:
            print("\n********* Staff Dashboard *********")
            print("1. Show Menu")
            print("2. Take New Order")
            print("3. Update Order")
            print("4. Cancel Order")
            print("5. Invoice")
            print("6. Search Invoice")
            print("7. Show Invoice")
            print("8. Booking")
            print("9. Cancel Reservation")
            print("10.View Availablity")
            #print("11. ")
            print("12. Logout")

            try:
                action = input("Choose an action: ")
            except:
                print("please choose valid input")
                continue

            if action == "1":
                self.menu_management.show_menu()
            elif action == "2":
                print("Taking new order...")  
            elif action == "3":
                print("Updating order...")
            elif action == "4":
                print("Cancelling order...")
            elif action == "12":
                print("Logging out...")
                break
            else:
                print("Invalid choice.")
            
            if not ask_for_dashboard():
                break
