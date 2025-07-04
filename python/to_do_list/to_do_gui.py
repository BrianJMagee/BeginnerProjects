# gui.py
from tkinter import *
from tkinter import filedialog, messagebox
from to_do_list import To_Do_List

window = Tk()
window.title("To-Do List")
window.geometry("600x400")

my_list = To_Do_List()

# --- Functions --- #
def add_task():
    text = entryBox.get()
    if text:
        my_list.add_task(text)
        listbox.insert(END, text)
        listbox.config(height=listbox.size())
        entryBox.delete(0, END)

def delete_task():
    selected = listbox.curselection()
    if selected:
        index = selected[0]
        listbox.delete(index)
        my_list.remove_task(index)
        listbox.config(height=listbox.size())

def load_tasks():
    path = filedialog.askopenfilename(
        title="Open file",
        filetypes=[("Text files", "*.txt")]
    )
    if path:
        my_list.load_from_file(path)
        listbox.delete(0, END)
        for task in my_list.get_tasks():
            listbox.insert(END, task.description)
        listbox.config(height=listbox.size())

def save_tasks():
    path = filedialog.asksaveasfilename(
        defaultextension=".txt",
        filetypes=[("Text files", "*.txt")]
    )
    if path:
        my_list.save_to_file(path)
        messagebox.showinfo("Saved", f"Tasks saved to {path}")

# --- UI Elements --- #
listbox = Listbox(window, font=("Arial", 18), width=30)
listbox.pack(pady=10)

entryBox = Entry(window, font=("Arial", 14))
entryBox.pack()

button_frame = Frame(window)
button_frame.pack(pady=10)

addButton = Button(button_frame, text="Add", command=add_task)
addButton.pack(side=LEFT, padx=5)

deleteButton = Button(button_frame, text="Delete", command=delete_task)
deleteButton.pack(side=LEFT, padx=5)

# --- Menu --- #
menubar = Menu(window)
fileMenu = Menu(menubar, tearoff=0)
fileMenu.add_command(label="Open", command=load_tasks)
fileMenu.add_command(label="Save", command=save_tasks)
fileMenu.add_separator()
fileMenu.add_command(label="Exit", command=window.quit)

menubar.add_cascade(label="File", menu=fileMenu)
window.config(menu=menubar)

window.mainloop()




"""CHATGPT gui application (after refactoring of every function in every file lmao)

import tkinter as tk
from tkinter import filedialog, messagebox
from to_do_list import ToDoList
from task import Task
from file_io import FileIO

class ToDoAppGUI:
    def __init__(self, master):
        self.master = master
        self.master.title("To-Do List")
        self.todo = ToDoList()
        self.io = FileIO()

        self.listbox = tk.Listbox(master, font=("Arial", 16), width=50)
        self.listbox.pack()

        self.entry = tk.Entry(master, font=("Arial", 14))
        self.entry.pack()

        frame = tk.Frame(master)
        frame.pack()

        tk.Button(frame, text="Add", command=self.add_task).pack(side=tk.LEFT)
        tk.Button(frame, text="Delete", command=self.delete_task).pack(side=tk.LEFT)
        tk.Button(frame, text="Toggle", command=self.toggle_task).pack(side=tk.LEFT)
        tk.Button(frame, text="Save", command=self.save_tasks).pack(side=tk.LEFT)
        tk.Button(frame, text="Load", command=self.load_tasks).pack(side=tk.LEFT)

    def refresh(self):
        self.listbox.delete(0, tk.END)
        for task in self.todo.get_tasks():
            self.listbox.insert(tk.END, str(task))

    def add_task(self):
        text = self.entry.get().strip()
        if text:
            self.todo.add_task(text)
            self.entry.delete(0, tk.END)
            self.refresh()

    def delete_task(self):
        index = self.get_selected_index()
        if index is not None:
            self.todo.delete_task(index)
            self.refresh()

    def toggle_task(self):
        index = self.get_selected_index()
        if index is not None:
            self.todo.toggle_task(index)
            self.refresh()

    def save_tasks(self):
        path = filedialog.asksaveasfilename(defaultextension=".txt")
        if path:
            self.io.save(path, self.todo.get_tasks())

    def load_tasks(self):
        path = filedialog.askopenfilename()
        if path:
            self.todo.tasks = self.io.load(path)
            self.refresh()

    def get_selected_index(self):
        try:
            return self.listbox.curselection()[0]
        except IndexError:
            messagebox.showwarning("No Selection", "Please select a task.")
            return None

if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoAppGUI(root)
    root.mainloop()

"""