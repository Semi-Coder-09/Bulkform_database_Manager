from tkinter import messagebox
import mysql.connector

def update_data(selected_column, email, new_data):
    db = mysql.connector.connect(host='127.0.0.1', user='root', password='Apr@2120', database='test')
    cur = db.cursor()

    if selected_column == "emp_ID":
        sql = "UPDATE test.employee_data SET emp_ID = %s WHERE email = %s"
        value = (new_data, email + '@techmahindra.com')
    elif selected_column == "f_name":
        sql = "UPDATE test.employee_data SET f_name = %s WHERE email = %s"
        value = (new_data, email + '@techmahindra.com')
    elif selected_column == "l_name":
        sql = "UPDATE test.employee_data SET l_name = %s WHERE email = %s"
        value = (new_data, email + '@techmahindra.com')
    elif selected_column == "email":
        sql = "UPDATE test.employee_data SET email = %s WHERE email = %s"
        value = (new_data + '@techmahindra.com', email + '@techmahindra.com')
    elif selected_column == "password":
        sql = "UPDATE test.employee_data SET password = %s WHERE email = %s"
        value = (new_data, email + '@techmahindra.com')
    elif selected_column == "phone":
        sql = "UPDATE test.employee_data SET phone = %s WHERE email = %s"
        value = (new_data, email + '@techmahindra.com')
    else:
        messagebox.showinfo("Invalid Column", "Please input correct credentials")
        return

    cur.execute(sql, value)
    db.commit()
    messagebox.showinfo("Records Updated", f"{cur.rowcount} record(s) updated")

    cur.close()
    db.close()