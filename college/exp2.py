import tkinter as tk
root = tk.Tk()
root.title("My First Tkinter Window")
root.geometry("500x500")
label = tk.Label(root,text = "Welcome to Tkinterr!", font=("Arial Black", 18))
label.pack(pady=20)
root.mainloop()