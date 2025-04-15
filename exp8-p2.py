# Exp08(Postlb02)
# Aim: Write a Python GUI password protected program
# Name: Sidra Solkar
# UIN:231P087
# Roll No.:43
import tkinter as tk
from tkinter import messagebox

PASSWORD = "12345"

def verify_password():
    entered_password = entry_password.get()  
    
    if entered_password == PASSWORD:
        messagebox.showinfo("Access Granted", "You have successfully logged in!")
        show_main_window() 
    else:
        messagebox.showerror("Access Denied", "Incorrect Password!")

def show_main_window():
    login_window.withdraw()  
    
    main_window = tk.Tk()
    main_window.title("Main Window")
    
    label_main = tk.Label(main_window, text="Welcome to the main program!")
    label_main.pack(pady=20)

    exit_button = tk.Button(main_window, text="Exit", command=main_window.quit)
    exit_button.pack(pady=10)

    main_window.mainloop()

login_window = tk.Tk()
login_window.title("Password Protected Login")

label_username = tk.Label(login_window, text="Username:")
label_username.pack(pady=10)

entry_username = tk.Entry(login_window)
entry_username.pack(pady=5)

label_password = tk.Label(login_window, text="Password:")
label_password.pack(pady=10)

entry_password = tk.Entry(login_window, show="*")
entry_password.pack(pady=5)

submit_button = tk.Button(login_window, text="Submit", command=verify_password)
submit_button.pack(pady=20)

login_window.mainloop()
