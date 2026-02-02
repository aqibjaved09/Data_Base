
import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
)

cursor = conn.cursor()

# Create Data Base
cursor.execute("CREATE DATABASE IF NOT EXISTS contacts_db")
print ("Successfully DataBase Created\n")

# Use Which One Table Name In DataBase 
cursor.execute("USE contacts_db")

# After DataBase Created Tables 
cursor.execute("""CREATE TABLE IF NOT EXISTS student (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    grade VARCHAR(10),
    city VARCHAR(50)

)s
""")

# For 2nd Second Tab
'''cursor.execute("""CREATE TABLE IF NOT EXISTS fees (
    student_id INT PRIMARY KEY AUTO_INCREMENT,
    name VARCHAR(100) NOT NULL,
    age INT,
    grade VARCHAR(10),
    city VARCHAR(50)

)
""")'''

print("Successfully Table Created")

student_id = int(input("Enter Student ID: "))
name = input("Enter Customer Name: ")
age = int(input("Enter age:"))
grade = input("Enter Customer grade: ")
city = input("Enter city:")

# Insert the User Data 
cursor.execute("INSERT INTO student (student_id,name, age, grade, city) VALUES (%s, %s, %s, %s, %s)", 
               (student_id,name, age, grade, city))

print("Successfully Entered Data In Table")


# Fetch Table Data 
'''cursor.execute("SELECT * FROM student")
data = cursor.fetchall()'''


print(f"Output{cursor.execute}")

# Comment 
conn.commit()