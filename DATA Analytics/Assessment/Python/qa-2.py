class SchoolManagement:
    def __init__(self):   
        self.students = []   
        self.next_id = 1

    def new_admission(self, name, age, student_class, mobile):
        try:
            if not (5 <= age <= 18):
                raise ValueError("Age must be between 5 and 18.")
            if not (1 <= student_class <= 12):
                raise ValueError("Class must be between 1 and 12.")
            if not (mobile.isdigit() and len(mobile) == 10):
                raise ValueError("Mobile number must be 10 digits.")

            student = {
                "id": self.next_id,
                "name": name,
                "age": age,
                "class": student_class,
                "mobile": mobile
            }
            self.students.append(student)
            print(f"Admission successful! Student ID: {self.next_id}")
            self.next_id += 1

        except Exception as e:
            print(f"Error: {e}")

    def view_student(self, student_id):
        try:
            student = next((s for s in self.students if s["id"] == student_id), None)
            if not student:
                raise LookupError("Student not found.")
            print(f"ID: {student['id']} | Name: {student['name']} | "
                  f"Age: {student['age']} | Class: {student['class']} | Mobile: {student['mobile']}")
        except Exception as e:
            print(f"Error: {e}")

    def update_student(self, student_id, new_class=None, new_mobile=None):
        try:
            student = next((s for s in self.students if s["id"] == student_id), None)
            if not student:
                raise LookupError("Student not found.")

            if new_class is not None:
                if 1 <= new_class <= 12:
                    student["class"] = new_class
                else:
                    raise ValueError("Class must be between 1 and 12.")

            if new_mobile is not None:
                if new_mobile.isdigit() and len(new_mobile) == 10:
                    student["mobile"] = new_mobile
                else:
                    raise ValueError("Mobile must be 10 digits.")

            print("Student updated successfully.")

        except Exception as e:
            print(f"Error: {e}")

    def remove_student(self, student_id):
        try:
            before = len(self.students)
            self.students = [s for s in self.students if s["id"] != student_id]
            if len(self.students) == before:
                raise LookupError("Student not found.")
            print("Student removed.")
        except Exception as e:
            print(f"Error: {e}")

    def list_all(self):
        if not self.students:
            print("No students yet.")
        for s in self.students:
            print(f"{s['id']}: {s['name']} ({s['age']} yrs, Class {s['class']}, Mobile: {s['mobile']})")

if __name__ == "__main__":
    school = SchoolManagement()

    school.new_admission("manas", 16, 10, "9876543210")  
    school.view_student(1)   
    school.update_student(1, new_class=7, new_mobile="1112223334") 

    school.list_all()

    school.remove_student(1)
    school.list_all()
