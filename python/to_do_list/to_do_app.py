from to_do_list import To_Do_List

class To_Do_App:
    #I learnt a number of things to help with unit testing and writing better code
    #I should INJECT DEPENDENCIES
    #i will pass to_do_list into the constructor with a default value of none
    #this way, I can pass in a pre existing list if i have one and if not, then create a new one

    #furthermore, i can pass input and output into the constructor with the default value of input and print
    #(if they don't have the brackets, then i am referencing them as objects and not calling them as functions)
    #do things this way, allows me to easily mock the inputs and outputs by creating the app with custom ones 
    #also it helps because I can change how I take input and output. Like if I want to use a gui instead of CLI
    #(which is way better than hard coding them)

    def __init__(self, to_do_list = None, i_stream = input, o_stream = print):
        #checks if the passed list is not none (meaning it exists), if there isn't one, create one
        self.my_list = to_do_list if to_do_list is not None else To_Do_List()
        #here i create a new attribute input and assign it to my i_stream
        self.input = i_stream
        self.output = o_stream
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
            run = self.handle_choice(choice)


    def print_menu(self):
        #Shows options (add, remove, list, quit, etc.)
        self.output("\n********To_Do_List********")
        number = 1
        for element in self.menu_options:
            self.output(f"{number}: {element}") # now print isn't hard coded! :)
            number += 1
        self.output("**************************")


    def get_choice(self):
        try:
            choice = int(self.input("Please enter your choice: ")) #now the input isn't hard coded! :)
            return choice

        except ValueError as e:
            self.output(f"Error: {e}")
    

    def get_description(self):
        try:
            desc = str(self.input("Please enter the description for the task: "))
            return desc

        except ValueError as e:
            self.output(f"Error: {e}")
            
    
    def get_index(self):
        try:
            task_id = int(self.input("Please enter your choice: "))
            index = task_id - 1
            return index

        except ValueError as e:
            self.output(f"Error: {e}")


    def handle_choice(self, choice):
        #Dispatches to ToDoList methods
        match choice:
            case 1: 
                description = self.get_description()
                self.my_list.add_task(description)
                return True
            case 2: 
                index = self.get_index()
                self.my_list.remove_task(index)
                return True
            case 3: 
                self.my_list.display(self.output)
                return True
            case 4:
                index = self.get_index()
                self.my_list.complete_task(index)
                return True
            case 5:
                index = self.get_index()
                self.my_list.incomplete_task(index)
                return True
            case 6: 
                self.output("Thanks for using To-Do-List!")
                return False

