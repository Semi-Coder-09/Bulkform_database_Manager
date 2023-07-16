import tkinter as tk
from tkinter import filedialog, messagebox
import insert_api
import show_api
import update_api
import delete_api

def open_main_gui():
    root.title("Main Project GUI")

def show_data():
    selected_column = column_selection.get()
    name = name_entry.get()
    data = show_api.show_data(selected_column, name)

def update_data():
    selected_column = update_column_selection.get()
    email = email_entry.get()
    new_data = new_data_entry.get()
    result = update_api.update_data(selected_column, email, new_data)
    show_message_box("Update Data", result)

def delete_data():
    email = delete_email_entry.get()
    result = delete_api.delete_data(email)
    show_message_box("Delete Data", result)

root = tk.Tk()
root.title("Bulk Data Entry")
root.configure(bg="black")

def show_message_box(title, message):
    messagebox.showinfo(title, message)

def upload_file():
    file_path = filedialog.askopenfilename()
    show_message_box("File Upload", f"Selected File: {file_path}")
    insert_api.insert_words_from_file(file_path)

# Create a Canvas
canvas = tk.Canvas(root, bg="black")
canvas.pack(side=tk.LEFT, fill=tk.BOTH, expand=True)

# Add a Scrollbar to the Canvas
scrollbar = tk.Scrollbar(root, orient=tk.VERTICAL, command=canvas.yview)
scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

# Configure the Canvas to use the Scrollbar
canvas.configure(yscrollcommand=scrollbar.set)
canvas.bind("<Configure>", lambda e: canvas.configure(scrollregion=canvas.bbox("all")))

# Create a Frame inside the Canvas
frame = tk.Frame(canvas, bg="black")
canvas.create_window((root.winfo_width() / 2, root.winfo_height() / 2), window=frame, anchor="center")

# Header
header_label_1 = tk.Label(frame, text="Tech Mahindra", font=("Balsamiq Sans", 20), fg="red", bg="black")
header_label_1.pack(pady=0)

header_label_2 = tk.Label(frame, text="Bulk Data Entry", font=("Balsamiq Sans", 24), fg="white", bg="black")
header_label_2.pack(pady=15)

# Upload Form
upload_form = tk.Frame(frame, bg="black")
upload_form.pack(pady=5)

upload_label = tk.Label(upload_form, text="Select a file to upload:", font=("Balsamiq Sans", 12), fg="white", bg="black")
upload_label.pack()

upload_button = tk.Button(upload_form, text="Upload File", font=("Balsamiq Sans", 12), fg="red", bg="black", bd=10, command=upload_file)
upload_button.pack(pady=5)

# Separator Line
separator1 = tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN, bg="white")
separator1.pack(fill=tk.X, pady=10)

# Show Data Form
show_data_form = tk.Frame(frame, bg="black")
show_data_form.pack(pady=5)

column_label = tk.Label(show_data_form, text="Select a column to show:", font=("Balsamiq Sans", 12), fg="white", bg="black")
column_label.pack()

column_selection = tk.StringVar()
column_dropdown = tk.OptionMenu(show_data_form, column_selection, "all","emp_ID", "f_name", "l_name", "email", "password", "phone","name")
column_dropdown.config(font=("Balsamiq Sans", 12), width=20, bg="black", fg="red", activebackground="black", activeforeground="red", bd=10)
column_dropdown.pack(pady=5)

name_label = tk.Label(show_data_form, text="Enter the name:", font=("Balsamiq Sans", 12), fg="white", bd=10, bg="black")
name_label.pack()

name_entry = tk.Entry(show_data_form, font=("Balsamiq Sans", 12), fg="red", bg="black", bd=10)
name_entry.pack(pady=5)

show_data_button = tk.Button(show_data_form, text="Show Data", font=("Balsamiq Sans", 12), fg="red", bg="black", bd=10, command=show_data)
show_data_button.pack(pady=5)

# Separator Line
separator2 = tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN, bg="white")
separator2.pack(fill=tk.X, pady=10)

# Update Data Form
update_data_form = tk.Frame(frame, bg="black")
update_data_form.pack(pady=5)

update_column_label = tk.Label(update_data_form, text="Select a column to update:", font=("Balsamiq Sans", 12), fg="white", bg="black")
update_column_label.pack()

update_column_selection = tk.StringVar()
update_column_dropdown = tk.OptionMenu(update_data_form, update_column_selection, "emp_ID", "f_name", "l_name", "email", "password", "phone")
update_column_dropdown.config(font=("Balsamiq Sans", 12), width=20, bg="black", fg="red", activebackground="black", activeforeground="red", bd=10)
update_column_dropdown.pack(pady=5)

email_label = tk.Label(update_data_form, text="Enter the email ID Name:", font=("Balsamiq Sans", 12), fg="white", bg="black")
email_label.pack()

email_entry = tk.Entry(update_data_form, font=("Balsamiq Sans", 12), fg="red", bg="black", bd=10)
email_entry.pack(pady=5)

new_data_label = tk.Label(update_data_form, text="Enter the new data:", font=("Balsamiq Sans", 12), fg="white", bg="black")
new_data_label.pack()

new_data_entry = tk.Entry(update_data_form, font=("Balsamiq Sans", 12), fg="red", bg="black", bd=10)
new_data_entry.pack(pady=5)

update_data_button = tk.Button(update_data_form, text="Update Data", font=("Balsamiq Sans", 12), fg="red", bg="black", bd=10, command=update_data)
update_data_button.pack(pady=5)

# Separator Line
separator3 = tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN, bg="white")
separator3.pack(fill=tk.X, pady=10)

# Delete Data Form
delete_data_form = tk.Frame(frame, bg="black")
delete_data_form.pack(pady=5)

delete_email_label = tk.Label(delete_data_form, text="Enter the email ID Name:", font=("Balsamiq Sans", 12), fg="white", bg="black")
delete_email_label.pack()

delete_email_entry = tk.Entry(delete_data_form, font=("Balsamiq Sans", 12), fg="red", bg="black", bd=10)
delete_email_entry.pack(pady=5)

delete_data_button = tk.Button(delete_data_form, text="Delete Data", font=("Balsamiq Sans", 12), fg="red", bg="black", bd=10, command=delete_data)
delete_data_button.pack(pady=5)

# Separator Line
separator4 = tk.Frame(frame, height=2, bd=1, relief=tk.SUNKEN, bg="white")
separator4.pack(fill=tk.X, pady=10)

# Function to center the bulk data entry page
def center_window(event):
    canvas.configure(scrollregion=canvas.bbox("all"))
    canvas.create_window((canvas.winfo_width() // 2, canvas.winfo_height() // 2), window=frame, anchor="center")

# Bind the center_window function to the Canvas resize event
canvas.bind("<Configure>", center_window)

# Update the geometry manager to expand the frame to fill the window
frame.pack(fill=tk.BOTH, expand=True)

root.mainloop()
