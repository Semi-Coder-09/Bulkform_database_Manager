import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Connect to the database
db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Apr@2120',
    database='test'
)

def show_message(message):
    messagebox.showinfo("Message", message)

def insert_data_from_file():
    filename = input("Enter the path of the .txt file: ")

    # Create a cursor object to interact with the database
    cursor = db.cursor()

    # Open the file and read its contents
    with open(filename, 'r') as file:
        for line in file:
            # Split the line into sentences using newlines as separators
            sentences = line.strip().split('\n')
            for sentence in sentences:
                # Split the sentence into words using commas as separators
                words = sentence.strip().split(',')

                # Check if all the required data is present
                if len(words) != 5:
                    print("Invalid entry:", sentence)
                    continue

                # Check if the first two words contain only letters
                if not words[0].isalpha() or not words[1].isalpha():
                    print("Invalid entry:", sentence)
                    continue

                # Extract the words for further processing
                first_name = words[0]
                last_name = words[1]
                email = words[2]
                password = words[3]
                phone_number = words[4]

                # Check if the phone number is numeric
                if not phone_number.isnumeric():
                    print("Invalid entry:", sentence)
                    continue

                # Prepare the SQL query
                query = "INSERT INTO employee_data (emp_ID, f_name, l_name, email, password, phone) VALUES (%s, %s, %s, %s, %s, %s)"
                values = (None, first_name, last_name, email + "@techmahindra.com", password, phone_number)

                # Execute the query
                cursor.execute(query, values)

    # Commit the changes to the database
    db.commit()
    show_message(f"{cursor.rowcount} record(s) inserted")

    # Close the cursor
    cursor.close()

def delete_data():
    cur = db.cursor()

    e = input("Enter your Employee Email ID Name --> ")

    sql = "DELETE FROM employee_data WHERE email = %s"
    email = (e + '@techmahindra.com',)

    cur.execute(sql, email)
    db.commit()

    show_message(f"{cur.rowcount} record(s) deleted")

    cur.close()

def get_data():
    cur = db.cursor()

    a = input("Enter what you want to Show any column or type first name if you want to select a row --> ")
    b = input("Confirm the first name again --> ")

    if a == "emp_ID":
        sql = "SELECT emp_ID FROM employee_data"

    elif a == "f_name":
        sql = "SELECT f_name FROM employee_data"

    elif a == "l_name":
        sql = "SELECT l_name FROM employee_data"

    elif a == "email":
        sql = "SELECT email FROM employee_data"

    elif a == "password":
        sql = "SELECT password FROM employee_data"

    elif a == "phone":
        sql = "SELECT phone FROM employee_data"

    elif a == b:
        sql = "SELECT * FROM employee_data where f_name = %s"
        value = (b,)

    else:
        show_message("Input Correct credentials")
        return

    cur.execute(sql, value if a == b else None)
    result = cur.fetchall()

    if not result:
        show_message("No Record found.")
    else:
        show_message(f"{len(result)} record(s) fetched")
        for x in result:
            print(x)

    cur.close()

def update_data():
    cur = db.cursor()

    a = input("Enter what you want to change --> ")
    e = input("Enter your Employee Email ID Name --> ")
    n = input("Enter your New data --> ")

    if a == "emp_ID":
        sql = "UPDATE test.employee_data set emp_ID = %s WHERE email = %s "
        value = (n, e + '@techmahindra.com')

    elif a == "f_name":
        sql = "UPDATE test.employee_data set f_name = %s WHERE email = %s "
        value = (n, e + '@techmahindra.com')

    elif a == "l_name":
        sql = "UPDATE test.employee_data set l_name = %s WHERE email = %s "
        value = (n, e + '@techmahindra.com')

    elif a == "email":
        sql = "UPDATE test.employee_data set email = %s WHERE email = %s "
        value = (n + '@techmahindra.com', e + '@techmahindra.com')

    elif a == "password":
        sql = "UPDATE test.employee_data set password = %s WHERE email = %s "
        value = (n, e + '@techmahindra.com')

    elif a == "phone":
        sql = "UPDATE test.employee_data set phone = %s WHERE email = %s "
        value = (n, e + '@techmahindra.com')

    else:
        show_message("Input Correct credentials")
        return

    cur.execute(sql, value)
    db.commit()

    show_message(f"{cur.rowcount} record(s) Updated")

    cur.close()

root = tk.Tk()
root.title("Employee Management System")

# ... Rest of the code ...

# Insert Data Button
insert_data_button = tk.Button(form_frame, text="Insert Data", font=('Balsamiq Sans', 12), command=insert_data_from_file)
insert_data_button.pack(pady=10)

# Delete Data Button
delete_data_button = tk.Button(form_frame, text="Delete Data", font=('Balsamiq Sans', 12), command=delete_data)
delete_data_button.pack(pady=10)

# Get Data Button
get_data_button = tk.Button(form_frame, text="Get Data", font=('Balsamiq Sans', 12), command=get_data)
get_data_button.pack(pady=10)

# Update Data Button
update_data_button = tk.Button(form_frame, text="Update Data", font=('Balsamiq Sans', 12), command=update_data)
update_data_button.pack(pady=10)

root.mainloop()

# Close the database connection
db.close()