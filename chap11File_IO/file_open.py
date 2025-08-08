# f = open('demo.txt')
# data = f.read()
# print(data)
# f.close()

# it return same value bcz the rt default parameter in the open

# f = open('demo.txt', 'rt')
# data = f.read()
# print(data)
# f.close()

# with open statement 

# with open('demo.txt') as f:
#     data  = f.read()
#     print(data)

# it is best paractice when you write close after done it 
# but without the with statement you must write close


# APPEND THE TEXT 

# f = open('demo.txt', 'a')
# f.write("Im 22 year old! \n")



# with open('demo.txt') as f:
#     print(f.read())


# OVERWRITE EXISING 

# f = open('demo.txt', 'w')
# f.write("Im 22 year old! \n")



# with open('demo.txt') as f:
#     print(f.read())





# CREATING A NEW FILE

# f = open('myFile.txt', 'x')


with open('myFile.txt', 'a') as f:
    f.write('Hello this is me Najeeb i"m this .......')
