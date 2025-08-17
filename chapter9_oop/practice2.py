# # 🧠 Beginner Level Tasks
# # 1. Student Management System
# # Objective: Create a Student class with the following attributes:

# # name, roll_number, marks (as a dictionary for subjects)

# # Methods:

# # add_marks(subject, mark)

# # get_average_marks()

# # display_info()


# class Student:

#     def __init__(self, name, roll_number):
#         self.name = name
#         self.roll_number = roll_number
#         self.marks = {}
    
#     def add_marks(self, subject, mark):
#         self.marks[subject] = mark
#         print(f"Added: {subject} - {mark} marks")

#     def get_average_marks(self):
#         if not self.marks:
#             return 0
#         return sum(self.marks.values()) / len(self.marks)
    
#     def get_grade(self):

#         average= self.get_average_marks()

#         if average >= 90:
#             return "Grade A"
#         elif average >= 80 and average < 90:
#             return "Grade B"
#         elif average >= 60 and average < 80:
#             return "Grade C"
#         elif average >= 50 and average < 60:
#             return "Grade D"
#         elif average < 50:
#             return "Fail"
#         else:
#             print("You does not provide marks")


#     def display_info(self):
#         print("Student Name: ", self.name)
#         print("Student Roll No: ", self.roll_number)
#         print("Marks:")

#         print(f"Average Marks: {self.get_average_marks():.2f}")
#         print(f"Overall Grade: {self.get_grade()}")






# p = Student("Bilal Ahmad", 2100)

# p.add_marks("English", 85)
# p.add_marks("Python", 72)
# p.add_marks("Javascipt", 93)

# p.display_info()




# 2. Bank Account Simulation
# Objective: Create a BankAccount class.

# Attributes:

# account_holder, balance

# Methods:

# deposit(amount)

# withdraw(amount)

# check_balance()

# Add logic to prevent overdrawing.
        

# class BankAccount:
#     def __init__(self, accountHolder, balance):
#         self.accountHolder = accountHolder
#         self.balance = balance
    
#     def deposit(self, amount):
#         self.balance += amount
#         print(f"{amount} Deposite successfully! new balance: ", self.balance)

    
#     def withdraw(self, amount):
#         if amount > self.balance:
#             print("Withdraw Failed! Insuffient balanced")
#         else: 
#             self.balance -= amount
#             print(f"{amount} Withdrawal successful! New balance: ", self.balance)

#     def check_balance(self):
#         print(f"The Total balance is :", self.balance)


# p = BankAccount("Bilal Ahmad", 100334)
# print(p.accountHolder, p.balance)

# p.deposit(100000)
# p.withdraw(10000)



# p.check_balance()

# 5. Employee Salary Tracker
# 🎯 Objective:
# Track employee details and salary.

# 🧱 Class: Employee
# name, position, salary

# 🔧 Methods:
# display_info() → Show employee details.

# update_salary(amount) → Increase salary by given amount.

# annual_salary() → Calculate yearly salary.


# class Employee:
#     def __init__(self, name, position, salary):
#         self.name = name
#         self.position = position
#         self.salary = salary
    
#     def update_salary(self, amount):
#         self.salary += amount
#         print("Your new Salary is :", self.salary)

#     def annual_salary(self):
#         salary = self.salary
#         print("The annual salary is :", salary * 12)

#     def display_info(self):
#         print("Employee Name: ", self.name)
#         print("Employee position: ", self.position)

       



# emp = Employee("Bilal Abbass", "CEO", 200000)

# emp.display_info()
# emp.update_salary(20000)
# emp.annual_salary()



# 6. Movie Ticket Booking
# 🎯 Objective:
# Simulate ticket booking for a movie.

# 🧱 Class: MovieTicket
# movie_name, price, available_tickets

# 🔧 Methods:
# book_ticket(quantity) → Reduce available tickets.

# cancel_ticket(quantity) → Increase available tickets.

# check_availability() → Show tickets left.

class MovieTicket:
    def __init__(self, movie_name, price, available_tickets):
        self.movie_name = movie_name
        self.price = price
        self.available_tickets = available_tickets
    
    def book_ticket(self,quantity):
        if quantity <= self.available_tickets:
            self.available_tickets -= quantity
            print(f"{quantity} ticket(s) booked for {self.movie_name} movie")
            print(f"The total price: {self.price * quantity}")
        else:
            print("No enough tickets available")
    def cancel_ticket(self,quantity):
        self.available_tickets += quantity
        print(f"{quantity} No of tickets cancelled! Total tickets: {self.available_tickets}")
    
    def check_availability(self):
        print(f"The available tickets for {self.movie_name} : {self.available_tickets}")
         
        
        


ticket = MovieTicket('PK', 560, 99)

ticket.check_availability()
ticket.book_ticket(8)
ticket.cancel_ticket(2)
