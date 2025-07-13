import sqlite3

# Connect to existing database
conn = sqlite3.connect("students.db")
cursor = conn.cursor()

# Insert data
cursor.execute("INSERT INTO student (name, age) VALUES (?, ?)", ("Diya", 21))
conn.commit()

# Fetch data
cursor.execute("SELECT * FROM student")
rows = cursor.fetchall()

print("Student Records:")
for row in rows:
    print(row)

conn.close()
