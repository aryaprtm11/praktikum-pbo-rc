import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def msg_berhasil():
    messagebox.showinfo('Login Successfull', 'Welcome, Autumn!')

def msg_reg():
    messagebox.showinfo('Registration Successfull', 'You have successfully registered')

def register():
    extra_window = tk.Toplevel()
    extra_window.title('Register')
    extra_window.geometry('300x150')
    
    uname = tk.Label(extra_window, text="Username: ")
    password = tk.Label(extra_window, text="Password: ")
    uname.place(x = 10, y = 10)
    password.place(x = 10, y = 40)

    entry1 = tk.Entry(extra_window)
    entry2 = tk.Entry(extra_window)
    entry1.place(x = 80, y = 13)
    entry2.place(x = 80, y = 43)
    
    button2 = ttk.Button(extra_window, text = 'Register', command = msg_reg)
    button2.place(x = 100, y = 80)

window = tk.Tk()
window.title('Login')
window.geometry('300x150')

uname = tk.Label(window, text="Username: ")
password = tk.Label(window, text="Password: ")
uname.place(x = 10, y = 10)
password.place(x = 10, y = 40)

entry1 = tk.Entry(window)
entry2 = tk.Entry(window)
entry1.place(x = 80, y = 13)
entry2.place(x = 80, y = 43)

button1 = ttk.Button(window, text = 'Login', command = msg_berhasil)
button2 = ttk.Button(window, text = 'Register', command = register)
button1.place(x = 100, y = 80)
button2.place(x = 100, y = 110)

window.mainloop()