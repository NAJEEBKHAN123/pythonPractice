
import random
''''

1 for snake
-1 for water 
0 for gun

'''

print("Snake Water Gun game")
computer = random.choice([1,-1,0])

yourStr = input("Enter Snake, Water, or Gun: ")
youDic = {'Snake': 1, 'Water': -1, "Gun": 0}
reverserDic = {1: 'Snake', -1: 'Water', 0: 'Gun'}

print(f"You select {yourStr} and computer select {reverserDic[computer]}")

you = youDic[yourStr]

if (computer == you):
    print("Its a draw")
else:
    if (computer == 1 and you == -1 ):
        print("You lose!")
    elif(computer == -1 and you == 1):
        print('You Win!')
    elif(computer == 1 and you == 0):
        print("you Win!")
    elif(computer == -1 and you == 0):
        print("you lose!")
    elif(computer == 0 and you == 1):
        print("you lose!")
    elif(computer == 0 and you == -1):
        print("you win!")
    else:
        print("Something went wrong!")
    

