# 🧠 Beginner Level Inheritance Tasks in Python
# 1. Vehicle Inheritance 🚗
# Base Class: Vehicle

# Attributes: brand, model

# Method: display_info()

# Child Classes:

# Car → Extra attribute: doors

# Motorcycle → Extra attribute: type (sports/cruiser)


# class Vehicle:
#     def __init__(self, brand, model):
#         self.brand = brand
#         self.model = model
    
#     def display_info(self):
#         print(f"The Car model {self.model} and brand {self.brand}")
    
# class Car(Vehicle):
#     def __init__(self,brand, model, doors):
#         super().__init__(brand, model)
#         self.doors = doors

#     def display_info(self):
#         print(f"Model: {self.model} Brand: {self.brand} Doors: {self.doors}")

# class Motorcycle(Vehicle):

#    def __init__(self, brand, model, bike_type):
#        super().__init__(brand, model)
#        self.bike_type = bike_type
       
#    def display_info(self):
       
#        print(f"Model: {self.model} Brand: {self.brand} Doors: {self.bike_type}")
    



# p = Car('TOYOTA', 2022, 4)
# p.display_info()

# bike = Motorcycle('Honda', 2024, "speedy")
# bike.display_info()


# 2. Animal Sounds 🐶🐱🐦
# Base Class: Animal

# Attribute: name

# Method: speak() (default: "Some sound")

# Child Classes:

# Dog → speak() returns "Woof!"

# Cat → speak() returns "Meow!"

# Bird → speak() returns "Tweet!"


# class Animal:
#     def __init__(self, name):
#         self.name = name
    
#     def speak(self):
#        print(f"{self.name} make some sound.")

# class Dog(Animal):
#     def speak(self):
#         print(f"{self.name} says: Woof!")

# class Cat(Animal):
#     def speak(self):
#         print(f"{self.name} says: Meow!")


# class Bird(Animal):
#      def speak(self):
#         print(f"{self.name} says: Tweet!")
       


# p = Animal("Tiger")
# p.speak()


# dog = Dog("Buddy")
# Cat = Cat("Kitty")
# Bird = Bird("Tweety")

# dog.speak()
# Cat.speak()
# Bird.speak()


# 3. Employee Types 💼
# Base Class: Employee

# Attributes: name, salary

# Method: display_info()

# Child Classes:

# Manager → Extra attribute: department

# Developer → Extra attribute: programming_language

# class Employee:
#     def __init__(self, name, salary):
#         self.name = name
#         self.salary = salary

#     def display_info(self):
#         print(f"Employee Name: {self.name} \nSalary: {self.salary}")

# class Manager(Employee):
#     def __init__(self, name, salary, department):
#         super().__init__(name, salary) 
#         self.department = department
    
#     def display_info(self):
#         super().display_info()
#         print(f"Department: {self.department}")

# class Developer(Employee):
#     def __init__(self, name, salary, programmingLang ):
#         super().__init__(name, salary)
#         self.programmingLang = programmingLang
    
#     def display_info(self):
#         super().display_info()
#         print(f"Programming Lang: {self.programmingLang}")

# emp = Employee("Muhammad Umar", 220000)
# emp.display_info()


# manager = Manager("Talha Ahmad", 120000,"ACCA")
# manager.display_info()

# deve = Developer("Zeeshan Ijaz", 90000,"javaScript")
# deve.display_info()


# 4. Bank Accounts 🏦
# Base Class: BankAccount

# Attributes: account_holder, balance

# Methods: deposit(), withdraw(), check_balance()

# Child Classes:

# SavingsAccount → Extra attribute: interest_rate

# CurrentAccount → Extra attribute: overdraft_limit


class BankAccount:
    def __init__(self, account_holder, balance):
        self.account_holder = account_holder
        self.balance = balance

    
    def deposit(self, amount):
        self.balance += amount
        print(f"Dear {self.account_holder},  {amount}: Deposit successfully!")
    
    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount 
            print(f"Dear {self.account_holder}, {amount} Withdraw successfully!")
        else:
            print("You have enter insuffient balance")
        
    def check_balance(self):
        print(f"Dear {self.account_holder} Your total balance: {self.balance}")
  




# class SavingsAccount(BankAccount):
#     def __init__(self, account_holder, balance, interest_rate):
#         super().__init__(account_holder, balance)
#         self.interest_rate = interest_rate
#         print(f"the interest rate is : {self.interest_rate}")

#     def add_interest(self):
#         interest = self.balance * self.interest_rate
#         self.deposit(interest)
#         print(f"interest added: {interest}")


