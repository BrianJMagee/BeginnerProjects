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



    def load_from_file(self, path):
        self.tasks.clear()
        with open(path, "r") as file:
            for line in file:
                parts = line.strip().split("|||")
                if len(parts) == 2:
                    description, completed_str = parts
                    completed = completed_str == "True"
                    self.tasks.append(Task(description, completed))

    def save_to_file(self, path):
        with open(path, "w") as file:
            for task in self.tasks:
                file.write(f"{task.description}|||{task.completed}\n")

    def get_tasks(self):
        return self.tasks