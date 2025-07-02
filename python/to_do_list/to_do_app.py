from to_do_list import To_Do_List

class To_Do_App:
    def __init__(self):
        self.my_list = To_Do_List()
        self.menu_options = ["Add task", 
                             "Remove task", 
                             "Show tasks",
                             "Mark task as complete", 
                             "Mark task as incomplete", 
                             "Quit"]

    def run(self):
        run = True
        while run:
            #print menu
            self.print_menu()

            #get choice
            choice = self.get_choice()

            #handle choice
            run = self.handle_choice(choice, self.my_list)


    def print_menu(self):
        #Shows options (add, remove, list, quit, etc.)
        print("\n********To-Do_List********")
        number = 1
        for element in self.menu_options:
            print(f"{number}: {element}")
            number += 1
        print("**************************")


    def get_choice(self):
        try:
            choice = int(input("Please enter your choice: "))
            return choice

        except ValueError as e:
            print(f"Error: {e}")
    

    def get_description(self):
        try:
            desc = str(input("Please enter the description for the task: "))
            return desc

        except ValueError as e:
            print(f"Error: {e}")
            
    
    def get_index(self):
        try:
            task_id = int(input("Please enter your choice: "))
            index = task_id - 1
            return index

        except ValueError as e:
            print(f"Error: {e}")


    def handle_choice(self, choice, my_list):
        #Dispatches to ToDoList methods
        match choice:
            case 1: 
                description = self.get_description()
                my_list.add_task(description)
                return True
            case 2: 
                index = self.get_index()
                my_list.remove_task(index)
                return True
            case 3: 
                my_list.display()
                return True
            case 4:
                index = self.get_index
                my_list.complete_task(index)
            case 5:
                index = self.get_index
                my_list.incomplete_task(index)
            case 6: 
                print("Thanks for using To-Do-List!")
                return False

