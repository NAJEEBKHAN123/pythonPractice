# Dictionary are used to store data values in key:value pairs.
# A dict is a the collection of ordered, changeable and do not allow to duplicate values.


person  = {
    "name" : "najeeb",
    "age" : 20,
}

# print(person["name"])
# print(person)

# methods 

# print(person.get('age'))
# print(person.keys())
# print(person.values())

# print(person.items())
# person.update({"age" : 32})
# person.update({"city" : "peshawar"})


# # person.pop('age')
# # person.clear()

# new_person = person.copy()
# print(new_person)








# ************************ sets ******************* 

# A sets are used to store mutiple items in a single varibale 
# or built-in python data type that store unordered , unindexed and unique item 


# fruits = {'apple', 'banana', 'cherry'}

# print(type(fruits))
# fruits.add('orange')

# fruits.remove('cherry')

# fruits.discard('cherry')




# print(fruits)


# set1 = {1,2,3,6,9}
# set2 = {3,5,7,1,5,6}


# # print(set1.union(set2))
# # print(set1.intersection(set2))
# # print(set1.difference(set2))

# set1.update(set2)
# print(set1)




# s = set()

# for i in range(8):
#     i = int(input(f"Enter a number: #{i + 1} "))
#     s.add(i)
# print(s)



# favLang = {}

# for i in range(4):
#     lang  = input(f"Enter you fav language #{i + 1}: ")
#     name = input(f"Enter your name # {i + 1} :")

#     # print(f"Your fav language is {lang} and your name is {name}")
#     favLang[name] = lang

#     print(favLang)

s = {8,7,4, 'harry'}

print(s)
