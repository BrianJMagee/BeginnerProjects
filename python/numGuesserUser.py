import random

lowPoint = 1
highPoint = random.randint(2, 1000)

try:
    computerGuess = None

    print("---------------------------------------------")
    print("Hi, I'm the computer and I'll try and guess your number.")
    print(f"Please come up with a secret number between {lowPoint} and {highPoint}")

    play = True

    while play == True:
        # computer guesses
        computerGuess = random.randint(lowPoint, highPoint)
        print(f"Is your number: {computerGuess}")

        # i tell it if it's close
        playerHint = str(
            input("Tpye (h) for higher, (l) for lower, or (c) for correct: ")
        )
        match playerHint:
            case "h":
                lowPoint = computerGuess + 1
            case "l":
                highPoint = computerGuess - 1
            case "c":
                print("I got it!!!!")
                play = False
            case _:
                print("Invalid input")

except ValueError as e:
    print(f"Input error: {e}")
