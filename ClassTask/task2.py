# class Teacher:
#     def __init__(self, name, age, teacher_id, course:list, department):
#         self.name = name
#         self.age = age
#         self.teacher_id = teacher_id
#         self.course = list(course)
#         self.department = department
    
#     def add_course(self, new_course):
#         self.course.append(new_course)
        
#     def remove_course(self, course_remove):
#         if course_remove in self.course:
#             self.course.remove(course_remove)
        
#     def display(self):
#         print("Name:", self.name)
#         print("Age:", self.age)
#         print("Teacher ID:", self.teacher_id)
#         print("Courses:", self.course)
#         print("Department:", self.department)
    
    
# s1 = Teacher("Alice", 30, "T001", ["Math", "Physics"], "Science")
# # s2 = Teacher("ali khan", 30, "T044", ["Pak", "Isa"], "Social Studies")

# s1.add_course("Chemistry")
# s1.display()
# # s2.display()


# class Book:
#     def __init__(self, title, author, year):
#         self.title = title
#         self.author = author
#         self.year = year
    
#     def display(self):
#         print("Title:", self.title)
#         print("Author:", self.author)
#         print("Year:", self.year)
    
    
# for i in range(3):
#     title = input("Enter book title: ")
#     author = input("Enter book author: ")
#     year = input("Enter book year: ")

#     book = Book(title, author, year)
#     book.display()
    


# class Teacher:
    
#     def __init__(self, name, subjects, experience):
#         self.name = name
#         self.subjects = subjects
#         self.experience = experience
    
    
#     def display(self):
#         print("Name:", self.name)
#         print("Subjects:", self.subjects)
#         print("Experience:", self.experience, "years")
    
    
#     def get_subjects_by_id(self, subject_id):
#         return self.subjects[subject_id]
    
# subjects = [
#     {'id': 0, 'name': "Math"},
#     {'id': 1, 'name': "Science"},
#     {'id': 1, 'name': "Biology"},
#     {'id': 1, 'name': "English"}
# ]
# teacher1 = Teacher("John Doe", subjects = subjects)
# teacher1.display()

# print("******Now printing subjects by ID********")
# print("Get subject by ID: ",teacher1.get_subjects_by_id(2)) 
# print(type(teacher1.get_subjects_by_id(2)))  
