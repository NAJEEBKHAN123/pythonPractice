import streamlit as st
from abc import ABC, abstractmethod
from datetime import datetime
from decimal import Decimal
import sqlite3
import json
from typing import List, Optional, Tuple

# ================================
# Database Setup
# ================================
class DatabaseManager:
    def __init__(self, db_name="bank.db"):
        self.db_name = db_name
        self.init_db()

    def init_db(self):
        """Initialize database tables"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            
            # Accounts table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS accounts (
                    acc_number TEXT PRIMARY KEY,
                    holder_name TEXT NOT NULL,
                    pin TEXT NOT NULL,
                    balance REAL NOT NULL DEFAULT 0,
                    acc_type TEXT NOT NULL,
                    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
                )
            ''')
            
            # Transactions table
            cursor.execute('''
                CREATE TABLE IF NOT EXISTS transactions (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    acc_number TEXT NOT NULL,
                    transaction_type TEXT NOT NULL,
                    amount REAL NOT NULL,
                    description TEXT,
                    related_account TEXT,
                    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP,
                    FOREIGN KEY (acc_number) REFERENCES accounts (acc_number)
                )
            ''')
            
            conn.commit()
            conn.close()
            return True
        except sqlite3.Error as e:
            print(f"Database initialization error: {e}")
            return False

    def execute_query(self, query, params=(), fetch=False):
        """Execute SQL query with error handling"""
        try:
            conn = sqlite3.connect(self.db_name)
            cursor = conn.cursor()
            cursor.execute(query, params)
            
            if fetch:
                result = cursor.fetchall()
            else:
                result = cursor.rowcount  # Return number of affected rows
            
            conn.commit()
            conn.close()
            return result
        except sqlite3.Error as e:
            print(f"Database error: {e}")
            return -1  # Return -1 for error

    def get_account(self, acc_number):
        """Get account details"""
        result = self.execute_query(
            "SELECT * FROM accounts WHERE acc_number = ?", 
            (acc_number,), 
            fetch=True
        )
        return result[0] if result else None

    def create_account(self, acc_number, holder_name, pin, balance, acc_type):
        """Create new account"""
        try:
            # First check if account already exists
            if self.account_exists(acc_number):
                return False, "Account already exists"
                
            result = self.execute_query(
                "INSERT INTO accounts (acc_number, holder_name, pin, balance, acc_type) VALUES (?, ?, ?, ?, ?)",
                (acc_number, holder_name, pin, float(balance), acc_type)
            )
            
            if result == 1:  # 1 row affected means success
                return True, "Account created successfully"
            else:
                return False, "Failed to create account"
                
        except Exception as e:
            print(f"Create account error: {e}")
            return False, f"Error creating account: {e}"

    def update_balance(self, acc_number, new_balance):
        """Update account balance"""
        result = self.execute_query(
            "UPDATE accounts SET balance = ? WHERE acc_number = ?",
            (float(new_balance), acc_number)
        )
        return result == 1  # Return True if 1 row was updated

    def add_transaction(self, acc_number, transaction_type, amount, description="", related_account=None):
        """Add transaction record"""
        result = self.execute_query(
            "INSERT INTO transactions (acc_number, transaction_type, amount, description, related_account) VALUES (?, ?, ?, ?, ?)",
            (acc_number, transaction_type, float(amount), description, related_account)
        )
        return result == 1

    def get_transactions(self, acc_number, limit=100):
        """Get transaction history for account"""
        result = self.execute_query(
            "SELECT * FROM transactions WHERE acc_number = ? ORDER BY timestamp DESC LIMIT ?",
            (acc_number, limit),
            fetch=True
        )
        return result if result != -1 else []

    def account_exists(self, acc_number):
        """Check if account exists"""
        result = self.execute_query(
            "SELECT 1 FROM accounts WHERE acc_number = ?",
            (acc_number,),
            fetch=True
        )
        return bool(result)

# ================================
# Abstract Account Class (Updated)
# ================================
class Account(ABC):
    def __init__(self, acc_number, holder_name, pin, balance=0, db_manager=None):
        self.__acc_number = acc_number
        self.__holder_name = holder_name
        self.__pin = pin
        self.__balance = Decimal(str(balance))
        self.db_manager = db_manager or DatabaseManager()

    @abstractmethod
    def account_type(self):
        pass

    # PIN check
    def check_pin(self, pin):
        return self.__pin == pin

    # Deposit
    def deposit(self, amount):
        amount = Decimal(str(amount))
        if amount <= 0:
            return False, "Deposit amount must be positive"
        
        self.__balance += amount
        # Update database
        if self.db_manager.update_balance(self.__acc_number, float(self.__balance)):
            self.db_manager.add_transaction(
                self.__acc_number, 
                "DEPOSIT", 
                float(amount), 
                "Cash deposit"
            )
            return True, "Deposit successful"
        return False, "Database update failed"

    # Withdraw
    def withdraw(self, amount):
        amount = Decimal(str(amount))
        if amount <= 0:
            return False, "Withdrawal amount must be positive"
        if amount <= self.__balance:
            self.__balance -= amount
            # Update database
            if self.db_manager.update_balance(self.__acc_number, float(self.__balance)):
                self.db_manager.add_transaction(
                    self.__acc_number, 
                    "WITHDRAWAL", 
                    float(amount), 
                    "Cash withdrawal"
                )
                return True, "Withdraw successful"
            return False, "Database update failed"
        else:
            return False, "Insufficient balance"

    # Transfer
    def transfer(self, amount, other_account):
        amount = Decimal(str(amount))
        if amount <= 0:
            return False, "Transfer amount must be positive"
        if amount <= self.__balance:
            self.__balance -= amount
            other_account.__balance += amount

            # Update both accounts in database
            if (self.db_manager.update_balance(self.__acc_number, float(self.__balance)) and 
                self.db_manager.update_balance(other_account.get_acc_number(), float(other_account.get_balance()))):

                # Record transactions for both accounts
                self.db_manager.add_transaction(
                    self.__acc_number, 
                    "TRANSFER_OUT", 
                    float(amount), 
                    f"Transfer to {other_account.get_acc_number()}",
                    other_account.get_acc_number()
                )
                self.db_manager.add_transaction(
                    other_account.get_acc_number(), 
                    "TRANSFER_IN", 
                    float(amount), 
                    f"Transfer from {self.__acc_number}",
                    self.__acc_number
                )
                return True, "Transfer successful"
            return False, "Database update failed"
        else:
            return False, "Insufficient balance"

    # Getters
    def get_balance(self):
        return self.__balance

    def get_transactions(self):
        transactions = self.db_manager.get_transactions(self.__acc_number)
        formatted_transactions = []
        for trans in transactions:
            formatted_transactions.append(
                f"{trans[6]}: {trans[2]} - {trans[3]} - Amount: ${trans[4]}"
            )
        return formatted_transactions

    def get_acc_number(self):
        return self.__acc_number

    def get_holder_name(self):
        return self.__holder_name

    def load_from_db(self):
        """Load account data from database"""
        account_data = self.db_manager.get_account(self.__acc_number)
        if account_data:
            self.__holder_name = account_data[1]
            self.__pin = account_data[2]
            self.__balance = Decimal(str(account_data[3]))
            return True
        return False

# ================================
# Savings and Current Accounts
# ================================
class SavingsAccount(Account):
    def account_type(self):
        return "Savings"

    def apply_interest(self):
        interest = self.get_balance() * Decimal("0.05")
        success, message = self.deposit(interest)
        if success:
            return interest
        return Decimal("0.00")

class CurrentAccount(Account):
    def account_type(self):
        return "Current"

    def calculate_interest(self):
        return Decimal("0.00")

# ================================
# Bank Class (Updated)
# ================================
class Bank:
    def __init__(self):
        self.db_manager = DatabaseManager()
        self.accounts = {}  # Cache for active accounts

    def create_account(self, acc_number, holder_name, pin, acc_type):
        if not acc_number or not holder_name or not pin:
            return False, "Account number, holder name, and PIN are required"
        
        # Use the improved create_account method from DatabaseManager
        success, message = self.db_manager.create_account(acc_number, holder_name, pin, 0, acc_type)
        
        if success:
            # Create account object only if database creation was successful
            if acc_type.lower() == "savings":
                account = SavingsAccount(acc_number, holder_name, pin, 0, self.db_manager)
            else:
                account = CurrentAccount(acc_number, holder_name, pin, 0, self.db_manager)
            
            self.accounts[acc_number] = account
            return True, f"{acc_type} account created successfully!"
        else:
            return False, message

    def get_account(self, acc_number):
        # Check cache first
        if acc_number in self.accounts:
            return self.accounts[acc_number]
        
        # Load from database
        account_data = self.db_manager.get_account(acc_number)
        if account_data:
            if account_data[4].lower() == "savings":
                account = SavingsAccount(acc_number, "", "", 0, self.db_manager)
            else:
                account = CurrentAccount(acc_number, "", "", 0, self.db_manager)
            
            if account.load_from_db():
                self.accounts[acc_number] = account
                return account
        
        return None

    def deposit(self, acc_number, amount):
        account = self.get_account(acc_number)
        if account:
            return account.deposit(amount)
        return False, "Account not found"

    def withdraw(self, acc_number, pin, amount):
        account = self.get_account(acc_number)
        if account:
            if account.check_pin(pin):
                return account.withdraw(amount)
            else:
                return False, "Invalid PIN"
        return False, "Account not found"

    def transfer(self, from_acc, to_acc, pin, amount):
        sender = self.get_account(from_acc)
        receiver = self.get_account(to_acc)
        if not sender:
            return False, "Sender account not found"
        if not receiver:
            return False, "Receiver account not found"
        if sender == receiver:
            return False, "Cannot transfer to the same account"
        if not sender.check_pin(pin):
            return False, "Invalid PIN"
        return sender.transfer(amount, receiver)

    def view_balance(self, acc_number, pin):
        account = self.get_account(acc_number)
        if account:
            if account.check_pin(pin):
                return True, account.get_balance()
            else:
                return False, "Invalid PIN"
        return False, "Account not found"

    def view_transactions(self, acc_number, pin):
        account = self.get_account(acc_number)
        if account:
            if account.check_pin(pin):
                return True, account.get_transactions()
            else:
                return False, "Invalid PIN"
        return False, "Account not found"

# ================================
# Streamlit App
# ================================
if "bank" not in st.session_state:
    st.session_state.bank = Bank()

st.title("🏦 Bank Management System with Database")

menu = ["Create Account", "Deposit", "Withdraw", "Transfer", "View Balance", "View Transactions", "Database Info"]
choice = st.sidebar.selectbox("Menu", menu)

# ---- Create Account ----
if choice == "Create Account":
    st.subheader("Create a New Account")
    with st.form(key="create_form"):
        acc_number = st.text_input("Account Number")
        name = st.text_input("Account Holder Name")
        pin = st.text_input("PIN (4 digits)", type="password", max_chars=4)
        acc_type = st.selectbox("Account Type", ["Savings", "Current"])
        submit = st.form_submit_button("Create Account")
        if submit:
            if len(pin) != 4 or not pin.isdigit():
                st.error("PIN must be exactly 4 digits")
            else:
                success, result = st.session_state.bank.create_account(acc_number, name, pin, acc_type)
                if success:
                    st.success(result)
                else:
                    st.error(result)

# ---- Deposit ----
elif choice == "Deposit":
    st.subheader("Deposit Money")
    with st.form(key="deposit_form"):
        acc_number = st.text_input("Account Number")
        amount = st.number_input("Amount", min_value=0.01, format="%.2f")
        submit = st.form_submit_button("Deposit")
        if submit:
            success, result = st.session_state.bank.deposit(acc_number, amount)
            if success:
                st.success(result)
            else:
                st.error(result)

# ---- Withdraw ----
elif choice == "Withdraw":
    st.subheader("Withdraw Money")
    with st.form(key="withdraw_form"):
        acc_number = st.text_input("Account Number")
        pin = st.text_input("PIN", type="password", max_chars=4)
        amount = st.number_input("Amount", min_value=0.01, format="%.2f")
        submit = st.form_submit_button("Withdraw")
        if submit:
            success, result = st.session_state.bank.withdraw(acc_number, pin, amount)
            if success:
                st.success(result)
            else:
                st.error(result)

# ---- Transfer ----
elif choice == "Transfer":
    st.subheader("Transfer Money")
    with st.form(key="transfer_form"):
        from_acc = st.text_input("From Account Number")
        to_acc = st.text_input("To Account Number")
        pin = st.text_input("Sender PIN", type="password", max_chars=4)
        amount = st.number_input("Amount", min_value=0.01, format="%.2f")
        submit = st.form_submit_button("Transfer")
        if submit:
            success, result = st.session_state.bank.transfer(from_acc, to_acc, pin, amount)
            if success:
                st.success(result)
            else:
                st.error(result)

# ---- View Balance ----
elif choice == "View Balance":
    st.subheader("View Account Balance")
    acc_number = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password", max_chars=4)
    if st.button("Check Balance"):
        success, result = st.session_state.bank.view_balance(acc_number, pin)
        if success:
            st.success(f"Account Balance: ${result:.2f}")
        else:
            st.error(result)

# ---- View Transactions ----
elif choice == "View Transactions":
    st.subheader("View Transactions")
    acc_number = st.text_input("Account Number")
    pin = st.text_input("PIN", type="password", max_chars=4)
    if st.button("Show Transactions"):
        success, result = st.session_state.bank.view_transactions(acc_number, pin)
        if success:
            if result:
                st.write("Transaction History:")
                for transaction in result:
                    st.write(transaction)
            else:
                st.info("No transactions found for this account")
        else:
            st.error(result)

# ---- Database Info ----
elif choice == "Database Info":
    st.subheader("Database Information")
    
    db_manager = DatabaseManager()
    
    # Show account count
    result = db_manager.execute_query("SELECT COUNT(*) FROM accounts", fetch=True)
    st.write(f"Total accounts: {result[0][0] if result and result != -1 else 0}")
    
    # Show transaction count
    result = db_manager.execute_query("SELECT COUNT(*) FROM transactions", fetch=True)
    st.write(f"Total transactions: {result[0][0] if result and result != -1 else 0}")
    
    # Show recent transactions
    st.write("Recent Transactions:")
    result = db_manager.execute_query(
        "SELECT acc_number, transaction_type, amount, timestamp FROM transactions ORDER BY timestamp DESC LIMIT 10", 
        fetch=True
    )
    if result and result != -1:
        for trans in result:
            st.write(f"{trans[3]}: {trans[0]} - {trans[1]} - ${trans[2]:.2f}")
    else:
        st.info("No transactions found")

# Add a reset button for development
if st.sidebar.button("Reset Database (Development)"):
    db_manager = DatabaseManager()
    db_manager.execute_query("DELETE FROM transactions")
    db_manager.execute_query("DELETE FROM accounts")
    st.session_state.bank = Bank()
    st.sidebar.success("Database reset complete")