from task import Task

class To_Do_List:
    #Manages a list of tasks.
    def __init__(self):
        self.tasks = []
    
    def add_task(self, description):
        #creates task object
        #adds to list
        self.tasks.append(Task(description=description, completed=False))


    def remove_task(self, index):
        self.tasks.remove(index)


    def display(self):
        #prints or return list of tasks with status
        number = 1
        for element in self.tasks:
            print(f"{number}: {element.return_string()}")
            number+=1


    def complete_task(self, index):
        self.tasks[index].mark_complete() 
        

    def incomplete_task(self, index):
        self.tasks[index].mark_incomplete() 


"""
    def save_to_file(filename):
        pass
    
    def load_from_file(filename):
        pass
    
    """