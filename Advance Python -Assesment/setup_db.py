import pymysql

try:
    conn = pymysql.connect(host='localhost', user='root', password='')
    cursor = conn.cursor()

    # Create DB
    cursor.execute("CREATE DATABASE IF NOT EXISTS billing_db")
    cursor.execute("USE billing_db")

    # Create Table
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS bills (
            id INT AUTO_INCREMENT PRIMARY KEY,
            bill_no VARCHAR(10),
            customer_name VARCHAR(100),
            phone VARCHAR(15),
            total DECIMAL(10, 2),
            bill_text TEXT
        )
    """)

    conn.commit()
    print("Database and table created successfully!")

except Exception as e:
    print("Error:", e)

finally:
    conn.close()
