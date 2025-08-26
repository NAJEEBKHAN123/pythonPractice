# bank_system.py

import streamlit as st
from abc import ABC, abstractmethod
from datetime import datetime


# -------------------------------
# Abstract Account Class
# -------------------------------
class Account(ABC):
    def __init__(self, acc_number, holder_name, balance=0):
        self.__acc_number = acc_number
        self.__holder_name = holder_name
        self.__balance = balance
        self.__transactions = []

    @abstractmethod
    def account_type(self):
        pass

    # Encapsulation
    def deposit(self, amount):
        self.__balance += amount
        self.__transactions.append(f"{datetime.now()}: Deposited {amount}")

    def withdraw(self, amount):
        if amount <= self.__balance:
            self.__balance -= amount
            self.__transactions.append(f"{datetime.now()}: Withdrew {amount}")
            return "Withdraw successful"
        else:
            return "Insufficient balance"

    def transfer(self, amount, other_account):
        if amount <= self.__balance:
            self.withdraw(amount)
            other_account.deposit(amount)
            self.__transactions.append(
                f"{datetime.now()}: Transferred {amount} to {other_account.get_acc_number()}"
            )
            return "Transfer successful"
        else:
            return "Insufficient balance"

    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        return self.__transactions

    def get_acc_number(self):
        return self.__acc_number

# -------------------------------
# Savings and Current Accounts
# -------------------------------
class SavingsAccount(Account):
    def account_type(self):
        return "Savings"

    def calculate_interest(self):
        # Optional: 5% interest
        return self.get_balance() * 0.05

class CurrentAccount(Account):
    def account_type(self):
        return "Current"

    def calculate_interest(self):
        return 0

# -------------------------------
# Bank Class
# -------------------------------
class Bank:
    def __init__(self):
        self.accounts = {}

    def create_account(self, acc_number, holder_name, acc_type):
        if acc_number in self.accounts:
            return "Account already exists"
        if acc_type.lower() == "savings":
            self.accounts[acc_number] = SavingsAccount(acc_number, holder_name)
        else:
            self.accounts[acc_number] = CurrentAccount(acc_number, holder_name)
        return f"{acc_type} account created successfully!"

    def get_account(self, acc_number):
        return self.accounts.get(acc_number)

    def deposit(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            account.deposit(amount)
            return f"Deposited {amount} successfully!"
        return "Account not found"

    def withdraw(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            return account.withdraw(amount)
        return "Account not found"

    def transfer(self, from_acc, to_acc, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if not sender or not receiver:
            return "One or both accounts not found"
        return sender.transfer(amount, receiver)

    def view_balance(self, acc_number):
        account = self.get_account(acc_number)
        if account:
            return account.get_balance()
        return "Account not found"

    def view_transactions(self, acc_number):
        account = self.get_account(acc_number)
        if account:
            return account.get_transactions()
        return "Account not found"

# -------------------------------
# Streamlit UI
# -------------------------------
bank = Bank()
st.title("🏦 Bank Management System")

menu = ["Create Account", "Deposit", "Withdraw", "Transfer", "View Balance", "View Transactions"]
choice = st.sidebar.selectbox("Menu", menu)

# -------------------------------
# Menu Options
# -------------------------------
if choice == "Create Account":
    st.subheader("Create a New Account")
    with st.form(key="create_form"):
        acc_number = st.text_input("Account Number")
        name = st.text_input("Account Holder Name")
        acc_type = st.selectbox("Account Type", ["Savings", "Current"])
        submit = st.form_submit_button("Create Account")
        if submit:
            st.success(bank.create_account(acc_number, name, acc_type))

elif choice == "Deposit":
    st.subheader("Deposit Money")
    with st.form(key="deposit_form"):
        acc_number = st.text_input("Account Number")
        amount = st.number_input("Amount", min_value=0.0)
        submit = st.form_submit_button("Deposit")
        if submit:
            st.success(bank.deposit(acc_number, amount))

elif choice == "Withdraw":
    st.subheader("Withdraw Money")
    with st.form(key="withdraw_form"):
        acc_number = st.text_input("Account Number")
        amount = st.number_input("Amount", min_value=0.0)
        submit = st.form_submit_button("Withdraw")
        if submit:
            st.success(bank.withdraw(acc_number, amount))

elif choice == "Transfer":
    st.subheader("Transfer Money")
    with st.form(key="transfer_form"):
        from_acc = st.text_input("From Account Number")
        to_acc = st.text_input("To Account Number")
        amount = st.number_input("Amount", min_value=0.0)
        submit = st.form_submit_button("Transfer")
        if submit:
            st.success(bank.transfer(from_acc, to_acc, amount))

elif choice == "View Balance":
    st.subheader("View Account Balance")
    acc_number = st.text_input("Account Number")
    if st.button("Check Balance"):
        balance = bank.view_balance(acc_number)
        st.write(f"Balance: {balance}")

elif choice == "View Transactions":
    st.subheader("View Transactions")
    acc_number = st.text_input("Account Number")
    if st.button("Show Transactions"):
        transactions = bank.view_transactions(acc_number)
        if transactions != "Account not found":
            st.table(transactions)
        else:
            st.error(transactions)
