# 1. Number Guessing Game 2.0
# import random

# def guessing_number():
#     guesses = 0
#     computer = random.randint(1,100)

#     while True:
#        user_input = int(input("Enter a number: "))


#        guesses += 1
#        if user_input == computer:
#            print(f"Guess the number in {guesses} attempt")
#            return True
       
#        elif user_input > computer:
#            print("Too high please guess low!")
        
#        elif user_input < computer:
#            print("Too low please guess high!")
        
#        else:
#            print("invalid input!")
           
# guessing_number()


# 2. To-Do List (Save to File)


# import os

# def add_task():
#     name = input("Enter the task name: ").strip()
#     if not name.strip():
#         print("Task name cannot be empty.")
#         return
    
#     if os.path.exists("tasks.txt"):
#         with open("tasks.txt", 'r') as file:
#             tasks = file.readlines()
#             if name + '\n' in tasks:
#                 print("Task already exists.")
#                 return
#             else:
#                 print("Task does not exist, adding it now.")
#     else:
#         print("No tasks file found, creating a new one.")

#     with open("tasks.txt", 'a') as file:
#         file.write(name + '\n')
#         print(f"Task {name} added successfully!")
    
    
# def view_tasks():
#     if os.path.exists("tasks.txt"):
#         with open("tasks.txt") as file:
#             tasks = file.readlines()

#             if not tasks:
#                 print("No tasks found.")
#             else:
#                 print("Tasks:")
#                 for task in tasks:
#                     print(f"- {task.strip()}")
#                 else:
#                     print("End of tasks.")
#     else:
#         print("No tasks file found.")
           

# def delete_task():
#     name = input("Enter the task name to delete: ").strip()
#     if not name.strip():
#         print("Task name cannot be empty.")
#         return 
    
#     if os.path.exists("tasks.txt"):
#         with open("tasks.txt") as file:
#             tasks = file.readlines()
#             if name + '\n' not in tasks:
#                 print("Task does not exist.")
#                 return
#             else:
#                 print("Task exists, deleting it now.")

#                 with open('tasks.txt', 'w') as file:
#                     for task in tasks:
#                         if task.strip() != name:
#                             file.write(task)
#                 print(f"Task {name} deleted successfully!")
#     else:
#         print("No tasks file found, nothing to delete.")


# def main():
#     while True:
#         print("\nTo-Do List Menu:")
#         print("1. Add Task")
#         print("2. View Tasks")
#         print("3. Delete Task")
#         print("4. Exit")

#         choice = input("Enter your choice (1-4): ").strip()
#         if choice == '1':
#             add_task()
#         elif choice == '2':
#             view_tasks()
#         elif choice == '3':
#             delete_task()   
#         elif choice == '4':
#             print("Exiting the program. Goodbye!")
#             break       
#         else:
#             print("Invalid choice. Please try again.")
# if __name__ == "__main__":
#     main()  


# 3. Simple Calculator (With History)

# import os


# def add(a, b):
#     return a + b

# def subtract(a, b):
#     return a - b

# def multiply(a, b):
#     return a * b

# def divide(a, b):
#     if b == 0:
#         return "Error: Division by zero is not allowed."
#     return a / b

# def calculator():
#     while True:
#         print("\nSimple Calculator Menu:")
#         print("1. Add")
#         print("2. Subtract")
#         print("3. Multiply")
#         print("4. Divide")
#         print("5. View History")
#         print("6. Exit")

#         choice = input("Enter your choice (1-6): ").strip()
        
#         if choice == '1':
#             a = float(input("Enter first number: "))
#             b = float(input("Enter second number: "))
#             result = add(a, b)
#             print(f"Result: {result}")

#         elif choice == '2':
#             a = float(input("Enter first number: "))
#             b = float(input("Enter second number: "))
#             result = subtract(a, b)
#             print(f"Result: {result}")
#         elif choice == '3':
#             a = float(input("Enter first number: "))
#             b = float(input("Enter second number: "))
#             result = multiply(a, b)
#             print(f"Result: {result}")
#         elif choice == '4':
#             a = float(input("Enter first number: "))
#             b = float(input("Enter second number: "))
#             result = divide(a, b)
#             print(f"Result: {result}")

# calculator()


# 4. Rock, Paper, Scissors (Best of 5 Rounds)
# Instead of a single round, keep track of the score until one player wins 3 times.



# import random 



# def play_round():
#     user_wins = 0
#     computer_wins = 0
#     choices = ['rock', 'paper', 'scissors']
#     while user_wins < 3 and computer_wins < 3:

#         user_choice = input("Enter your choice (rock, paper, scissors): ").lower()

#         if user_choice not in choices:
#             print("Invalid choice. Please try again.")
#             continue  
        
#         computer_choice = random.choice(choices)

#         print(f"Computer chose: {computer_choice}")
#         print(f"You chose: {user_choice}")

#         if user_choice == computer_choice:
#             print("It's a tie!")

#         elif (user_choice == "rock" and computer_choice == "scissors") or \
#             (user_choice == "paper" and computer_choice == "rock") or \
#             (user_choice == "scissors" and computer_choice == "paper"):
        

#             print("You win!")
#             user_wins += 1
#         else:
#             print("Computer win!")
#             computer_wins += 1
        
