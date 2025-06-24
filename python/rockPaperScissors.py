import random
import time

print("-------------------------------")
print("Let's play rock, paper, scissors!")


play = True

while play == True:
    print("Get ready!")
    print("Type (r) rock, (p) paper or (s) scissors in ")

    for i in range(3, 0, -1):
        print(i)
        time.sleep(1)
    
    choices = ("Rock", "Paper", "Scissors")

    userChoice = str(input("GO: "))
    computerChoice = random.choice(choices)
    print(f"Computer chose {computerChoice}")
    
    if userChoice == "r" and computerChoice == "Rock" or userChoice == "p" and computerChoice == "Paper" or userChoice == "s" and computerChoice == "Scissors":
        again = input("A tie! Shall we go again (y/n): ")
    elif userChoice == "r" and computerChoice == "Scissors" or userChoice == "p" and computerChoice == "Rock" or userChoice == "s" and computerChoice == "Paper":
        again = input("You win! Shall we go again (y/n): ")
    else:
        again = input("The computer wins! Shall we go again (y/n): ")

    
    if again == "y":
        break  # valid, continue game loop
        
    elif again == "n":
        play = False
        print("Thanks for playing!")
        print("-------------------------------")
        break
    else:
        print("Please enter 'y' or 'n'.")
        print("-------------------------------")