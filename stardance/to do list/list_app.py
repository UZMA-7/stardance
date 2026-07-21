import tkinter as tk
from tkinter import messagebox
import pyttsx3


# Load tasks from file
try:
    with open("tasks.txt", "r") as file:
        tasks = file.read().splitlines()
except FileNotFoundError:
    tasks = []


# Save tasks
def save_tasks():
    with open("tasks.txt", "w") as file:
        for task in tasks:
            file.write(task + "\n")


# Update list 
def update_list():
    task_list.delete(0, tk.END)

    for i, task in enumerate(tasks, start=1):
        task_list.insert(tk.END, f"{i}. {task}")


# Add task
def add_task():
    task = task_entry.get()

    if task:
        tasks.append(task)
        save_tasks()
        update_list()
        task_entry.delete(0, tk.END)

    else:
        messagebox.showwarning(
            "Warning",
            "Please enter a task."
        )


# Remove multiple tasks 
def remove_task():
    selected = task_list.curselection()

    if selected:
        # Delete from the end so indexes don't change
        for index in reversed(selected):
            tasks.pop(index)

        save_tasks()
        update_list()

    else:
        messagebox.showwarning(
            "Warning",
            "Select at least one task."
        )


# Read tasks aloud 
def read_tasks():
    if not tasks:
        messagebox.showinfo(
            "Tasks",
            "You have no tasks."
        )
        return

    engine = pyttsx3.init()

    text = "Your tasks are: "

    for task in tasks:
        text += task + ". "

    engine.say(text)
    engine.runAndWait()


# Create window 
window = tk.Tk()

window.title("My To-Do List")
window.geometry("450x550")


# Title
title = tk.Label(
    window,
    text="TO-DO LIST",
    font=("Arial", 22, "bold")
)

title.pack(pady=10)


# Task list 
task_list = tk.Listbox(
    window,
    width=40,
    height=15,
    font=("Arial", 12),
    selectmode=tk.MULTIPLE
)

task_list.pack(pady=10)


# Task input
task_entry = tk.Entry(
    window,
    width=35,
    font=("Arial", 12)
)

task_entry.pack(pady=5)


# Buttons 
add_button = tk.Button(
    window,
    text="Add Task",
    width=15,
    command=add_task
)

add_button.pack(pady=5)


remove_button = tk.Button(
    window,
    text="Remove Selected",
    width=15,
    command=remove_task
)

remove_button.pack(pady=5)


read_button = tk.Button(
    window,
    text="Read Tasks ❗",
    width=15,
    command=read_tasks
)

read_button.pack(pady=5)


exit_button = tk.Button(
    window,
    text="Exit",
    width=15,
    command=window.destroy
)

exit_button.pack(pady=5)


# Display saved tasks
update_list()


# To start the app
window.mainloop()