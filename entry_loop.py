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

#conn = sqlite3.connect("for_training.db")

selected = StringVar()
selected_radio = StringVar()


selected_combobox = StringVar()
output = StringVar()

entr1 = []

for i in range(4):
    entry = Entry(window)
    entry.grid(row=0,column=i)
    entr1.append(entry)
window.mainloop()
#conn.close()
