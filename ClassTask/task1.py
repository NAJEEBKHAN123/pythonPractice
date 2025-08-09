# max_attempt = 3
# secure_password = "secure@123"

# while max_attempt > 0:
#     password = input("Enter your password: ")
#     if password == secure_password:
#         print("Login successfully!")
#         break
#     else:
#         max_attempt -= 1
#         if max_attempt == 0:
#             print("Your attempt is complete")
#         else:
#             print("Invalid crediential")
 




        
# count = 10

# while count >= 0:
#     if count == 5:
#         count -= 1
#         continue 
    
#     print(count)
#     count -= 1
    
# else:
#      print("Time's Up!")

    

# try:
#     num = int(input("Enter a number: "))
#     print(f"You entered: {num}")
# except ValueError:
#     print("Invalid input! Please enter a number.")

# try:
#     num1 = int(input("Enter a number: "))
#     num2 = int(input("Enter a number: "))
#     print(f"You entered: {num1/num2}")
# except ZeroDivisionError:
#     print("You can't divide a number by 0")

# num1 = int(input("Enter a number: "))
# num2 = int(input("Enter a number: "))
# print(f"You entered: {num1/num2}")


# try:
#     num1 = int(input("Enter a number: "))
#     print(num1)
# except Exception as e:
#             print("Please enter a number")


# print("Hey i'm inside finally")



# def check_finally():
#         try:
#             num1 = int(input("Enter a number: "))
#             print(num1)
#             return
#         except Exception as e:
#             print("Please enter a number")
#             return

#         finally:
#                print("Hey i'm inside finally")

# check_finally()

