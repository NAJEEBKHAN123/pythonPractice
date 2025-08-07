# FUNCTION DEFINATION

# the block of code that run for the specific purpose 

# or  

# A group of statement perform for a specific task

# def greet():         #function defination 
#     print("Hello this is function")

# greet() #function call 



# FUNCTION IS A ARGUMENTS 

# def greet(name):
#     print(f"Hello, {name} Good morning")

# greet("Ali")


# FUNCTION WITH RETURN
# def greet(name):
   
#     return (f"Hello, {name} Good morning")

# a = greet("Ali")
# print(a)

# FUNCTION WITH DEFAULT VALUE 

def greet(name, title="Thanks for you response!"):
    print(f"Hello, {name} Good morning", title)
   
    
greet("Ali", "Come to quicly!")