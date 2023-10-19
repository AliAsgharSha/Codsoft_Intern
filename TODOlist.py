import tkinter as tk
from tkinter import scrolledtext

tasks = []

def add_task():
    task = task_entry.get()
    date = date_entry.get()

    if task:
        if date:
            task = f"{task} (Due: {date})"
        tasks.append(task)
        display_tasks()

    task_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

def display_tasks():
    task_text.delete(1.0, tk.END)
    for i, task in enumerate(tasks, start=1):
        task_with_serial = f"{i}. [ ] {task}"
        task_text.insert(tk.END, task_with_serial + '\n')

def remove_task():
    cursor_pos = task_text.index(tk.CURRENT)
    line = cursor_pos.split(".")[0]
    tasks.pop(int(line) - 1)  # Remove the task from the list
    display_tasks()

root = tk.Tk()
root.title("To-Do List")

task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

date_label = tk.Label(root, text="Due Date (DD/MM/YYYY):")
date_label.pack()
date_entry = tk.Entry(root, width=30)
date_entry.pack()

add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

task_text = scrolledtext.ScrolledText(root, width=50, height=10)
task_text.pack(pady=10)

remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

root.geometry("700x600")

root.mainloop()
