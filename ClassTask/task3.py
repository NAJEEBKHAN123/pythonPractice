# class BankAccount:
#     def __init__(self):
#         self.__balance = 0
        
#     def deposit(self, amount):
#         self.amount = amount
#         if amount > 0:
#             self.__balance += amount
#             print(f"Deposit amount successful : {amount}")
#             amount = self.__balance
#             print(f"Your total amount is: {amount}")
#         else:
#             print("Balance can't be negative")
        
#     def withdraw(self, amount):
#         self.amount = amount
#         if 0 < amount <= self.__balance:
#             self.__balance -= amount
#             print(f"Withdraw amount successful : {amount}")
        
#         else:
#             print("Insufficient Balance")
        
#     def get_balance(self):
#         return self.__balance
 
#     def display_balance(self):
#         print(f"Your current balance is : {self.__balance}")
    
    
# class SavingsAccount(BankAccount):
#     def __init__(self):
#         super().__init__()
#         self.interest_rate = 0.05 
    
#     def calculate_interest(self):
#         interest = self.get_balance() * self.interest_rate
#         print(f"Interest earned: {interest}")
#         return interest
    
# account = BankAccount()
# account.deposit(1000)
# # account.display_balance()
# account.withdraw(300)
# account.get_balance()
        
# account.display_balance()
        
      
            
            
# class Student:
#     def __init__(self):
#         self__grade = None
    
#     def set_grade(self, grade):
#         if 0 <= grade <= 100:
#             self.__grade = grade
#             print(f"Grade set to {grade}")
#         else:
#             print("Invalid grade. Enter grade between 0 and 100")
        
#     def get_grade(self):
#         return self.__grade
    
#     def isPassed(self):
#         if self.__grade >= 50:
#             print("Student has passed")
#             return True
#         else:
#             print("Student has failed")
#             return False
     
#     def display_grade(self):
        
#         print(f"student grade is : {self.__grade}")
        
        
            
# student = Student()

# student.set_grade(89)
# student.display_grade()
# student.isPassed()




# # Abstract Class
# class Payment():

  
#     def pay(self, amount):
#         """Abstract method - must be implemented in child classes"""
#         pass


# # Concrete Implementations
# class CreditCardPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Credit Card.")


# class CashPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using PayPal.")


# class BankTransferPayment(Payment):
#     def pay(self, amount):
#         print(f"Paid {amount} using Bank Transfer.")


# # Client code
# # def process_payment(payment: Payment, amount: int):
# #     payment.pay(amount)


# # Usage
# credit = CreditCardPayment()
# credit.pay(1000)

# bank = BankTransferPayment()
# bank.pay(5000)



class Payment:
    
    def pay():
        """Abstract method: Every subclesses must implement this"""
        pass
    

class CreditCardPayment(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using credit Card")
    
class Paypal(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Paypal card")

class CashMethod(Payment):
    def pay(self, amount):
        print(f"Paid {amount} using Cash method")
    

credit = CreditCardPayment()
credit.pay(1000)

paypal = Paypal()
paypal.pay(5000)
    
cash = CashMethod()
cash.pay(9000)
    