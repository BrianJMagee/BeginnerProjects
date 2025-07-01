from to_do_app import To_Do_App

def main():
    app = To_Do_App()
    app.run

if __name__ == "__main__":
    main()



"""Absolutely — planning your classes and methods first is a great approach! For a beginner-level **To-Do List CLI Project**, here’s a clean and simple structure using **object-oriented programming**.

---

### ✅ **Suggested Classes & Methods**

#### 1. **Task**

Represents a single to-do item.

**Attributes:**

* `description`: str
* `completed`: bool

**Methods:**

* `mark_complete()`: Sets `completed = True`
* `mark_incomplete()`: Sets `completed = False`
* `__str__()`: Returns a string like `"☑ Buy groceries"` or `"☐ Wash car"`

---

#### 2. **ToDoList**

Manages a list of tasks.

**Attributes:**

* `tasks`: list of `Task` objects

**Methods:**

* `add_task(description: str)`
* `remove_task(index: int)`
* `list_tasks()`: Print or return list of tasks with status
* `complete_task(index: int)`
* `incomplete_task(index: int)`
* `save_to_file(filename: str)` *(Optional but great practice!)*
* `load_from_file(filename: str)` *(Optional)*

---

#### 3. **ToDoApp (Optional Controller Layer)**

Handles user input/output logic if you want to separate it from core logic.

**Methods:**

* `run()`: The main loop (menu, user interaction)
* `print_menu()`: Shows options (add, remove, list, quit, etc.)
* `handle_choice(choice: str)`: Dispatches to ToDoList methods

---

### 🧠 Bonus Ideas (If You Want to Extend Later)

* Add due dates (with `datetime`)
* Priorities (e.g., High/Medium/Low)
* Search/filter tasks
* Persistent storage using `json`

---

Would you like help building the class structure or setting up your files and testing strategy for it?
"""