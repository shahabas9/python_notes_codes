from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from tkinter import scrolledtext
from tkinter import Menu
import os

window = Tk()
window.title("tkinter training window")
window.geometry("500x500")
selected = StringVar()
selected_radio = StringVar()
selected_combobox = StringVar()


def save_file():
    dir = os.getcwd()
    print(dir)
    path = os.path.join(os.getcwd(),"notepad.txt")
    file = open(path,"a")
    file.write(st.get("1.0",END))
    file.close()
    messagebox.showinfo(
    title= "Message Box" , 
    message="Created and saved successfully!!!"
     )
def open_file():
     dir = os.getcwd()
     path = os.path.join(os.getcwd(),"notepad.txt")
     file = open("notepad.txt","r")
     content = file.read()
     st.insert(END,content)
    

#menu:
menuContent = Menu(window)


file = Menu(menuContent,tearoff=False)
menuContent.add_cascade(label='File',menu=file)
file.add_command(label ="new")
file.add_command(label ="open", command= open_file)
file.add_command(label ="save",command= save_file)         
file.add_command(label ="exit")
file.add_separator()



view = Menu(menuContent,tearoff=False)
menuContent.add_cascade(label='view',menu=view)


edit = Menu(menuContent,tearoff=False)
menuContent.add_cascade(label='edit',menu=edit)
edit.add_command(label ="find")
edit.add_command(label ="replace")
edit.add_command(label ="select all")
edit.add_command(label ="time/date")
edit.add_separator()




st = scrolledtext.ScrolledText(window,width = 200, height = 100)
st.pack(side = LEFT)





window.config(menu=menuContent)










window.mainloop()




