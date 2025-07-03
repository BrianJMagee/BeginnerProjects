from to_do_list import To_Do_List


class To_Do_App:
    # I learnt a number of things to help with unit testing and writing better code
    # I should INJECT DEPENDENCIES
    # i will pass to_do_list into the constructor with a default value of none
    # this way, I can pass in a pre existing list if i have one and if not, then create a new one

    # furthermore, i can pass input and output into the constructor with the default value of input and print
    # (if they don't have the brackets, then i am referencing them as objects and not calling them as functions)
    # do things this way, allows me to easily mock the inputs and outputs by creating the app with custom ones
    # also it helps because I can change how I take input and output. Like if I want to use a gui instead of CLI
    # (which is way better than hard coding them)

    def __init__(self, to_do_list=None, i_stream=input, o_stream=print):
        # checks if the passed list is not none (meaning it exists), if there isn't one, create one
        self.my_list = to_do_list if to_do_list is not None else To_Do_List()

        # here i create a new attribute input and assign it to my i_stream
        self.input = i_stream
        self.output = o_stream
        self.menu_options = [
            "Add task",
            "Remove task",
            "Show tasks",
            "Mark task as complete",
            "Mark task as incomplete",
            "Save tasks to file",
            "Load tasks from file",
            "Quit",
        ]
        self.file_path = "C:\\Users\\brian\\Documents\\Workspace_VS_Code\\beginner_projects\\python\\to_do_list\\list.txt"


    def run(self):
        run = True
        while run:
            # print menu
            self.print_menu()

            # get choice
            choice=self.get_input(
                "Choose option: ",
                int,
                validate_func=lambda x: 1 <= x <= len(self.menu_options),
                )

            # handle choice
            run = self.handle_choice(choice)

    def print_menu(self):
        # Shows options (add, remove, list, quit, etc.)
        self.output("\n********To_Do_List********")
        number = 1
        for element in self.menu_options:
            self.output(f"{number}: {element}")  # now print isn't hard coded! :)
            number += 1
        self.output("**************************")

    # here I combined all three of the input functions into one.
    # this one takes a prompt and handles input for everythin, however how do i handle casting?
    # well i set the default to string, and pass a different one if it's an int
    def get_input(self, prompt, cast_func=str, validate_func=lambda x: True):
        while True:
            try:
                user_input = self.input(prompt)
                value = cast_func(user_input)
                if not validate_func(value):
                    self.output("Invalid choice, please try again.")
                    continue
                return value
            except (ValueError, TypeError) as e:
                self.output(f"Error: {e}. Please try again.")

    def handle_choice(self, choice):
        # Dispatches to ToDoList methods
        match choice:
            case 1:
                description = self.get_input(
                    "Please enter a description for the task: ", str
                )
                self.my_list.add_task(description)
                return True
            

            case 2:
                if not self.my_list.tasks:
                    self.output("No tasks to remove.")
                    return True
                # a lambda function is a small, temprary function that we can create instead of using def
                # so, i pass the entire function lambda x to get_input. Then, when x is used in get_input,
                # it calls the lambda function where it will convert x to an int and subtract 1 and return the result to get_input
                # which will further return the result to the index attribute below
                index = self.get_input(
                    "Please enter the task to be removed: ",
                    lambda x: int(x) - 1,
                    lambda x: 0 <= x <= len(self.my_list.tasks) - 1,
                )
                self.my_list.remove_task(index)
                return True
            case 3:
                self.my_list.display(self.output)
                return True
            

            case 4:
                if not self.my_list.tasks:
                    self.output("No tasks to remove.")
                    return True
                
                
                index = self.get_input(
                    "Please enter the task to be marked as complete: ",
                    lambda x: int(x) - 1,
                    lambda x: 0 <= x <= len(self.my_list.tasks) - 1,
                )
                self.my_list.complete_task(index)
                return True
            

            case 5:
                if not self.my_list.tasks:
                    self.output("No tasks to remove.")
                    return True
                
                index = self.get_input(
                    "Please enter the task to be marked as incomplete: ",
                    lambda x: int(x) - 1,
                    lambda x: 0 <= x <= len(self.my_list.tasks) - 1,
                )
                self.my_list.incomplete_task(index)
                return True
            

            case 6:
                self.my_list.save_to_file(output=self.output, filename=self.file_path)
                return True


            case 7:
                self.my_list.load_from_file(output=self.output, filename=self.file_path)
                return True


            case 8:
                self.output("Thanks for using To-Do-List!")
                return False
