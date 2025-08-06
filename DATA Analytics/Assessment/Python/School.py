class SchoolManagement:
    def __init__(self):
        self.students = {}  # Key: student_id, Value: student data dict
        self.student_id_counter = 1001  # Auto-increment ID

    def new_admission(self):
        print("\n--- New Admission ---")
        name = input("Enter student name: ")
        try:
            age = int(input("Enter age: "))
            student_class = int(input("Enter class (1-12): "))
        except ValueError:
            print("Invalid input. Age and class must be numbers.")
            return

        mobile = input("Enter guardian's mobile number: ")

        # Validations
        if not (5 <= age <= 18):
            print("Invalid age. Must be between 5 and 18.")
            return
        if not (len(mobile) == 10 and mobile.isdigit()):
            print("Invalid mobile number. Must be exactly 10 digits.")
            return

        student_id = f"S{self.student_id_counter}"
        self.student_id_counter += 1

        self.students[student_id] = {
            "name": name,
            "age": age,
            "class": student_class,
            "mobile": mobile
        }

        print(f"Admission successful. Student ID is: {student_id}")

    def view_student(self):
        print("\n--- View Student Details ---")
        student_id = input("Enter student ID (e.g. S1001): ")
        student = self.students.get(student_id)

        if student:
            print(f"Student ID: {student_id}")
            print(f"Name: {student['name']}")
            print(f"Age: {student['age']}")
            print(f"Class: {student['class']}")
            print(f"Guardian Mobile: {student['mobile']}")
        else:
            print("Student not found.")

    def update_student(self):
        print("\n--- Update Student Info ---")
        student_id = input("Enter student ID to update: ")
        if student_id not in self.students:
            print("Student not found.")
            return

        print("1. Update Class\n2. Update Guardian's Mobile Number")
        choice = input("Choose an option: ")

        if choice == '1':
            try:
                new_class = int(input("Enter new class (1-12): "))
                self.students[student_id]["class"] = new_class
                print("Class updated successfully.")
            except ValueError:
                print("Invalid input.")
        elif choice == '2':
            new_mobile = input("Enter new mobile number: ")
            if len(new_mobile) == 10 and new_mobile.isdigit():
                self.students[student_id]["mobile"] = new_mobile
                print("Mobile number updated successfully.")
            else:
                print("Invalid mobile number.")
        else:
            print("Invalid choice.")

    def remove_student(self):
        print("\n--- Remove Student Record ---")
        student_id = input("Enter student ID to remove: ")
        if student_id in self.students:
            del self.students[student_id]
            print("Student record removed.")
        else:
            print("Student not found.")

    def run(self):
        while True:
            print("\n===== School Management System =====")
            print("1. New Admission")
            print("2. View Student Details")
            print("3. Update Student Info")
            print("4. Remove Student Record")
            print("5. Exit")
            choice = input("Enter your choice (1–5): ")

            if choice == '1':
                self.new_admission()
            elif choice == '2':
                self.view_student()
            elif choice == '3':
                self.update_student()
            elif choice == '4':
                self.remove_student()
            elif choice == '5':
                print("Exiting system.")
                break
            else:
                print("Invalid choice. Please enter 1 to 5.")


# Run the program
if __name__ == "__main__":
    sm = SchoolManagement()
    sm.run()
