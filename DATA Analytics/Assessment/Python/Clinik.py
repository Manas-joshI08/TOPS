class ClinicAppointment:
    def __init__(self):
        self.slots = ["10am", "11am", "12pm", "2pm", "3pm"]
        self.appointments = {}  # Key: (doctor, slot), Value: list of patient dicts

    def book_appointment(self):
        print("\n--- Book Appointment ---")
        name = input("Enter patient name: ")
        age = input("Enter age: ")
        mobile = input("Enter mobile number: ")
        doctor = input("Enter preferred doctor name: ")

        print("Available Time Slots:")
        for slot in self.slots:
            print("-", slot)
        slot = input("Choose a time slot: ")

        if slot not in self.slots:
            print("Invalid time slot. Try again.")
            return

        key = (doctor, slot)

        if key not in self.appointments:
            self.appointments[key] = []

        if len(self.appointments[key]) >= 3:
            print("Sorry, this slot is full for Dr.", doctor)
            return

        self.appointments[key].append({
            "name": name,
            "age": age,
            "mobile": mobile
        })

        print(f"Appointment booked with Dr. {doctor} at {slot}.")

    def view_cancel_appointment(self):
        print("\n--- View/Cancel Appointment ---")
        mobile = input("Enter your mobile number: ")
        found = False

        for key in list(self.appointments.keys()):
            doctor, slot = key
            for patient in self.appointments[key]:
                if patient["mobile"] == mobile:
                    found = True
                    print(f"\nAppointment Found:\nDoctor: {doctor}\nSlot: {slot}")
                    print(f"Patient Name: {patient['name']}, Age: {patient['age']}")
                    choice = input("Do you want to cancel this appointment? (yes/no): ").lower()
                    if choice == "yes":
                        self.appointments[key].remove(patient)
                        print("Appointment cancelled.")
                        # Clean up empty keys
                        if not self.appointments[key]:
                            del self.appointments[key]
                    return

        if not found:
            print("No appointment found with this mobile number.")

    def run(self):
        while True:
            print("\n======= Clinic Appointment System =======")
            print("1. Book Appointment")
            print("2. View/Cancel Appointment")
            print("3. Exit")
            choice = input("Enter your choice (1-3): ")

            if choice == '1':
                self.book_appointment()
            elif choice == '2':
                self.view_cancel_appointment()
            elif choice == '3':
                print("Thank you! Exiting system.")
                break
            else:
                print("Invalid choice. Please enter 1, 2, or 3.")


# To run the system
if __name__ == "__main__":
    app = ClinicAppointment()
    app.run()
