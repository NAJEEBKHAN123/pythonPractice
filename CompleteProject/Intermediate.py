# 1. Expense Tracker (File version)

# import os

# FILE_NAME = 'expenses.txt'



# def add_expenses():
#     date = input("Enter date (YYYY-MM-DD): ")
#     description = input("Enter description: ")
#     amount = float(input("Enter amount: "))

#     with open(FILE_NAME, 'a') as file:
#         file.write(f"{date}, {description},  {amount} \n")
    
#     print("Expenses Added!")


# def view_expenses():
#     if not os.path.exists(FILE_NAME):
#         print("No expenses recorded yet.")
#         return
    
#     with open(FILE_NAME, "r") as file:
#         expenses = file.readlines()
    
#     total = 0
#     print("\nDate\t\tDescription\tAmount")
#     print("-"*40)
#     for expense in expenses:
#         expense = expense.strip()
#         if not expense:  
#             continue
        
#         parts = expense.split(",")
#         if len(parts) != 3:  
#             continue
        
#         date, description, amount = parts
#         print(f"{date}\t{description}\t${amount}")
#         total += float(amount)
    
#     print("-"*40)
#     print(f"Total: ${total:.2f}\n")

# while True:
#     print("1: Add Expense")
#     print("2: View Expense")
#     print("3: Exit")

#     choice = input("Enter an option: ")

#     if choice == '1':
#         add_expenses()

#     elif choice == '2':
#         view_expenses()

#     elif choice == '':
#         break
#     else:
#         print("Invalid choice! please enter correct one")


# 2. Personal Diary App
# Add daily notes with date & time.

# Save entries in a .txt or .json file.

# Add a search function to find past notes.

import os

FILE_NAME = 'diayapp.txt'


def diary_app():
    date = input("Enter date (YYYY-MM-DD): ")
    description = input("Enter description: ")

    with open(FILE_NAME, 'a') as file:
        file.write(f"{date}, {description}\n")
    
    print("note added!")


def search_note():
    if not os.path.exists(FILE_NAME):
        print("📭 No diary entries found!")
        return
    
    keyword = input("Enter keyword or data for search: ").lower()

    
    with open(FILE_NAME, 'r') as file:
       notes = file.readline()
    

    print("\nDate\t\tDescription")
    print('-'*40)
    found = False
    for note in notes:
        note = note.strip()

        if not note:
            continue
        parts = note.split(",", 1)
        if len(parts) != 2:  
            continue
        
        date, description = parts
        if keyword in date.lower() or keyword in description.lower():
         print(f"{date}\t{description}")
         found = True
       
    if not found:
        print('No matching notes found.')

while True:
    print("\n📓 Personal Diary App")
    print("1. Add Note")
    print("2. Search Notes")
    print("3. Exit")

    choice = input("Enter an option: ")

    if choice == "1":
        diary_app()
    elif choice == "2":
        search_note()
    elif choice == "3":
        print("👋 Goodbye!")
        break
    else:
        print("Invalid choice, try again!")





        






    






