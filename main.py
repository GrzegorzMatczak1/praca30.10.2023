from student import Student
from student_manager import StudentManager

manager = StudentManager()

while True:
    print("Student Management System Menu:")
    print("a. Add a student")
    print("b. Update a student's details")
    print("c. Delete a student")
    print("d. View all students")
    print("e. Exit")

    choice = input("Enter your choice: ")

    if choice == "a":
        id = input("Enter student ID: ")
        name = input("Enter student name: ")
        age = input("Enter student age: ")
        grade = input("Enter student grade: ")
        student = Student(id, name, age, grade)
        manager.add_student(student)

    elif choice == "b":
        id = input("Enter student ID to update: ")
        name = input("Enter new name: ")
        age = input("Enter new age: ")
        grade = input("Enter new grade: ")
        if not manager.update_student(id, name, age, grade):
            print("Student not found!")

    elif choice == "c":
        id = input("Enter student ID to delete: ")
        if not manager.delete_student(id):
            print("Student not found!")

    elif choice == "d":
        students = manager.view_students()
        for student in students:
            print(student.get_details())

    elif choice == "e":
        break
    