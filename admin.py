import tkinter as tk
from tkinter import messagebox
import mysql.connector

# Database configuration
db = mysql.connector.connect(
    host='127.0.0.1',
    user='root',
    password='Apr@2120',
    database='credential'
)

# Function to add data to the database
def add_data():
    username = username_entry.get()
    password = password_entry.get()

    # Validate input
    if not username or not password:
        messagebox.showerror("Error", "Please enter both username and password.")
        return

    try:
        cursor = db.cursor()

        # Insert the data into the database
        query = "INSERT INTO users (username, password) VALUES (%s, %s)"
        values = (username, password)
        cursor.execute(query, values)

        # Commit the changes to the database
        db.commit()

        # Display success message
        messagebox.showinfo("Success", "Data added successfully.")

        # Clear the input fields
        username_entry.delete(0, tk.END)
        password_entry.delete(0, tk.END)

    except mysql.connector.Error as error:
        # Handle database errors
        messagebox.showerror("Database Error", str(error))
        db.rollback()

    finally:
        # Close the database connection
        cursor.close()

# Function to delete data from the database
def delete_data():
    username = username_entry.get()

    # Validate input
    if not username:
        messagebox.showerror("Error", "Please enter a username.")
        return

    try:
        cursor = db.cursor()

        # Delete the data from the database
        query = "DELETE FROM users WHERE username = %s"
        value = (username,)
        cursor.execute(query, value)

        # Commit the changes to the database
        db.commit()

        if cursor.rowcount == 0:
            messagebox.showinfo("No Data", "No data found with the provided username.")
        else:
            # Display success message
            messagebox.showinfo("Success", "Data deleted successfully.")

        # Clear the input field
        username_entry.delete(0, tk.END)

    except mysql.connector.Error as error:
        # Handle database errors
        messagebox.showerror("Database Error", str(error))
        db.rollback()

    finally:
        # Close the database connection
        cursor.close()

# Function to display existing data
def display_data():
    try:
        cursor = db.cursor()

        # Retrieve all data from the database
        query = "SELECT * FROM users"
        cursor.execute(query)

        data = cursor.fetchall()

        if not data:
            messagebox.showinfo("No Data", "No data found in the database.")
        else:
            # Display the data in a messagebox
            messagebox.showinfo("Data", "\n".join([f"Username: {row[0]}, Password: {row[1]}" for row in data]))

    except mysql.connector.Error as error:
        # Handle database errors
        messagebox.showerror("Database Error", str(error))

    finally:
        # Close the database connection
        cursor.close()

# Function to change password
def change_password():
    username = username_entry.get()
    old_password = old_password_entry.get()
    new_password = new_password_entry.get()

    # Validate input
    if username and old_password and new_password:
        try:
            cursor = db.cursor()

            # Check if the provided username and old password match a record in the database
            query = "SELECT * FROM users WHERE username = %s AND password = %s"
            values = (username, old_password)
            cursor.execute(query, values)

            data = cursor.fetchone()

            if not data:
                messagebox.showerror("Invalid Credentials", "Incorrect username or old password.")
            else:
                # Update the password in the database
                update_query = "UPDATE users SET password = %s WHERE username = %s"
                update_values = (new_password, username)
                cursor.execute(update_query, update_values)
                db.commit()

                messagebox.showinfo("Success", "Password changed successfully.")

                # Clear the input fields
                username_entry.delete(0, tk.END)
                old_password_entry.delete(0, tk.END)
                new_password_entry.delete(0, tk.END)

        except mysql.connector.Error as error:
            # Handle database errors
            messagebox.showerror("Database Error", str(error))
            db.rollback()

        finally:
            # Close the database connection
            cursor.close()

    else:
        messagebox.showerror("Error", "Please enter username, old password, and new password.")

# Create the main GUI window
root = tk.Tk()
root.title("Tech Mahindra Admin")
root.geometry("450x400")
root.configure(bg="black")

# Header
header_frame = tk.Frame(root, bg="black")
header_frame.pack()

# Tech Mahindra label
tech_mahindra_label = tk.Label(header_frame, text="Tech Mahindra", font=("Balsamiq Sans", 20), fg="red", bg="black")
tech_mahindra_label.pack(pady=(10, 0))

# Admin label
admin_label = tk.Label(header_frame, text="Admin", font=("Balsamiq Sans", 12), fg="red", bg="black")
admin_label.pack(pady=(0, 10))

# Frame for data entry fields
entry_frame = tk.Frame(root, bg="black")
entry_frame.pack()

# Username label and entry field
username_label = tk.Label(entry_frame, text="Username:", font=("Balsamiq Sans", 12), fg="white", bg="black")
username_label.grid(row=0, column=0, pady=5)

username_entry = tk.Entry(entry_frame, font=("Balsamiq Sans", 12), fg="red", bg="black")
username_entry.grid(row=0, column=1, pady=5)

# Password label and entry field
password_label = tk.Label(entry_frame, text="Password:", font=("Balsamiq Sans", 12), fg="white", bg="black")
password_label.grid(row=1, column=0, pady=5)

password_entry = tk.Entry(entry_frame, show="*", font=("Balsamiq Sans", 12), fg="red", bg="black")
password_entry.grid(row=1, column=1, pady=5)

# Buttons frame
button_frame = tk.Frame(root, bg="black")
button_frame.pack()

# Add data button
add_button = tk.Button(button_frame, text="Add Data", command=add_data, font=("Balsamiq Sans", 12), fg="white", bg="black")
add_button.grid(row=0, column=0, padx=5, pady=10)

# Delete data button
delete_button = tk.Button(button_frame, text="Delete Data", command=delete_data, font=("Balsamiq Sans", 12), fg="white", bg="black")
delete_button.grid(row=0, column=1, padx=5, pady=10)

# Display data button
display_button = tk.Button(button_frame, text="Display Data", command=display_data, font=("Balsamiq Sans", 12), fg="white", bg="black")
display_button.grid(row=0, column=2, padx=5, pady=10)

# Frame for password change fields
password_frame = tk.Frame(root, bg="black")
password_frame.pack()

# Old password label and entry field
old_password_label = tk.Label(password_frame, text="Old Password:", font=("Balsamiq Sans", 12), fg="white", bg="black")
old_password_label.grid(row=0, column=0, pady=5)

old_password_entry = tk.Entry(password_frame, show="*", font=("Balsamiq Sans", 12), fg="red", bg="black")
old_password_entry.grid(row=0, column=1, pady=5)

# New password label and entry field
new_password_label = tk.Label(password_frame, text="New Password:", font=("Balsamiq Sans", 12), fg="white", bg="black")
new_password_label.grid(row=1, column=0, pady=5)

new_password_entry = tk.Entry(password_frame, show="*", font=("Balsamiq Sans", 12), fg="red", bg="black")
new_password_entry.grid(row=1, column=1, pady=5)

# Change password button
change_password_button = tk.Button(password_frame, text="Change Password", command=change_password, font=("Balsamiq Sans", 12), fg="white", bg="black")
change_password_button.grid(row=2, columnspan=2, padx=5, pady=10)

# Start the GUI main loop
root.mainloop()
