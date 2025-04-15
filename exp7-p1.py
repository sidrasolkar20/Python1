#Postlab(01)
#Aim:Write a Python program to create, read, and delete data/task added from an SQLite database
# Name:Sidra Solkar
# UIN: 231P087
# Roll No.: 43
import sqlite3
import tkinter as tk
from tkinter import messagebox

conn = sqlite3.connect("tasks.db")
cursor = conn.cursor()

cursor.execute("""
CREATE TABLE IF NOT EXISTS tasks (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    task TEXT NOT NULL
)
""")
conn.commit()

def add_task():
    task = entry_task.get()
    if task:
        cursor.execute("INSERT INTO tasks (task) VALUES (?)", (task,))
        conn.commit()
        entry_task.delete(0, tk.END)  
        view_tasks() 
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

def view_tasks():
    listbox_tasks.delete(0, tk.END)
    cursor.execute("SELECT * FROM tasks")
    for row in cursor.fetchall():
        listbox_tasks.insert(tk.END, f"{row[0]}. {row[1]}") 

def delete_task():
    try:
        selected_task = listbox_tasks.get(listbox_tasks.curselection()) 
        task_id = selected_task.split(".")[0]  
        cursor.execute("DELETE FROM tasks WHERE id=?", (task_id,))
        conn.commit()
        view_tasks() 
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete!")
root = tk.Tk()
root.title("Task Manager")
root.geometry("400x400")
label = tk.Label(root, text="Enter Task:", font=("Arial", 12))
label.pack(pady=5)
entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=5)
btn_add = tk.Button(root, text="Add Task", command=add_task)
btn_add.pack(pady=5)
listbox_tasks = tk.Listbox(root, width=50, height=10)
listbox_tasks.pack(pady=10)
btn_delete = tk.Button(root, text="Delete Task", command=delete_task)
btn_delete.pack(pady=5)
btn_refresh = tk.Button(root, text="Refresh List", command=view_tasks)
btn_refresh.pack(pady=5)
view_tasks()
root.mainloop()
