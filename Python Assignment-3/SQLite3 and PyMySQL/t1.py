import sqlite3

# Connect to SQLite database 
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Create a table
cursor.execute('''
    CREATE TABLE IF NOT EXISTS student (
        id INTEGER PRIMARY KEY,
        name TEXT,
        age INTEGER
    )
''')

print("Database and table created successfully.")
conn.close()
