import random

highPoint = 0
lowPoint = 0

try:
    if lowPoint == 0 and highPoint == 0:
        lowPoint = int(input("State the low end for the guessing: "))
        highPoint = int(input("State the high end for the guessing: "))

    if highPoint <= lowPoint:
        raise ValueError("The high point must be greater than the low point.")
    if lowPoint <= 0 or highPoint <= 0:
        raise ValueError("Values must be greater than 0.")

    secretNum = random.randint(lowPoint, highPoint)
    userGuess = None

    print("---------------------------------------------")
    print("Hi, I'm the computer and I've picked a number.")
    print("Try to guess it!")

    while userGuess != secretNum:
        try:
            userGuess = int(input("Guess: "))

            if userGuess == secretNum:
                print("You found it!!!!")
            elif userGuess < secretNum:
                print("Too low!")
            elif userGuess > secretNum:
                print("Too high!")

        except ValueError:
            print("Please enter a valid number.")

except ValueError as e:
    print(f"Input error: {e}")
