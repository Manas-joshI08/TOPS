class BusReservation:
    def __init__(self):
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Ahmedabad to Surat": 450,
            "Bangalore to Mysore": 550
        }
        self.bookings = {}  # Key: ticket_id, Value: booking info
        self.seats = {}     # Key: route, Value: list of booked seat numbers
        self.ticket_counter = 1001

    def show_routes(self):
        print("\n--- Available Routes ---")
        for route, price in self.routes.items():
            print(f"{route} - ₹{price}")

    def book_ticket(self):
        print("\n--- Book Ticket ---")
        name = input("Enter passenger name: ")
        try:
            age = int(input("Enter age: "))
        except ValueError:
            print("Invalid age.")
            return
        mobile = input("Enter mobile number: ")

        self.show_routes()
        route = input("Enter route as shown above: ")

        if route not in self.routes:
            print("Invalid route.")
            return

        if route not in self.seats:
            self.seats[route] = []

        if len(self.seats[route]) >= 40:
            print("All seats are booked on this route.")
            return

        seat_no = len(self.seats[route]) + 1
        ticket_id = f"T{self.ticket_counter}"
        self.ticket_counter += 1

        self.bookings[ticket_id] = {
            "name": name,
            "age": age,
            "mobile": mobile,
            "route": route,
            "seat": seat_no,
            "price": self.routes[route]
        }

        self.seats[route].append(seat_no)

        print(f"Ticket booked successfully!\nTicket ID: {ticket_id}\nSeat No: {seat_no}")

    def view_ticket(self):
        print("\n--- View Ticket ---")
        ticket_id = input("Enter your ticket ID: ")

        if ticket_id in self.bookings:
            ticket = self.bookings[ticket_id]
            print(f"\nTicket Details for {ticket_id}:")
            print(f"Passenger: {ticket['name']} (Age: {ticket['age']})")
            print(f"Mobile: {ticket['mobile']}")
            print(f"Route: {ticket['route']}")
            print(f"Seat No: {ticket['seat']}")
            print(f"Price: ₹{ticket['price']}")
        else:
            print("Ticket not found.")

    def cancel_ticket(self):
        print("\n--- Cancel Ticket ---")
        ticket_id = input("Enter your ticket ID to cancel: ")

        if ticket_id in self.bookings:
            route = self.bookings[ticket_id]["route"]
            seat_no = self.bookings[ticket_id]["seat"]

            # Remove seat and ticket
            self.seats[route].remove(seat_no)
            del self.bookings[ticket_id]

            print(f"Ticket {ticket_id} cancelled successfully.")
        else:
            print("Ticket not found.")

    def run(self):
        while True:
            print("\n===== Bus Reservation System =====")
            print("1. Show Available Routes")
            print("2. Book Ticket")
            print("3. View Ticket")
            print("4. Cancel Ticket")
            print("5. Exit")
            choice = input("Enter your choice (1–5): ")

            if choice == '1':
                self.show_routes()
            elif choice == '2':
                self.book_ticket()
            elif choice == '3':
                self.view_ticket()
            elif choice == '4':
                self.cancel_ticket()
            elif choice == '5':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please enter a number from 1 to 5.")


# Run the system
if __name__ == "__main__":
    system = BusReservation()
    system.run()
