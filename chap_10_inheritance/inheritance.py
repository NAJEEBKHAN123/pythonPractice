class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

     
class Student(Person):
    def __init__(self, name, age, year):
        super().__init__(name, age)
        self.graduationYear = year
    
    def welcome(self):
        print(f"welcome {self.name}  the section of {self.graduationYear}")
            


p = Student("ali", 30, 2025)
print(p.name, p.age, p.graduationYear)
p.welcome()

    
