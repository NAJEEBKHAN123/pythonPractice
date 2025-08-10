from functools import reduce
# Square a Number

# lam = lambda x : x*x
# print(lam(4))


# Find Maximum of Two Numbers

# lam = lambda a, b : a if a > b else b
# print(lam(10,20))

# Check Even or Odd

# lam = lambda a : "Even" if a%2 == 0 else "Odd"
# print(lam(9))

# Map
# Square a List

# nums = [1,2,3,4,5,6,7]
# square_list = list(map(lambda x: x ** 2, nums))
# print(square_list)



# nums = [1,2,3,4,5,6,7,8]

# evenNum = list(filter(lambda x: x%2 == 0 , nums))
# print(evenNum)


# Filter Words Longer Than 5 Letters


# words = ["Hello", "how are you", 'im', "najeeb", "ullah", "what", 'is', 'this', ]


# res = list(filter(lambda x: len(x) > 5, words))
# print(res)


# Reduce

# Sum All Numbers


# nums = [1,2,3,4,5,6,7,8]

# res = reduce(lambda x,y: x+y, nums)
# print(res)


# Find Product of All Numbers

# nums = [1,2,3,4,5]

# res = reduce(lambda x,y: x*y, nums)
# print(res)

# Find Maximum in a List

# Use reduce() to find the largest number in a list.
 
# nums = [1,2,9,3,4,5]
 
# res = reduce(lambda a, b: a if a > b else b, nums)

# print(res)

# Intermediate-level tasks for lambda, map, filter, and reduce

students = [
    {"name": "Ali", "marks": 85},
    {"name": "Sara", "marks": 92},
    {"name": "Bilal", "marks": 45},
    {"name": "Umar", "marks": 7}
]

# Tasks:

# Use map() to extract only student names into a list.

# Use filter() to get only students who passed (marks ≥ 50).

# Use reduce() to calculate the total marks of all students.

# Use lambda with map() to add a new key "grade" based on marks.

# 1
# res = list(map(lambda student: student['name'], students))
# print(res)

# 2: 
# res = list(filter(lambda student: (student["marks"] > 50), students))
# print(res)

# nums = [1,2,3,4,5]
# 3
# res = reduce(lambda x,y: x*y, map(lambda s : s["marks"], students))
# print(res)


words = ["Apple", "banana", "Apple", "orange", "banana", "apple"]

# Tasks:

# Use map() and lambda to convert all words to lowercase.

# Use filter() to keep only words starting with "a".

# Use reduce() to create a dictionary with word counts.


# res = list(map(lambda x: x.lower(), words))
# print(res)

# res = list(map(lambda x: x.upper(), words))
# print(res)

# res = list(filter(lambda x: x.startswith('a'), words))
# print(res)

prices = [100, 250, 50, 80, 120]

# Use map() to apply a 10% discount to all prices.

# Use filter() to find products costing more than $100 after discount.

# Use reduce() to find the total cost of all discounted products.

# Use lambda to format the prices like "$100.00".


# res = list(map(lambda x: x + ( x * 10 / 100), prices))
# print(res)

# res = list(filter(lambda x: x if x > 100 else "", prices) )
# print(res)
