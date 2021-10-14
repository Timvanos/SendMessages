import tkinter as tk

root = tk.Tk()

margin = 0.23

entry = tk.Entry(root)

entry.pack()

def insert_credentials():
    UserNameString = entry.get()
    print(UserNameString)

button_login = tk.Button(root, text="Login", command=insert_credentials)
button_login.pack()
root.mainloop()

