import sqlite3 

DB_FILE = "contacts.db"

def get_connection():
    conn = sqlite3.connect(DB_FILE)
    return conn

def init_db():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS contacts (
               
                   id INTEGER PRIMARY KEY AUTOINCREMENT,
                   name TEXT,
                   age INTEGER,
                   rollNo INTEGER,
                   description TEXT
                   
                   )
    """)
    
    conn.commit()
    conn.close()


def add_contacts(name, age, rollNo, description):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""
        INSERT INTO contacts (name, age, rollNo, description) 
        VALUES (?, ?, ?, ?)
    """, (name.strip(), age, rollNo, description.strip()))
    
    conn.commit()     
    conn.close()   
    print("contact added!") 

init_db()


add_contacts("Najee", 20, 200, "this is my first entry")  

