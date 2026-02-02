
import mysql.connector

# Data Base Name 
DB_NAME = "test" 

# Sql Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="test"
)

# Check Database 
print("Connected\n")

# Must Add Cursor Connection
cursor = conn.cursor()

order_id = int(input("Enter Order ID: "))
customer_name = input("Enter Customer Name: ")
location = input("Enter Location:")
 
# Insert the User Data 
cursor.execute("INSERT INTO tblorder (order_id,customer_name, location) VALUES (%s, %s, %s)", 
               (order_id, customer_name, location))

conn.commit()

# Added New Data in Column Name 1st Table 
'''cursor.execute("INSERT INTO tblorder (order_id,customer_name, location) VALUES (25,'Developer', 'Multan')")
conn.commit()'''



# 1. Table First
cursor.execute("SELECT * FROM tblorder")
print("Table 1:")
for row in cursor.fetchall():
    print(row)

# 2. Table Second  
cursor.execute("SELECT * FROM customer_data")
print("\nTable 2:")
for row in cursor.fetchall():
    print(row)


# Close
cursor.close()
conn.close()