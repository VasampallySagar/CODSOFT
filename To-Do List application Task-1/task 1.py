import tkinter as tk
from tkinter import messagebox
from datetime import datetime
import time

counter = 1

def add_task():
    global counter
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(tk.END, f"{counter}. {task}")
        counter += 1
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def update_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        updated_task = entry_task.get()
        listbox_tasks.delete(task_index)
        listbox_tasks.insert(task_index, f"{task_index + 1}. {updated_task}")
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to update.")

def quit_app():
    root.destroy()

def display_time():
    current_time = time.strftime('%I:%M:%S %p')
    digital_clock.config(text=current_time)
    digital_clock.after(200, display_time)

def display_date():
    current_date = datetime.now().strftime('%A, %B %d, %Y')
    date_label.config(text=current_date)

root = tk.Tk()
root.title("To-Do List Application")
root.geometry("1000x1000")
root.configure(bg="#f2f2f2")

date_label = tk.Label(root, text="", font=("Arial", 14), bg="#f2f2f2")
date_label.pack(pady=10)
display_date()

frame_tasks = tk.Frame(root, bg="#f2f2f2")
frame_tasks.pack(pady=20)

listbox_tasks = tk.Listbox(frame_tasks, height=15, width=40)
listbox_tasks.pack(side=tk.LEFT, padx=20)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=40)
entry_task.pack(pady=10)
entry_task.focus()

button_add_task = tk.Button(root, text="Add Task", width=30, command=add_task, bg="light green",fg="black",font="arial")
button_add_task.pack(pady=5)

button_delete_task = tk.Button(root, text="Delete Task", width=30, command=delete_task, bg="light green",fg="black",font="arial")
button_delete_task.pack(pady=5)

button_update_task = tk.Button(root, text="Update Task", width=30, command=update_task, bg="light green",fg="black",font="arial")
button_update_task.pack(pady=5)

button_quit = tk.Button(root, text="Quit", width=30, command=quit_app, bg="red", fg="black",font="arial")
button_quit.pack(pady=5)

digital_clock = tk.Label(root, text="", font=("Arial", 30))
digital_clock.pack(pady=20)
display_time()
root.mainloop()
