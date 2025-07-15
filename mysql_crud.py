import pymysql

# Connect to MySQL
conn = pymysql.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="testdb"
)
cursor = conn.cursor()

# Create
cursor.execute("INSERT INTO users (name, email) VALUES ('Asha', 'asha@example.com')")
conn.commit()
print("✅ User inserted")

# Read
cursor.execute("SELECT * FROM users")
results = cursor.fetchall()
print("📄 All users:")
for row in results:
    print(row)

# Update
cursor.execute("UPDATE users SET email = 'asha@newmail.com' WHERE name = 'Asha'")
conn.commit()
print("✏️ Email updated")

# Delete
cursor.execute("DELETE FROM users WHERE name = 'Asha'")
conn.commit()
print("❌ User deleted")

cursor.close()
conn.close()
print("✅ Done")
