"""
After refactoring the `TicTacToe` class as discussed earlier (removing `used_coords` from the constructor, moving that logic into the class, and renaming `play()` to `play_turn()`), your `main.py` can be **simplified** and **cleaned up** to reflect those changes.

Here’s how you should update your `main.py`:

---

### ✅ **Updated `main.py`**

```python
from board import Board
from player import Player
from tic_tac_toe import TicTacToe
from computer_player import Computer

def get_game_mode():
    while True:
        try:
            answer = int(input("Would you like to play (1) PvP or (2) PvAI: "))

            match answer:
                case 1: 
                    return Player("Jim", "x"), Player("Bob", "o")
                case 2:
                    return Player("Jim", "x"), Computer("El Computo", "o")
                case _:
                    raise ValueError("Invalid input")
        except ValueError as e:
            print(f"Error: {e}")

def main():
    player1, player2 = get_game_mode()

    print("*************")
    print("|", "1", "|", "2", "|", "3", "|")
    print("|", "4", "|", "5", "|", "6", "|")
    print("|", "7", "|", "8", "|", "9", "|")
    print("Here is the key")
    print("*************")

    board = Board()
    game = TicTacToe(board, player1, player2)

    while True:
        if not game.play_turn():
            break

if __name__ == "__main__":
    main()
```

---

### ✅ **Why This Is Better**

* `get_game_mode()` isolates input logic for mode selection.
* Clear, readable `main()` function with no global state.
* Uses the refactored `TicTacToe` interface with no need to pass `used_coords` externally.
* `if __name__ == "__main__"` guard lets you import this file in unit tests without running the game.

Let me know if you want a version that also includes replay/restart functionality after a game ends.

"""