import tkinter as tk
from tkinter import messagebox
def login():
    if(userentry.get()=="Zulfi"):
        text = "Welcome "+userentry.get()
        messagebox.showinfo("Login Successful", text)
    else:
        text = "Invalid Username or password"
        messagebox.showwarning("Login Failed", text)
main = tk.Tk()
main.title("Login Form")
main.geometry("300x300")
userlabel = tk. Label(main, text="User Name:")
userlabel.grid(row=100,column=100,padx=100)
userentry = tk. Entry(main, width=10)
userentry.grid(row=101,column=100,padx=100)
passwordlabel = tk. Label(main, text="Password:")
passwordlabel.grid(row=102,column=100, padx=100)
passwordentry = tk.Entry(main, width=10,show="*")
passwordentry.grid(row=103,column=100, padx=100)
okbutton = tk.Button(main, text="Ok",command=login)
okbutton.grid(row=104,column=100,padx=100)
main.mainloop()
