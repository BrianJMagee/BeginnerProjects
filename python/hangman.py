import random
import string

def inGuessedLetters(gLetters, uGuess):
    if uGuess in gLetters or not uGuess.isalpha():
        print("Already guessed or invalid letter.")
        return True
    return False

def updateRevealed(wLetters, revealed, uGuess):
    for i in range(len(wLetters)):
        if wLetters[i] == uGuess:
            revealed[i] = uGuess
    return revealed

# --- Main Program ---
lives = 5
words = ["apple", "banana", "orange"]
guessedLetters = []

computerWord = random.choice(words).upper()
wordLetters = list(computerWord)
revealedLetters = ["_" for _ in wordLetters]

print("I'm thinking of a word with", len(computerWord), "letters.")

while lives > 0 and "_" in revealedLetters:
    print("\nWord progress:", " ".join(revealedLetters))
    userGuess = input("Guess a letter: ").upper()

    if inGuessedLetters(guessedLetters, userGuess):
        lives -= 1
        print(f"Lives remaining: {lives}")
        continue

    guessedLetters.append(userGuess)

    if userGuess in wordLetters:
        print("Correct!")
        revealedLetters = updateRevealed(wordLetters, revealedLetters, userGuess)
    else:
        lives -= 1
        print("Wrong!")
        print(f"Lives remaining: {lives}")

if "_" not in revealedLetters:
    print("\nYou won! The word was:", computerWord)
else:
    print("\nYou lost. The word was:", computerWord)
