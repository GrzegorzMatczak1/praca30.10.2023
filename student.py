class Student:
    def init(self, id, name, age, grade):
        self.id = id
        self.name = name
        self.age = age
        self.grade = grade

    def get_details(self):
        return f"ID: {self.id}, Name: {self.name}, Age: {self.age}, Grade: {self.grade}"

    def set_details(self, name, age, grade):
        self.name = name
        self.age = age
        self.grade = grade