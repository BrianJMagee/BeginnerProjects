from to_do_list import To_Do_List

class To_Do_App:
    def __init__(self):
        self.my_list = To_Do_List()

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
            run = self.handle_choice(choice, self.my_list)


    def print_menu():
        #Shows options (add, remove, list, quit, etc.)
        print("********To-Do_List********")
        print("Your options are:")
        print("1. Add task")
        print("2. Remove task")
        print("3. Show tasks")
        print("4. Quit")
        print("**************************")

    def get_input():
        try:
            choice = int(input("Please enter your choice: "))
            return choice

        except ValueError as e:
            print(f"Error: {e}")
    
    

    def handle_choice(choice, my_list):
        #Dispatches to ToDoList methods
        match choice:
            case 1: 
                my_list.add_task()
                return True
            case 2: 
                my_list.remove_task()
                return True
            case 3: 
                my_list.display()
                return True
            case 4: 
                print("Thanks for using To-Do-List!")
                return False

