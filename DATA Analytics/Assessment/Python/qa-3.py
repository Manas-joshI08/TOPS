class BusReservation:
    def __init__(self):
        self.routes = {
            "Mumbai to Pune": 500,
            "Delhi to Jaipur": 600,
            "Bangalore to Chennai": 550,
            "Kolkata to Patna": 450
        }
        self.tickets = {}  
        self.next_ticket_id = 1
        self.max_seats = 40
        self.seat_allocation = {route: [] for route in self.routes} 

    def show_routes(self):
        print("\nAvailable Routes:")
        for i, (route, price) in enumerate(self.routes.items(), start=1):
            print(f"{i}. {route} - ₹{price}")

    def get_route_by_number(self, number): 
        routes_list = list(self.routes.keys())
        if 1 <= number <= len(routes_list):
            return routes_list[number - 1]
        return None

    def book_ticket(self, name, age, mobile, route):
        try:
            if route not in self.routes:
                raise ValueError("Invalid route selected.")
            if not (mobile.isdigit() and len(mobile) == 10):
                raise ValueError("Mobile number must be 10 digits.")
            if not (5 <= age <= 100):
                raise ValueError("Invalid age entered.")

            if len(self.seat_allocation[route]) >= self.max_seats:
                raise OverflowError("All seats are booked for this route.")

            seat_number = len(self.seat_allocation[route]) + 1
            self.seat_allocation[route].append(seat_number)

            ticket_id = self.next_ticket_id
            self.next_ticket_id += 1

            self.tickets[ticket_id] = {
                "name": name,
                "age": age,
                "mobile": mobile,
                "route": route,
                "seat": seat_number,
                "price": self.routes[route]
            }
            print(f"\n Ticket booked successfully! Ticket ID: {ticket_id}, Seat: {seat_number}")

        except Exception as e:
            print(f"Error: {e}")

    def view_ticket(self, ticket_id):
        try:
            ticket = self.tickets.get(ticket_id)
            if not ticket:
                raise KeyError("Ticket not found.")

            print(f"\n Ticket ID: {ticket_id}")
            print(f"Passenger: {ticket['name']} ({ticket['age']} yrs)")
            print(f"Mobile: {ticket['mobile']}")
            print(f"Route: {ticket['route']}")
            print(f"Seat: {ticket['seat']}")
            print(f"Price: ₹{ticket['price']}\n")
        except Exception as e:
            print(f"Error: {e}")

    def cancel_ticket(self, ticket_id):
        try:
            ticket = self.tickets.pop(ticket_id, None)
            if not ticket:
                raise KeyError("Ticket not found.")

            self.seat_allocation[ticket["route"]].remove(ticket["seat"])
            print(f"\n Ticket {ticket_id} cancelled successfully.")
        except Exception as e:
            print(f"Error: {e}")


if __name__ == "__main__":
    bus = BusReservation()

    while True:
        print("\n=== BUS RESERVATION SYSTEM ===")
        print("1. Show Routes")
        print("2. Book Ticket")
        print("3. View Ticket")
        print("4. Cancel Ticket")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == "1":
            bus.show_routes()

        elif choice == "2":
            name = input("Enter passenger name: ")
            age = int(input("Enter age: "))
            mobile = input("Enter mobile number: ")

            bus.show_routes()
            try:
                route_num = int(input("Select route number: "))
                route_choice = bus.get_route_by_number(route_num)

                if route_choice is None:
                    print("Invalid route number.")
                else:
                    bus.book_ticket(name, age, mobile, route_choice)

            except ValueError:
                print(" Please enter a valid number.")

        elif choice == "3":
            try:
                ticket_id = int(input("Enter Ticket ID: "))
                bus.view_ticket(ticket_id)
            except ValueError:
                print(" Please enter a valid Ticket ID.")

        elif choice == "4":
            try:
                ticket_id = int(input("Enter Ticket ID to cancel: "))
                bus.cancel_ticket(ticket_id)
            except ValueError:
                print("Please enter a valid Ticket ID.")

        elif choice == "5":
            print("Exiting system... Goodbye ")
            break

        else:
            print(" Invalid choice. Please try again.")
