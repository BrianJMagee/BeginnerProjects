"""CHATGPT EVALUATION: refactoring to make unit tests easier - see test_player

Yes — your `TicTacToe` class would **absolutely benefit from refactoring** as well, especially for **clarity**, **testability**, and **clean separation of logic**. Here’s a breakdown of why, how to improve it, and what refactored code and tests could look like.

---

### 🚩 **Problems in the Current Code**

1. **Too many responsibilities in `play()`:**
   It's doing input, validation, board update, display, win check, player switch, and returning state — all in one method.

2. **Manual check of active player for board update:**
   Both conditions do the same thing — this can be simplified.

3. **Direct mutation of `used_coords` by external classes:**
   Ideally, `TicTacToe` should manage state like `used_coords`, not rely on other classes to mutate it.

4. **Tight coupling to input/output:**
   Hard to test because `getMove()` depends on `input()`, and `play()` prints directly.

---

### ✅ **Refactored Version**

Here’s a cleaner version:

```python
class TicTacToe:
    def __init__(self, board, player1, player2):
        self.board = board
        self.player1 = player1
        self.player2 = player2
        self.active_player = player1
        self.used_coords = []

    def switch_player(self):
        self.active_player = (
            self.player2 if self.active_player == self.player1 else self.player1
        )

    def is_game_over(self):
        return self.board.isFull() or self.board.checkWinner(self.active_player.symbol)

    def play_turn(self):
        position = self.active_player.getMove(self.used_coords)

        if not self.board.isValidMove(position):
            print("Invalid move. Try again.")
            return True  # Allow retry

        self.board.update(position, self.active_player.symbol)
        self.used_coords.append(self._convert_to_number(position))
        self.board.display()

        if self.board.checkWinner(self.active_player.symbol):
            self.end_game(self.active_player.name)
            return False

        if self.board.isFull():
            print("It's a draw!")
            return False

        self.switch_player()
        return True

    def end_game(self, winner):
        print(f"{winner} has won!!!!")

    def _convert_to_number(self, position):
        pos_map = {
            (0, 1): 1, (0, 3): 2, (0, 5): 3,
            (1, 1): 4, (1, 3): 5, (1, 5): 6,
            (2, 1): 7, (2, 3): 8, (2, 5): 9,
        }
        return pos_map.get(position)
```

---

### 🔧 Improvements

* **Single responsibility per method** (`play_turn`, `switch_player`, `is_game_over`)
* Makes it **testable** (no need to run the whole game to test logic)
* Centralizes `used_coords` logic inside `TicTacToe`
* Simplifies redundant checks
* Removes repeated code for both players

---

### 🧪 Example Unit Tests (with `pytest`)

```python
def test_switch_player():
    game = TicTacToe(board, player1, player2)
    current = game.active_player
    game.switch_player()
    assert game.active_player != current

def test_valid_move(monkeypatch):
    monkeypatch.setattr(player1, "getMove", lambda used: (1, 3))  # Corresponds to number 5
    game = TicTacToe(board, player1, player2)

    result = game.play_turn()
    assert result is True
    assert board.grid[1][3] == player1.symbol

def test_win_condition(monkeypatch):
    board.grid = [
        ["|", "X", "|", "X", "|", " ", "|"],
        ["|", " ", "|", " ", "|", " ", "|"],
        ["|", " ", "|", " ", "|", " ", "|"]
    ]
    monkeypatch.setattr(player1, "getMove", lambda used: (0, 5))  # This move should win
    game = TicTacToe(board, player1, player2)

    result = game.play_turn()
    assert result is False  # Game ends
```

---

### ✅ Final Notes

Yes, the class should be refactored for testability and clarity, and after this refactor:

* You can isolate each method for unit testing.
* You can mock `getMove()` for predictable control in tests.
* You avoid logic duplication and improve readability.

Would you like the full test suite or a main loop to run the game after refactoring?

"""