
# class Programmer:
#    company = "MicroSoft"
#    def __init__(self, name, age, salary):
#       self.name = name
#       self.age = age
#       self.salary = salary
    


# print("Details of the employee at MicroSoft companay: ")
# AliInfo = Programmer("M Ali", 20, 120000)
# print(f"1: M Ali Details: Name: {AliInfo.name}, Age: {AliInfo.age}, Salary: {AliInfo.salary} at  {AliInfo.company}")

# BilalInfo = Programmer("Bilal Ahmad", 22, 130000)
# print(f"2: Bilal Ahmad Details: Name: {BilalInfo.name}, Age: {BilalInfo.age}, Salary: {BilalInfo.salary} ")

# NajeebInfo = Programmer("Najeeb Ullah", 24, 150000)
# print(f"3: Bilal Ahmad Details: Name: {NajeebInfo.name}, Age: {NajeebInfo.age}, Salary: {NajeebInfo.salary} ")


# Q2 

# class Calculator: 
    
#     def __init__(self, n):
#         self.n = n
    
#     def square(self):
#         print("the squre is ", self.n * self.n)

#     def cube(self):
#         print('the cube is: ', self.n * self.n * self.n)

#     def squareRoot(self):
#         print("the the square: ", self.n ** 1/2)

# p = Calculator(4)

# p.square()
# p.cube()
# p.squareRoot()


# Q3 

# class isObjAtrrRepalce:
#     x = 9

# p = isObjAtrrRepalce()
# p.x = 0
# print(p.x)


# Q4:

class staticMethod:
    # def __init__(self, name):
    #     self.name = name
    
    # def greet(self):
    #     print(f"Hello {self.name} this is me Najeeb")

    @staticmethod
    def hello():
        print("Hello there!")


name = staticMethod()
name.hello()