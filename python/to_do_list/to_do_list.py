from task import Task

class To_Do_List:
    #Manages a list of tasks.
    #inject open()
    def __init__(self, file_opener=open):
        self.tasks = []
        self.file_opener = file_opener
    

    def add_task(self, description):
        #creates task object
        #adds to list
        self.tasks.append(Task(description=description, completed=False))


    def remove_task(self, index):
        self.tasks.pop(index)


    def display(self, output):
        #prints or return list of tasks with status
        output("\n**************Your_Tasks**************")
        number = 1
        for element in self.tasks:
            output(f"{number}: {element.return_string()}     Status: {element.return_is_complete()}")
            number+=1
        output("\n**************************************")

    def complete_task(self, index):
        self.tasks[index].mark_complete() 
        

    def incomplete_task(self, index):
        self.tasks[index].mark_incomplete() 


    def save_to_file(self, filename, output):
        try:
            with self.file_opener(filename, mode="w") as file:
                for task in self.tasks:
                    line = f"{task.return_string()}|||{task.completed}\n"
                    file.write(line)
            output(f"Tasks successfully saved to '{filename}'.")
        except Exception as e:
            output(f"An error occurred while saving: {e}")


        

    def load_from_file(self, filename, output):
        try:
            with self.file_opener(filename, mode="r") as file:
                self.tasks.clear()  # Clear current tasks
                for line in file:
                    parts = line.strip().split("|||")
                    if len(parts) == 2:
                        description, completed_str = parts
                        completed = completed_str == "True"
                        self.tasks.append(Task(description, completed))
            output(f"Tasks successfully loaded from '{filename}'.")
        except FileNotFoundError:
            output("That file was not found")
        except PermissionError:
            output("You do not have permission for this")
        except Exception as e:
            output(f"An error occurred while reading: {e}")



    


"""
with #closes the file after we're done with it
open(file = file_path, mode = "w") 
as file #is like instanciating a file object, like how we do x = object()

"""