#         print(f"Score: You {user_wins}, Computer {computer_wins}")

#     if user_wins == 3:
#          print("Congratulations! You won the best-of-5 series!")
#     elif computer_wins == 3:
#         print("The computer won the best-of-5 series!")
#     else:
#         print('something went wrong')
       

# if __name__ == '__main__':
#    play_round()




# 5. Password Generator

# import random
# import string

# def generate_password(length=12, use_special_chars=True):
#     characters = string.ascii_letters + string.digits
#     if use_special_chars:
#         characters += string.punctuation
#         password = ''.join(random.choice(characters) for _ in range(length))
#     else:
#         password = ''.join(random.choice(string.ascii_letters + string.digits) for _ in range(length))
#     return password
# def main():
#     while True:
#         try:
#             length = int(input("Enter the desired password length (default is 12): ") or 12)
#             use_special_chars = input("Include special characters? (yes/no, default is yes): ").strip().lower() in ['yes', 'y', '']
#             if length < 1:
#                 print("Password length must be at least 1 character.")
#                 continue
#             password = generate_password(length, use_special_chars)
#             print(f"Generated password: {password}")
#             break
#         except ValueError:
#             print("Invalid input. Please enter a valid number for the password length.")
# if __name__ == "__main__":
#     main()



# def isPrime(num):
#     """Check if a number is prime."""
#     if num <= 1:
#         return False
#     for i in range(2, num):
#         if num % i == 0:
#             return False
#     return True

# while True:
#     try:
#         num = int(input("Enter a number to check if it's prime: "))
#         if isPrime(num):
#             print(f"{num} is a prime number.")
#         else:
#             print(f"{num} is not a prime number.")
    
#     except ValueError:
#         print("Invalid input. Please enter a valid integer.")


# 6. Countdown Timer

# import time

# def countdown_timer(seconds, minutes=0, ):
#     total_seconds = seconds + (minutes * 60)
#     while total_seconds:
#         mins, secs = divmod(total_seconds, 60)
#         timer = f"{mins:02d}:{secs:02d}"
#         print(timer, end="\r")
#         time.sleep(1)
#         total_seconds -= 1

#     print("Time's up!")

# def main():
#         while True:
#             try:
#                 seconds = int(input("Enter the number of secnonds for the countdown: "))
#                 minutes = int(input("Enter the number of minutes for the countdown (default is 0): ") or 0)
#                 if seconds < 0 or minutes < 0:
#                     print("Please enter non-negative values for seconds and minutes.")
#                     continue
#                 countdown_timer(seconds, minutes)
#                 break
#             except ValueError:
#                 print("Invalid input. Please enter valid integers for seconds and minutes.")

# if __name__ == "__main__":  
#     main()
#     main()
#     countdown_timer(10, 0)  # Example usage: countdown from 10 seconds
#     countdown_timer(0, 1)   # Example usage: countdown from 1 minute
#     countdown_timer(0, 2)   # Example usage: countdown from 2 minutes
#     countdown_timer(30, 0)  # Example usage: countdown from 30 seconds
#     countdown_timer(0, 5)   # Example usage: countdown from 5 minutes


# 7. Dice Roller (Multiple Dice)

# import random

# def roll_dice(num_dice=1, num_sides=6):
#     """Roll multiple dice with a specified number of sides."""
#     results = []
#     for _ in range(num_dice):
#         result = random.randint(1, num_sides)
#         results.append(result)
#     return results
# def main():
#     while True:
#         try:
#             num_dice = int(input("Enter the number of dice to roll (default is 1): ") or 1)
#             num_sides = int(input("Enter the number of sides on each die (default is 6): ") or 6)   
#             if num_dice < 1 or num_sides < 2:
#                 print("Please enter a valid number of dice (at least 1) and sides (at least 2).")
#                 continue
#             results = roll_dice(num_dice, num_sides)
#             print(f"Rolled {num_dice} dice with {num_sides} sides: {results}")
#             break
#         except ValueError:
#             print("Invalid input. Please enter valid integers for the number of dice and sides.")
# if __name__ == "__main__":
#     main()
#     roll_dice(2, 6)

#8. Quiz Game

# Ask 5 questions and keep score.

# Show correct answers at the end.


import random

def quiz_game():
    questions = {
        "What is the capital of France?": "Paris",
        "What is 2 + 2?": "4",
        "What is the largest planet in our solar system?": "Jupiter",
        "What is the chemical symbol for water?": "H2O",
        "Who wrote 'To Kill a Mockingbird'?": "Harper Lee"
    }
    score = 0
    total_questions = len(questions)

    for question, answer in questions.items():
        user_answer = input(f"{question} ").strip()

        if user_answer.lower() == answer.lower():
            print("Correct! Well done.")
            score += 1
        else:
            print(f"Incorrect. The correct answer is: {answer}")
    
    print(f"\nYou scored {score} out of {total_questions}.")
    if score == total_questions:
        print("Congratulations! You answered all questions correctly!")
    elif score >= total_questions / 2:
        print("Good job! You passed the quiz.")
    else:
        print("Better luck next time! Keep practicing.")

if __name__ == "__main__":
    quiz_game()
