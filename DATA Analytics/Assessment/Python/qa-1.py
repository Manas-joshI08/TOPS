class ClinicAppointment:
    def _init_(self):
        self.appointments = {}

    def bookAppointment(self, dr_dict):
        try:
            name = input("Enter patient name: ")
            age = int(input("Enter patient age: "))
            mobile_number = input("Enter patient mobile number: ")
            
          
            print("\nAvailable Doctors and their time slots:")
            for dr_name, slots in dr_dict.items():
                available_slots = [slot for slot, count in slots.items() if count < 3]
                print(f"- {dr_name}: {', '.join(available_slots)}")

            dr_name = input("\nPlease enter preferred doctor's name: ")
            if dr_name not in dr_dict:
                raise ValueError("This doctor's name is not in our system.")

            slot = input("Please enter the preferred time slot: ")
            if slot not in dr_dict[dr_name]:
                raise ValueError("This time slot is not available for the selected doctor.")

            if self.checkDrAvailability(dr_dict, dr_name, slot):
                patient_info = {
                    'name': name,
                    'age': age,
                    'doctor': dr_name,
                    'slot': slot
                }
                self.appointments[mobile_number] = patient_info
                print("\n--- Your appointment is booked successfully! ---")
                print(f"Patient: {name}, Doctor: {dr_name}, Time: {slot}")
            else:
                print("\n--- Sorry, the selected slot is fully booked. Please try another time. ---")

        except ValueError as e:
            print(f"\n--- Error: Invalid input. {e} ---")
        except Exception as e:
            print(f"\n--- An unexpected error occurred: {e} ---")

    def view_Cancel_app(self):
        mobile_number = input("Enter your mobile number to view or cancel your appointment: ")
        
        if mobile_number in self.appointments:
            appointment_info = self.appointments[mobile_number]
            print("\n--- Your Appointment Details ---")
            print(f"Patient Name: {appointment_info['name']}")
            print(f"Doctor: {appointment_info['doctor']}")
            print(f"Time Slot: {appointment_info['slot']}")
            
            action = input("\nDo you want to cancel this appointment? (yes/no): ").lower()
            if action == 'yes':
                dr_name = appointment_info['doctor']
                slot = appointment_info['slot']
                
               
                if dr_name in dr_dict and slot in dr_dict[dr_name]:
                    dr_dict[dr_name][slot] -= 1
                    del self.appointments[mobile_number]
                    print("\n--- Your appointment has been canceled. ---")
            else:
                print("\n--- No changes were made. ---")
        else:
            print("\n--- No appointment found for this mobile number. ---")

    def checkDrAvailability(self, dr_dict, dr_name, slot):
      
        if dr_dict[dr_name][slot] < 3:
            dr_dict[dr_name][slot] += 1
            return True
        else:
            return False

dr_dict = {
    'Dr Shah': {'10 am': 0, '11 am': 0, '2 pm': 0},
    'Dr Patel': {'11 am': 0, '3 pm': 0},
    'Dr Modi': {'10 am': 0, '11 am': 0, '4 pm': 0}
}

if _name_ == "_main_":
    obj = ClinicAppointment()
    while True:
        print("\n--- Clinic Appointment System ---")
        print("1. Book an Appointment")
        print("2. View/Cancel an Appointment")
        print("3. Exit")
        
        choice = input("Enter your choice (1, 2, or 3): ")

        if choice == '1':
            obj.bookAppointment(dr_dict)
        elif choice == '2':
            obj.view_Cancel_app()
        elif choice == '3':
            print("Thank you for using the system. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter 1, 2, or 3.")