import mysql.connector

# connect to DB using container name as host
conn = mysql.connector.connect(
    host="mydb",
    user="root",
    password="root",
    database="mydb"
)

cursor = conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (id INT PRIMARY KEY AUTO_INCREMENT, name VARCHAR(50))")
cursor.execute("INSERT INTO users (name) VALUES ('Bestie')")
conn.commit()

cursor.execute("SELECT * FROM users")
for row in cursor.fetchall():
    print(row)

conn.close()

