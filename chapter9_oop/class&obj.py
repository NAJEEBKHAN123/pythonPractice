# class myClass: 
#     lang = "Python"
#     age = 20


# p1 = myClass()
# name = 'umar'
# print(name, p1.age, p1.lang)

# p2 = myClass()
# name = "Ali"
# print(name, p2.age, p2.lang)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def myFun(self):
        print(f"Hello {self.name} can i help you if you don't mind")





p1 = Person("ali", 20)

p1.myFun()
print(p1.name, p1.age)

