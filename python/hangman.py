import random

#keep track of lives
lives = 5

#computer picks a word
words = ("Banana", "Apple", "Orange")
computerChoice = words[random.randint(0, 2)]
wordLength = len(computerChoice)
underscoreArray = []

for i in range(0, wordLength):
    underscoreArray.append("_")

#loop to repeat the prints
play = True
while play == True:
    #print statemets
    print("Here is the hidden word")
    print(underscoreArray)
    userChoice = input("Please enter a letter for your guess: ")
    
    if computerChoice.find(userChoice):
        underscoreArray[computerChoice.find(userChoice)] = userChoice
    else:
        lives -= 1
        print(lives)

    play = True


#if the user guesses a letter in the word, that is letter is revealed
#if the user guesses a wrong letter, they lose a life