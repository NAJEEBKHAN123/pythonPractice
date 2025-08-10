# Beginner Python Project Ideas
# 1. Number Guessing Game

import random 


# computer = random.randint(1,100)
# guesses = 0

# print("I'm thinking of a number between 1 and 100. Can you guess it?")

# while computer != guesses:
#     try:
#         guess = int(input("Enter a number: "))
#         guesses += 1
#         if guess == computer:
#             print(f"congratulation you find that number which is {computer} in {guesses} attempt!")
#         elif guess > computer:
#             print("Low number please")
#         elif guess < computer:
#             print("heigher number please")
#         else:
#             print("provide a correct range number")
            
#     except ValueError:
#             print("Invalid input. Please enter a number.")



# 2. Simple Calculator

# def Calculator():
#     num1 = int(input("Enter first number: "))
#     num2 = int(input("Enter second number: "))
#     opr =  input("Enter any operator: ")
#     try:
#         if opr == '+':
#             print(num1 + num2)
#         elif opr == '-':
#             print(num1 - num2)
#         elif opr == '*':
#             print(num1 * num2)
#         elif opr == '/':
#             print(num1 / num2)
    
#     except ValueError:
#         print("Invalid Input! please enter a number and operator only")

# Calculator()


  
    # 3. To-Do List App (Console Version)/
def add_task():

    task = input("Enter your task: ").strip()
    if not task:
        print('Task cannot be empty')
        return
    with open('tasks.txt', 'a', encoding="utf-8") as f:
        f.write(task+ '\n')
    print(f"Task added: {task}")
add_task()


print("Listed data: ")

def view_task():
    with open('tasks.txt', 'r') as f:
      data =  f.read()
      print(data)

view_task()
   

