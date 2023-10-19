import tkinter as tk
from tkinter import scrolledtext  # Import the scrolledtext module

# Initialize a list to store tasks
tasks = []

# Function to add a task
def add_task():
    task = task_entry.get()
    date = date_entry.get()

    if task:
        if date:
            task = f"{task} (Due: {date})"
        tasks.append(task)  # Add the task to the list
        display_tasks()

    task_entry.delete(0, tk.END)
    date_entry.delete(0, tk.END)

# Function to display tasks
def display_tasks():
    task_text.delete(1.0, tk.END)  # Clear the existing text
    for i, task in enumerate(tasks, start=1):
        task_with_serial = f"{i}. [ ] {task}"  # [ ] represents an unchecked checkbox
        task_text.insert(tk.END, task_with_serial + '\n')

# Function to remove a task
def remove_task():
    cursor_pos = task_text.index(tk.CURRENT)
    line = cursor_pos.split(".")[0]
    tasks.pop(int(line) - 1)  # Remove the task from the list
    display_tasks()

# Create the main window
root = tk.Tk()
root.title("To-Do List")

# Create and configure the task entry field
task_entry = tk.Entry(root, width=30)
task_entry.pack(pady=10)

# Create and configure the date entry field
date_label = tk.Label(root, text="Due Date (DD/MM/YYYY):")
date_label.pack()
date_entry = tk.Entry(root, width=30)
date_entry.pack()

# Create and configure the "Add Task" button
add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack()

# Create a scrolled Text widget to display tasks
task_text = scrolledtext.ScrolledText(root, width=50, height=10)
task_text.pack(pady=10)

# Create a "Remove Task" button
remove_button = tk.Button(root, text="Remove Task", command=remove_task)
remove_button.pack()

# Configure the main window's size
root.geometry("700x600")

root.mainloop()
