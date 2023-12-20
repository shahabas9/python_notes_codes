from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import Menu
import os
import sqlite3



window = Tk()
window.title("tkinter training window")
window.geometry("500x500")

conn = sqlite3.connect("for_training.db")





selected = StringVar()
selected_radio = StringVar()


selected_combobox = StringVar()
output = StringVar()

id = StringVar()
name = StringVar()
age = StringVar()
phoneno = StringVar()
email = StringVar()




def adduser():
    cursor_obj = conn.cursor()
    query = "INSERT INTO users (id, NAME, age, phoneno,email) VALUES (?, ?, ?, ?, ?)"
    values = (id.get(), name.get(), age.get(),phoneno.get(), email.get())  
    print(values)
    cursor_obj.execute(query,values)
    conn.commit()
    messagebox.showinfo(
        title="display clicked",
        message="user is added successfully"
    )

# def updateuser():
#     cursor_obj = conn.cursor()
#     query = "UPDATE users SET (id, NAME, age, phoneno,email) VALUES (?, ?, ?, ?, ?)"
#     values = (id.get(), name.get(), age.get(),phoneno.get(), email.get())  
#     #print(values)
#     cursor_obj.execute(query,values)
#     conn.commit()
#     messagebox.showinfo(
#         title="update sucessfully",
#         message="user is updated successfully"
#     )


def deleteuser(user_id):
    cursor_obj = conn.cursor()
    query = "DELETE FROM users WHERE id = ?"
    cursor_obj.execute(query, (user_id,))
    conn.commit()
    messagebox.showinfo(
        title="Deleted Successfully",
        message="User is deleted successfully"
    )
def getusers():
    conn = sqlite3.connect("for_training.db")
    cursor_obj = conn.cursor()
    query = "SELECT * FROM users"
    cursor_obj.execute(query)
    rows = cursor_obj.fetchall()
    conn.commit()
    return rows
rows = getusers()
messagebox.showinfo(
    title="fetch user",
    message="the data id: {}".format(rows)
     )

ent1 = ttk.Entry(window,textvariable= id).pack()
ent2 = ttk.Entry(window,textvariable= name).pack()
ent3 = ttk.Entry(window,textvariable= age).pack()
ent4 = ttk.Entry(window,textvariable= phoneno).pack()
ent5 = ttk.Entry(window,textvariable= email).pack()
btn1 =  ttk.Button(window,text='addusers',command= adduser).pack()
#btn2 =  ttk.Button(window,text='updateusers',command= updateuser).pack()
btn4 =  ttk.Button(window,text='deleteusers',command= deleteuser).pack()
btn5 =  ttk.Button(window,text='getusers',command= getusers).pack()
window.mainloop()
conn.close()