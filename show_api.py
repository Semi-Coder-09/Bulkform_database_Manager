from tkinter import messagebox
import mysql.connector

def show_data(selected_column, name):
    db = mysql.connector.connect(host='127.0.0.1', user='root', password='Apr@2120', database='test')
    cur = db.cursor()

    if selected_column == "emp_ID":
        sql = "SELECT emp_ID FROM employee_data"
    elif selected_column == "f_name":
        sql = "SELECT f_name FROM employee_data"
    elif selected_column == "l_name":
        sql = "SELECT l_name FROM employee_data"
    elif selected_column == "email":
        sql = "SELECT email FROM employee_data"
    elif selected_column == "password":
        sql = "SELECT password FROM employee_data"
    elif selected_column == "phone":
        sql = "SELECT phone FROM employee_data"
    elif selected_column == "all":
        sql = "SELECT * FROM employee_data"
    elif selected_column == "name":
        sql = "SELECT * FROM employee_data WHERE f_name = %s"
        value = (name,)
    else:
        messagebox.showinfo("Invalid Column", "Please input correct credentials")
        return

    cur.execute(sql, value if selected_column == "name" else None)
    result = cur.fetchall()

    if not result:
        messagebox.showinfo("No Record Found", "No record found.")
    else:
        messagebox.showinfo("Records Fetched", f"{len(result)} record(s) fetched")
        data = "\n".join([str(row) for row in result])
        messagebox.showinfo("Data", data)

    cur.close()
    db.close()