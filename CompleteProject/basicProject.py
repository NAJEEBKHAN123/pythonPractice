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
# def add_task():

#     task = input("Enter your task: ").strip()
#     if not task:
#         print('Task cannot be empty')
#         return
#     with open('tasks.txt', 'a', encoding="utf-8") as f:
#         f.write(task+ '\n')
#     print(f"Task added: {task}")
# add_task()


# print("Listed data: ")

# def view_task():
#     with open('tasks.txt', 'r') as f:
#       data =  f.read()
#       print(data)

# view_task()
   

# 4. Rock, Paper, Scissors Game

# import random

# def play_rock_paper_scissors():

#     """Play Rock, Paper, Scissors Game"""

#     choices = ['rock', 'paper', 'scissors']
    
#     while True:
#        user_choice = input("Enter you choice in (rock, paper, scissors): ").lower()

#        if user_choice in choices:
#            break
#        else:
#            print("Invalid choice! please enter a rock, paper or scissors")

#     computer_choice = random.choice(choices)

#     print(f"Your choice: {user_choice}")
#     print(f"Computer choice: {computer_choice}")

#     if computer_choice == user_choice:
#         print("It's a tie!")
    
#     elif user_choice == 'roce' and computer_choice == 'scissors' or \
#          user_choice == 'paper' and computer_choice == 'rock' or \
#          user_choice == 'scissors' and computer_choice == 'paper':
#         print("You win!")
#     else:
#         print("Computer win!")
    

# play_rock_paper_scissors()






# 5. Password Generator

# import random
# import string


# def generateRandomPassword(length):
     
#     characters = string.ascii_letters + string.digits + string.punctuation
#     random_string = "".join(random.choices(characters, k=length))
#     return random_string

# random_result = generateRandomPassword(14)
# print(f"Random password: {random_result}")

# 7. Dice Roller



# def rollingDice(sides=6):
#     return random.randint(1,sides)

# res =  rollingDice()
# print(f"You rolled a {res} on a 6-sided die.")

# 8. Weather App (Console)

# import requests

# city_name = "Karachi"
# api_key = 'f8ab698e9d5080de03c48e2b76897510'

# url = f'https://api.openweathermap.org/data/2.5/weather?q={city_name}&appid={api_key}&units=metric'

# response = requests.get(url) 

# if response.status_code == 200:
#     data = response.json()
#     print('Weather is: ', data['weather'][0]['description'])
#     print("Current temp:", data['main']['temp'])



# 9. Unit Converter

# Celsius/Fahrenheit
# def unitConverter():
    
#     inputVal = int(input("Enter temp in Celsius: "))
#     Fahrenheit  = (inputVal * 9/5) + 32
#     print(Fahrenheit)


# unitConverter()


# def unitConverter():
    
#     inputVal = int(input("Enter distence in KM: "))
#     miles = inputVal * 0.621371
#     print(miles)
   

# 6. Countdown Timer

# import time

# def countDown(t):
#     while t:
#         mins, secs = divmod(t, 60)
#         timer = f'{mins:02d}:{secs:02d}'
#         print(timer, end='\r')
#         time.sleep(1)
#         t -= 1
#     print("Time's Off")

# duration = int(input("Enter a countDown duration in seconds: "))
# countDown(duration)


# practice on Rock, Paper, Scissors game

import random

def play_game():
    """play Rock, Paper, Scissors game"""

    choices = ['rock', 'paper', 'scissors']

    while True:
        user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

        if user_choice in choices:
            break
        else:
            print("Invalid choice! please enter correct choice")
        
    computer_choice = random.choice(choices)

    print(f"Your choice: {user_choice}")
    print(f"Computer choice: {computer_choice}")

    if user_choice == computer_choice:
        print("it's tie!")
    
    elif (user_choice == 'rock' and computer_choice == 'scissors') or \
         (user_choice == 'paper' and computer_choice == 'rock') or \
         (user_choice == 'scissors' and computer_choice == 'paper'):
        print("You win!")
    else:
        print("Computer win!")

play_game()
            