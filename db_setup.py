import sqlite3

def setup_database():
    conn = sqlite3.connect('researchers.db')
    c = conn.cursor()
    
    c.execute('''CREATE TABLE IF NOT EXISTS researchers 
                 (name TEXT PRIMARY KEY, contribution TEXT)''')
    conn.commit()
    conn.close()

setup_database()
