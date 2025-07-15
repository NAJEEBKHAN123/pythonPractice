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


set1 = {1,2,3,6,9}
set2 = {3,5,7,1,5,6}


# print(set1.union(set2))
# print(set1.intersection(set2))
# print(set1.difference(set2))

set1.update(set2)
print(set1)


