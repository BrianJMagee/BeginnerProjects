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
        self.tasks.pop(index)


    def display(self, output):
        #prints or return list of tasks with status
        output("\n********Your_Tasks********")
        number = 1
        for element in self.tasks:
            output(f"{number}: {element.return_string()}     Status: {element.return_is_complete()}")
            number+=1
        output("\n**************************")

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