
class Student:
    def __init__(self, name, age, gender, place):
        self.name = name
        self.age = age
        self.gender = gender
        self.place = place

    def profile(self):
        print("----------------------")
        print("Profile Information")
        print("----------------------")
        print(f"Name : {self.name}")
        print(f"Age : {self.age}")
        print(f"Gender : {self.gender}")
        print(f"place : {self.place}")

    @staticmethod
    def Addition(a: int, b: int) -> int:
        return a + b

