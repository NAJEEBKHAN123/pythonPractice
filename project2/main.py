import random

n = random.randint(1,100)
a = -1
guesses = 1

while(a != n):
    a = int(input("Enter the number: "))
    
    if n > a:
        print("Heigher number please")
        guesses += 1
    elif n < a:
        print("Lower number please")
        guesses += 1
print(f"You have guess the {n} number correctly in {guesses} Attempt!")