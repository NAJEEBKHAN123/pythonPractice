# 🎯 Task Name: Student Marks Manager

# students = []
# marks = []

# for i in range(5):
#     student_name = input("Enter student name: ")
#     student_marks = int(input("Enter marks: "))

#     students.append(student_name)
#     marks.append(student_marks)

# # Displaying the students and their marks
# print("\n Student marks:")

# for i in range(5):
#     print(f"{students[i]} : {marks[i]}")


# highest_marks = max(marks)
# position = marks.index(highest_marks)

# print(f"\nHighest marks: {highest_marks} by {students[position]}")


# 📌 Practice Task:

# Create a list of your 5 favorite websites.
# favSites = ["Google", "YouTube", "Github", "Facebook", 'LinkedIn']

# favSites.append("Indeed")
# favSites.append("Stack Overflow")

# favSites.remove("Facebook")

# favSites.sort()


# print(favSites)

# ✅ Task Name: Favorite Movies List
# 🎯 Objective:

# Take names of 3 favorite movies from the user.

# Store them in a list.

# Display the list.

# Let the user remove one movie from the list.

# Show the updated list.

# movies = []



# for i in range(3):
#    movies_name = input(f"Enter you favorite movie #{i + 1} ")
#    movies.append(movies_name)

#    print("\nYour favorite movies are: ")
#    print(movies)

# # Removing a movie
# remove_movie = input("\nEnter the name of the movie you want to remove: ")
# if remove_movie in movies:
   
#    movies.remove(remove_movie)
#    print(f"\n{remove_movie} has been remove from you movies list :")
#    print("\n Updated favorite movies list: ")
#    print(movies)

# else:
#    print(f"\n{remove_movie} is not in you favorite movies list.")

#    print("\n Updated favorite movies list: ")
#    print(movies)


# ✅ Task: Shopping Cart (Simple List Practice)

# cart = []

# for i in range(3):
#     item = input(f"Enter item # {i + 1} for your shopping cart: ")
#     cart.append(item)
#     print(f"\n Your shopping cart items are: {cart}")

# # Removing an item
# remove_item = input("\nEnter the name of the item you want to remove from your cart: ")
# if remove_item in cart:
#     cart.remove(remove_item)
#     print(f"\n{remove_item} has been removed from your shopping cart. ")
#     print(f"\nUpdated shopping cart items: {cart}")

# else:
#     print(f"\n{remove_item} is not in your shopping cart.")
#     print(f"\nYour shopping cart items remain unchanged: {cart}")











# ********************* TUPLE *********************

# 🧩 Task Steps:
# Create a tuple called marks with these numbers:
# (85, 90, 75, 90, 60, 90, 70)

# Print how many times the mark 90 appears in the tuple.

# Print the index of the first time 75 appears.

# Try to change a mark (e.g. marks[0] = 95) and observe the error.

# Convert the tuple to a list and add a new mark: 88.
# Then convert it back to a tuple and print it.

# solution 
# marks = (85, 90, 75, 90, 60, 90, 70)

# print(marks.count(90))
# print(marks.index(75))
# marks[0] = 100

# marks_list = list(marks)


# marks_list.append(88)

# marks = tuple(marks_list)



# print(marks)


# ✅ Task: 📋 Student Record System (List + Tuple Practice)



# students = []

# for i in range(3):
#     studentName =  input(f"Enter student name #{i + 1}: ")
#     studentMarks = int(input(f"Enter marks for {studentName}: "))
#     studentAge = float(input(f"Enter student age for {studentName}: "))
   
#     student = (studentName, studentMarks, studentAge)
#     students.append(student)
    
# for student in students: 
#     print(f"\nStudent Name: {student[0]}, Marks: {student[1]}, Age: {student[2]}")


# students marks and then sorted it 

# students = []

# for i in range(3):
#     studentMarks = int(input(f"Enter marks of # {i + 1} : "))
#     students.append(studentMarks)

#     students.sort()
#     print(students)
