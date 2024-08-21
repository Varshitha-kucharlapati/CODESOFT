import tkinter as tk
from tkinter import messagebox
import json

tasks = []

def load_tasks(filename='tasks.json'):
    global tasks
    try:
        with open(filename, 'r') as file:
            tasks = json.load(file)
    except FileNotFoundError:
        tasks = []

def save_tasks(filename='tasks.json'):
    with open(filename, 'w') as file:
        json.dump(tasks, file)

def add_task():
    title = entry_title.get()
    description = entry_description.get()
    if title:
        task_id = len(tasks) + 1
        task = {
            'id': task_id,
            'title': title,
            'description': description,
            'completed': False
        }
        tasks.append(task)
        save_tasks()
        update_task_list()
    else:
        messagebox.showwarning("Input Error", "Title cannot be empty")

def update_task_list():
    listbox_tasks.delete(0, tk.END)
    for task in tasks:
        status = 'Completed' if task['completed'] else 'Not Completed'
        listbox_tasks.insert(tk.END, f"ID: {task['id']}, Title: {task['title']}, Status: {status}")

def mark_completed():
    try:
        selected_index = listbox_tasks.curselection()[0]
        task_id = tasks[selected_index]['id']
        for task in tasks:
            if task['id'] == task_id:
                task['completed'] = True
                break
        save_tasks()
        update_task_list()
    except IndexError:
        messagebox.showwarning("Selection Error", "No task selected")

# GUI setup
root = tk.Tk()
root.title("To-Do List")

frame = tk.Frame(root)
frame.pack(padx=10, pady=10)

entry_title = tk.Entry(frame, width=40)
entry_title.pack(pady=5)
entry_description = tk.Entry(frame, width=40)
entry_description.pack(pady=5)

button_add = tk.Button(frame, text="Add Task", command=add_task)
button_add.pack(pady=5)

listbox_tasks = tk.Listbox(frame, width=50, height=10)
listbox_tasks.pack(pady=5)

button_complete = tk.Button(frame, text="Mark as Completed", command=mark_completed)
button_complete.pack(pady=5)

load_tasks()
update_task_list()

root.mainloop()
