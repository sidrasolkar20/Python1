# Exp08(Postlb01)
# Aim: Write a Python program to create entry widgets for entering user name and password and display entered text.
# Name: Sidra Solkar
# UIN:231P087
# Roll No.:43

import tkinter as tk

# Function to display the entered text
def display_entry():
    username = entry_username.get()
    password = entry_password.get()  
    
    label_result.config(text=f"Username: {username}\nPassword: {password}")

root = tk.Tk()
root.title("Username and Password Entry")

label_username = tk.Label(root, text="Username:")
label_username.pack(pady=5)

entry_username = tk.Entry(root)
entry_username.pack(pady=5)

label_password = tk.Label(root, text="Password:")
label_password.pack(pady=5)

entry_password = tk.Entry(root, show="*")
entry_password.pack(pady=5)

submit_button = tk.Button(root, text="Submit", command=display_entry)
submit_button.pack(pady=10)

label_result = tk.Label(root, text="Entered Username and Password will appear here")
label_result.pack(pady=10)

root.mainloop()
