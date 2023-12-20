from tkinter import *
from tkinter import ttk
from tkinter import messagebox 

window = Tk()
window.title("tkinter training window")
window.geometry("500x500")
output = StringVar()

def clicked():
    messagebox.showinfo(
        title="display clicked",
        message="the login user name is " + output.get(),
    )



icon = PhotoImage(file="icon_1.png")
themed_label = Label(window,text="display").pack()
#themed_label1 = ttk.Label(window,text="picture").pack()
#btn_1 = Button (window,text="window_bin", command= Button).place(x=150,y=150)
# userlbl = ttk.Entry(window,text = "user name").pack()
useName = ttk.Entry(window, textvariable=output).pack()

Btn = ttk.Button(window, text="login",command=clicked).pack(anchor= CENTER)

# # ScrolledText = StringVar()

# def checkbox_Clicked():
#     messagebox.showinfo(
#         title = "hello world",
#         message= "the selected programming language is {}".format(selected.get())
#     )
# def radio_clicked():
#     messagebox.showinfo(
#         title= " selected program",
#         message= "the selected programming language is {}".format(selected_radio.get())
#     )
# def combobox_clicked(event):
#     messagebox.showinfo(
#         title= "selected Language",
#         message= "The selected language is %s" % selected_combobox.get()
#     )
# def getText():
#     messagebox.showinfo(
#         title='hello world!',
#         message=st.get("1.0", END)
#     )


# lang1 = ttk.Checkbutton(window,text='python', command=checkbox_Clicked, variable=selected, onvalue='python selected',offvalue='python not selected').pack()
# lang2 = ttk.Checkbutton(window,text='javascript', command=checkbox_Clicked, variable=selected, onvalue='javascript selected',offvalue='javascript not selected').pack()

# r1 = ttk.Radiobutton (window,text='python', value='pyton',command=radio_clicked, variable=selected_radio).pack()
# r2 = ttk.Radiobutton (window,text='java',value='java' ,command=radio_clicked, variable=selected_radio).pack()
# r3 = ttk.Radiobutton (window,text='javascript', value='javascript',command=radio_clicked, variable=selected_radio).pack()

# language = ttk.Combobox(window,width=25,height=10,textvariable=selected_combobox)

# language['values'] = (
#     'python' , 'java', 'javascript', 'golang', 'reacts'
# )

# language.current(0)
# language.bind('<<ComboboxSelected>>',combobox_clicked)
# language.pack()


# st = scrolledtext.ScrolledText(window,width = 50, height = 5)
# st.pack(side = LEFT)
# #btn = ttk.Button(window,text="getData",command=getText).pack()






window.mainloop()