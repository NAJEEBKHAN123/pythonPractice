# 2. BMI Calculator (Body Mass Index)/
# Use Case: Health apps use BMI to check body fitness levels.





# ************** BMI FORMULA ***********

# BMI = (weight) / (height) sqr 2


# weight_kg = float(input("Enter your body weight in Kg: "))
# height_m = float(input("Enter your body height in meter: "))

# bmi = weight_kg / height_m ** 2

# print(f"Your BMI is: {bmi:.2f}")


# students = [
#     {"name": "Ali", "age": 20, "grade": "A"},
#     {"name": "Sara", "age": 22, "grade": "B"},
#     {"name": "Ahmed", "age": 19, "grade": "A+"}
# ]

# # Accessing data
# for student in students:
#     print(f"Name: {student['name']}, Age: {student['age']}, Grade: {student['grade']}")



# for i in range(1,11):
#     if i == 3:
#         continue
#     print(i)

# food_item = ['']



# product_list = [1122, 2234, 5993, 103, 9920, 7272]

# search_product = 103  

# for product in product_list:
#     print(product)
    
#     if product == search_product:
#         print(f"Product Found: {product}")
#         break
# else:
#     print("Product not found.")


# # CONTIUNE EXP 

# foodList = ["banana", 'orange', 'apple', 'kiwi', 'staberry']

# for list in foodList:

#     if list == 'apple':
#         continue
         
#     print(list)




# Question:
# Create a Python program that stores a list of product codes.

# Ask the user to enter a product code to search.

# Print all product codes one by one.

# If the entered code is found, print “Product Found!” and stop the loop.

# If the loop finishes without finding the product, print “Product Not Found!”.


# Product_list = [1122, 3344, 5566, 2244, 7766, 9988]

# print("Welcome to our Store")
# searchProduct =  int(input("Enter the Product code: "))

# for list in Product_list:
#     print(list)
    
#     res = Product_list[searchProduct]
#     if res:
#         print(list)
#         break
#     else:
#         print("does not found")
# else:
#     print('no product')

# Write a function check_even(num) that returns "Even" if the number is even, otherwise "Odd".
print("Check whatever the number is Even or Odd")

def check_even(num):
    if num % 2 == 0:
        print("Even number")
    else:
        print("Odd number")

   
num = int(input("Enter a number: "))

check_even(num)


# Write a function find_max(a, b) that returns the largest of two numbers.
print("Enter a numbers to find the largest number:")

def find_max(a, b):

    if a > b:
        return print("A is greater then B")
    else:
        print("B is greater then A")

num1 = int(input("Enter number in A: "))
num2 = int(input("Enter number in B: "))

find_max(num1, num2)


# Write a function square(num) that returns the square of a number.

print("Find a square of the number:")
def square(num):

    return print(f"The Squre of the {num} is {num ** 2}")
   
num = int(input("Enter a number: "))
square(num)



    

