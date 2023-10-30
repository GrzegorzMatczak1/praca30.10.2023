class StudentManager:
    def init(self):
        self.students = []

    def add_student(self, student):
        self.students.append(student)

    def update_student(self, id, name, age, grade):
        for student in self.students:
            if student.id == id:
                student.set_details(name, age, grade)
                return True
        return False

    def delete_student(self, id):
        for student in self.students:
            if student.id == id:
                self.students.remove(student)
                return True
        return False

    def view_students(self):
        return self.students