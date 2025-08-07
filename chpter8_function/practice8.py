# Write a function that takes two numbers and returns their sum.


# def sum(a, b):
#     return print(a + b)

# sum(5,6)


# Create a function that takes a number and returns whether it is even or odd.


# def findNumber(a):
#     print(a)

# findNumber(5)
 


# Create a function that takes 2 numbers and an operator (+, -, *, /) and returns the result.
# def add(a,b):
#     return a + b

# def sub(a,b):
#     return a - b

# def mult(a,b):
#     return a * b

# def divi(a,b):
#     return a / b


# def calculator():
#     a = int(input("Enter your first number: "))
#     b = int(input("Enter your second number: "))
#     opr = input("Enter any operator of them (+, -, *, /): ")


#     if opr == "+":
#         print(add(a,b))
    
#     elif opr == "-":
#         print(sub(a,b))
    
#     elif opr == '*':
#         print(mult(a,b))

#     elif opr == '/':
#         print(divi(a,b))
        
#     else:
#         print("Your provided unsuported opr")


# calculator()
    




def resturant_system():
    print("We have mutiple food plan Like: ")
    print("1: Starter \n2: Main Course \n3: Dessert")

    take_input = int(input("Enter food plan from the above list: "))

    if take_input == 1:
        print("Starter Menu : Friesh & Sandwitch")
        user_input = input("Enter one of them: ")
        print(f"Your order is {user_input}")

    elif take_input == 2:
        print("Starter Menu : karahi & chawal")
        user_input = input("Enter one of them: ")
        print(f"Your order is {user_input}")

    elif take_input == 3:
        print("Starter Menu : karahi & chawal")
        user_input = input("Enter one of them: ")
        print(f"Your order is {user_input}")

    
    else:
        print("Your don't select any plan")



resturant_system()


