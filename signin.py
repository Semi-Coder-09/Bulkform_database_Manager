import tkinter as tk
import mysql.connector
from tkinter import messagebox
from PIL import Image, ImageTk

def authenticate(username, password):
    db = mysql.connector.connect(host='127.0.0.1', user='root', password='Apr@2120', database='credential')
    cursor = db.cursor()

    query = "SELECT * FROM users WHERE username = %s AND password = %s"
    values = (username, password)
    cursor.execute(query, values)
    result = cursor.fetchone()

    cursor.close()
    db.close()

    if result:
        open_main_gui()
    elif username == "admin" and password == "admin123":
        import admin
        admin.open_admin()
    else:
        messagebox.showinfo("Authentication Failed", "Invalid username or password")

def open_main_gui():
    # Import bulkform here to avoid circular import
    import bulkform
    bulkform.open_main_gui()

def toggle_password_visibility():
    if password_entry['show'] == '*':
        password_entry.config(show='')
        show_password_button.config(text="Hide", image=hide_image)
    else:
        password_entry.config(show='*')
        show_password_button.config(text="Show", image=show_image)

def sign_in():
    username = username_entry.get()
    password = password_entry.get()
    authenticate(username, password)

# Create the sign-in page GUI
root = tk.Tk()
root.title("Sign In")
root.geometry("300x350")
root.configure(bg="black")

# Tech Mahindra Logo
logo_image = tk.PhotoImage(file="techm.png")  # Replace with the actual logo file path
logo_label = tk.Label(root, image=logo_image, bg="black")
logo_label.pack(pady=10)

# Username Label and Entry
username_label = tk.Label(root, text="Username:", fg="white", bg="black", font=("Balsamiq Sans", 12))
username_label.pack()

username_entry = tk.Entry(root, font=("Balsamiq Sans", 14))
username_entry.pack()

# Password Label, Entry, and Show/Hide Button
password_label = tk.Label(root, text="Password:", fg="white", bg="black", font=("Balsamiq Sans", 12))
password_label.pack()

password_frame = tk.Frame(root, bg="black")
password_frame.pack()

password_entry = tk.Entry(password_frame, show="*", font=("Balsamiq Sans", 13))
password_entry.pack(side=tk.LEFT)

# Load and scale the show/hide images
show_image = Image.open("eyeshow.png")
show_image = show_image.resize((16, 16), Image.ANTIALIAS)
show_image = ImageTk.PhotoImage(show_image)

hide_image = Image.open("eyehide.png")
hide_image = hide_image.resize((16, 16), Image.ANTIALIAS)
hide_image = ImageTk.PhotoImage(hide_image)

show_password_button = tk.Button(password_frame, image=show_image, command=toggle_password_visibility, bd=0, bg="black", width=20, height=20)
show_password_button.pack(side=tk.RIGHT, padx=5)

# Sign-In Button
sign_in_button = tk.Button(root, text="Sign In", command=sign_in, font=("Balsamiq Sans", 12), fg="red", bg="black", bd=10)
sign_in_button.pack(pady=10)

# Start the sign-in page
root.mainloop()