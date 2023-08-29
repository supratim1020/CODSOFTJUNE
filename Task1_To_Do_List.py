import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Please enter a task to add.")

def update_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        new_task = entry_task.get()
        if new_task:
            index = selected_task_index[0]
            listbox_tasks.delete(index)
            listbox_tasks.insert(index, new_task)
            entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task to update.")

def delete_task():
    selected_task_index = listbox_tasks.curselection()
    if selected_task_index:
        index = selected_task_index[0]
        listbox_tasks.delete(index)
    else:
        messagebox.showwarning("Warning","Please select a task to delete.")

root = tk.Tk()
root.title("To Do List")
root.geometry("350x300")
root.resizable(False,False)
root.config(bg="#18989a")

frame_tasks = tk.Frame(root)
frame_tasks.pack(pady=10)

listbox_tasks = tk.Listbox(frame_tasks, width=50)
listbox_tasks.pack(side=tk.LEFT, fill=tk.BOTH)

scrollbar_tasks = tk.Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.BOTH)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = tk.Entry(root, width=53)
entry_task.pack(pady=10)


btn_add_task = tk.Button(root, text="Add Task",fg="black",bg="#80ff80", command=add_task)
btn_add_task.place(x=15,y=240,width=62,height=40)

btn_update_task = tk.Button(root, text="Update Task",fg="black",bg="#99d1ff", command=update_task)
btn_update_task.place(x=88,y=240,width=80,height=40)

btn_delete_task = tk.Button(root, text="Delete Task",fg="black",bg="#ffb3b3", command=delete_task)
btn_delete_task.place(x=180,y=240,width=73,height=40)

btn_exit=tk.Button(root,text="Exit",fg="white",bg="#ff3333",command=exit)
btn_exit.place(x=265,y=240,width=70,height=40)


root.mainloop()