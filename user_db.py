
import mysql.connector
conn = mysql.connector.connect(
    host="localhost", 
    user="root",
    password="",   
)   
cursor = conn.cursor()  
# Create Data Base
cursor.execute("CREATE DATABASE IF NOT EXISTS user_authentication")
print ("Successfully DataBase Created\n")

cursor.execute("USE user_authentication")

# Table Created
cursor.execute("""CREATE TABLE IF NOT EXISTS users (
    id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(70) UNIQUE,
    password VARCHAR(100) 
)
""")

print("Successfully Table Created")

# We Use Loop For Register And Login

print(" 1. Register\n 2. Login\n 3. Exit")


    # That we Use 3 Entry to put Develope the Data

while True:
    choice = input(" Enter your choice (1/2/3): ")
    if choice == '1':
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Check if username already exists
        cursor.execute(" SELECT * FROM users WHERE username = %s", (username,))
        if cursor.fetchone():
            print(" Username already exists Please choose a different username.")
                
        # Use Else For Insert Data iF Data is Not Exist
        else:
            cursor.execute(" INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
            print(" Successfully Registered!")      
        conn.commit()
        
    elif choice == '2':
        username = input("Enter username: ")
        password = input("Enter password: ")

        # Verify user credentials
        cursor.execute(" SELECT * FROM users WHERE username = %s AND password = %s", (username, password))
        if cursor.fetchone():
            print(" Login successful!")
        else:
            print("Invalid username or password.....")

    elif choice == '3':
        print(" Exiting....")
        
        break
                    
    else:
        print("Invalid choice. Please try again...")        
        
# Connection Close
cursor.close()
conn.close()
    