# class CurrentAccount(BankAccount):
#     def __init__(self, account_holder, balance, overdraft_limit):
#         super().__init__(account_holder, balance)
#         self.overdraft_limit = overdraft_limit

#     def withdraw(self, amount):
#         # Override parent's withdraw() to allow overdraft
#         if (self.balance - amount) >= -self.overdraft_limit:
#             self.balance -= amount
#         else:
#             print("Withdrawal denied! Exceeds overdraft limit.")

# p = BankAccount("Ali khan", 100000)

# p.deposit(20000)
# p.withdraw(10000)
# p.check_balance()

# save = SavingsAccount("Umar Ali",500000, 0.01)
# save.add_interest()
# save.deposit(20000)
# save.withdraw(10000)
# save.check_balance()


# curr = CurrentAccount("kashif khan",500000, 2)
# curr.deposit(20000)
# curr.withdraw(10000)
# curr.check_balance()



# 5. Shape Area Calculator 📏
# Base Class: Shape

# Method: area() (default: returns 0)

# Child Classes:

# Rectangle → attributes: length, width, area() returns length * width

# Circle → attributes: radius, area() returns 3.14 * radius^2


# class Shape:

#     def area():
#         return 0
    
# class Rechtangle():
#     def __init__(self, width, length):
#         self.width = width
#         self.length = length
#     def area(self):
#         return self.length * self.width
    
# class Circle():
#     def __init__(self, radius):
#         self.radius = radius

#     def area(self):
#         return 3.14 * self.radius ** 2
    



# rect = Rechtangle(4,5)
# print(rect.area())

# cir = Circle(5)
# print(cir.area())


# 1. Library Management System 📚
# Base Class: LibraryItem

# Attributes: title, author, year

# Method: display_info()

# Child Classes:

# Book → Extra attribute: pages



# Task:

# Create a list of mixed Book and Magazine objects and display their details using a loop.

# class LibraryItem:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
    
#     def display_info(self):
#         print(f"Book Title: {self.title}")
#         print(f"Book Author: {self.author}")
#         print(f"Book Year: {self.year}")

        
# class Book(LibraryItem):
#     def __init__(self, title, author, year, pages):
#         super().__init__(title,author,year)
#         self.pages = pages

#     def display_info(self):
#         super().display_info()
#         print(f"Book pages: {self.pages}")

# class Magazine(LibraryItem):
#     def __init__(self, title, author, year, issueNumber):
#         super().__init__(title,author,year)
#         self.issueNumber = issueNumber

#     def display_info(self):
#         super().display_info()
#         print(f"Book Issue No: {self.issueNumber}")
    

    
# library = [
#     Book("Python Basics", "John Doe", 2023, 350),
#     Magazine("Tech Today", "Jane Smith", 2025, "March")
# ]

# for item in library:
#     item.display_info()
#     print("-----")


# 2. Online Store Products 🛒
# Base Class: Product

# Attributes: name, price

# Method: display_info()

# Child Classes:

# Electronics → Extra attribute: warranty

# Clothing → Extra attribute: size

# Extra Challenge:

# Override display_info() in each child class to include the extra attribute.

# Create a method apply_discount(percent) in the base class and use it for both child classes.


class Product:
    def __init__(self, name, price):
        self.name = name
        self.price = price
    
    def apply_discount(self, percent):
        """Reduce price by a given percentage"""
        if 0 <= percent <= 100:
            discount_amount = self.price * (percent / 100)
            self.price -= discount_amount
        else:
            print("Invalid discount percentage")
        

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Product Price: {self.price}")
    
   
class Electronics(Product):
    def __init__(self, name, price, warranty):
        super().__init__(name,price)
        self.warranty = warranty
    
    def display_info(self):
        super().display_info()
        print(f"Product Warranty: {self.warranty}")
    

    def apply_discount(self, percent):
        super().apply_discount(percent)

class Clothing(Product):
     def __init__(self, name, price, size):
        super().__init__(name,price)
        self.size = size

     def display_info(self):
        super().display_info()
        print(f"Product Size: {self.size}")
    
     def apply_discount(self, percent):
        super().apply_discount(percent)



clo = Clothing("Tayyiba cottan", 3000, 4)
clo.display_info()
clo.apply_discount(5)
print("\nAfter Discount:")
clo.display_info()

        

electronic = Electronics("headphones", 2400, "2 Years" )
electronic.display_info()
electronic.apply_discount(5)
print("\nAfter Discount:")
electronic.display_info()






