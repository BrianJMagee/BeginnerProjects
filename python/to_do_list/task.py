class Task:
    def __init__(self, description, completed):
        self.description = description
        self.completed = completed
    
    def mark_complete(self):
        self.completed = True

    def mark_incomplete(self):
        self.completed = False

    def return_string(self):
        return self.description
    
    def return_is_complete(self):
        return "Complete" if self.completed else "Incomplete"
