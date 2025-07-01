from to_do_list import To_Do_List

class To_Do_App:
    def run(self):
        tasks = []
        my_list = To_Do_List(tasks=tasks)

        run = True
        while run:
            #print menu
            self.print_menu()

            #get choice
            choice = self.get_input()

            #handle choice
            self.handle_choice(choice)


    def print_menu():
        #Shows options (add, remove, list, quit, etc.)
        print("********To-Do_List********")
        print("Your options are:")
        print("1. Add task")
        print("2. Remove task")
        print("**************************")

    def get_input():
        try:
            choice = int(input("Please enter your choice: "))
            return choice

        except ValueError as e:
            print(f"Error: {e}")

    def handle_choice(choice):
        #Dispatches to ToDoList methods
        match choice:
            case 1: 

