from tkinter import messagebox
import mysql.connector

def delete_data(email):
    db = mysql.connector.connect(host='127.0.0.1', user='root', password='Apr@2120', database='test')
    cur = db.cursor()

    sql = "DELETE FROM test.employee_data WHERE email = %s"
    value = (email + '@techmahindra.com',)
    cur.execute(sql, value)
    db.commit()
    messagebox.showinfo("Records Deleted", f"{cur.rowcount} record(s) deleted")

    cur.close()
    db.close()