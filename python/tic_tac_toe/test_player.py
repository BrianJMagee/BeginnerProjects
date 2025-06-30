"""
i've realised that my code is difficult to test, because my code does many things that require mocks, and also the unintuitiveness
of some of my loops, user input, and modifying of state outside of the class. Here was chatgpt's evaluation:



Yes — refactoring code to make it easier to test is both common and recommended. It's called **writing testable code** or **designing for testability**. Here are specific ways you could improve your `Player.getMove()` method to be more test-friendly:

---

### ✅ 1. **Separate Input Handling from Logic**

Right now, `getMove` both:

* prompts for input (`input()`)
* processes that input
* modifies the game state (`used_coords.append(...)`)

**Why it's a problem:** It's hard to test functions that:

* read from `input()`
* print directly
* include infinite loops

**How to fix it:**

Split into two functions:

```python
class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def choose_move(self, choice, used_coords):
        if choice in used_coords:
            raise ValueError("That coord has already been used")

        coord_map = {
            1: (0, 1),
            2: (0, 3),
            3: (0, 5),
            4: (1, 1),
            5: (1, 3),
            6: (1, 5),
            7: (2, 1),
            8: (2, 3),
            9: (2, 5),
        }

        if choice not in coord_map:
            raise ValueError("That was an invalid number")

        used_coords.append(choice)
        return coord_map[choice]

    def getMove(self, used_coords):
        while True:
            try:
                print(self.name.upper())
                user_choice = int(input("Please enter your choice as a number 1-9: "))
                return self.choose_move(user_choice, used_coords)
            except Exception as e:
                print(f"Error: {e}")
```

**Why this is better:**

* You can now test `choose_move()` directly without dealing with `input()` or a loop.
* The `getMove()` method becomes just a wrapper for I/O handling.

---

### ✅ 2. **Avoid Modifying Mutable Arguments Inside Methods**

Currently `used_coords.append(...)` happens inside `getMove`. You might consider returning the coordinate and updating `used_coords` outside.

Why? Functions that **modify external state** are harder to test and debug.

---

### ✅ 3. **Avoid Infinite Loops in Logic**

Infinite `while True` loops are dangerous in testing. Extract logic into single-shot methods that:

* process one thing
* return a result or raise

Then wrap it in a loop only in your main app logic.

---

### ✅ 4. **Use Return Values Instead of Printing in Core Logic**

Avoid `print()` inside logic-heavy methods. Let your game loop handle printing. This makes your logic testable and reusable.

---

### Summary: What to Change

| Current Practice               | Better Alternative                    |
| ------------------------------ | ------------------------------------- |
| `input()` in logic             | Pass input as an argument             |
| `print()` in logic             | Return error messages or raise errors |
| Modify `used_coords` in method | Return move; modify state externally  |
| `while True` inside logic      | Make logic a single decision per call |

---

Would you like help rewriting your current class this way?

"""

"""CHAT GPT UNIT TESTING FOR REFACTORED CODE:

import pytest
from player import Player  # Adjust the import path to match your project structure

def test_valid_move_adds_coord_and_returns_position():
    p = Player("Test", "X")
    used = []
    result = p.choose_move(1, used)
    assert result == (0, 1)
    assert 1 in used

def test_invalid_number_raises_value_error():
    p = Player("Test", "X")
    used = []
    with pytest.raises(ValueError, match="invalid number"):
        p.choose_move(10, used)

def test_used_coord_raises_value_error():
    p = Player("Test", "X")
    used = [5]
    with pytest.raises(ValueError, match="already been used"):
        p.choose_move(5, used)

def test_multiple_valid_choices():
    p = Player("Test", "X")
    used = []
    assert p.choose_move(3, used) == (0, 5)
    assert p.choose_move(4, used) == (1, 1)
    assert used == [3, 4]

"""


"""
#MY ATTEMPT AT TESTING
from player import Player
import pytest

@pytest.fixture
def player():
    return Player("Brian", "x")

@pytest.mark.parametrize("used_coords, expected", [
    (1, (0, 1)),
    (2, (0, 3)),
    (3, (0, 5)),
    (4, (1, 1)),
    (5, (1, 3)),
    (6, (1, 5)),
    (7, (2, 1)),
    (8, (2, 3)),
    (9, (2, 5)),
    (20, Exception("That was an invalid number")),
    (-20, Exception("That was an invalid number")),
    (0, Exception("That was an invalid number")),

])

def test_getMove(used_coords, expected):
    assert Player.getMove(used_coords) == expected

    """
