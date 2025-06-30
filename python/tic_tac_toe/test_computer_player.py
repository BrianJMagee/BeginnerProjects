"""CHATGPT EVALUATION: refactoring to make unit tests easier - see test_player


Yes, this `Computer` class can also benefit from **refactoring**, especially for **testability**, **clarity**, and **code reuse**. Here's how and why:

---

### 🔍 Key Issues in the Current Code

1. **Hard-coded mapping (1 → (0,1), etc.):**
   Same problem as in your original `Player` and `Board` code — using "magic numbers" and repeated `match` statements to convert numbers to coordinates.

2. **Side effects in `getMove`:**
   The function **mutates** `used_coords` *and* returns the move. This can be error-prone and harder to test.

3. **Coupling UI with logic:**
   The `print()` countdown and uppercase display is cool, but should be separated for testability.

4. **Manual filtering of available coords:**
   Works fine, but you could simplify this using list comprehensions or set operations.

---

### ✅ Refactored Version

Let’s clean this up:

```python
import random
import time

class Computer:
    coord_map = {
        1: (0, 0), 2: (0, 1), 3: (0, 2),
        4: (1, 0), 5: (1, 1), 6: (1, 2),
        7: (2, 0), 8: (2, 1), 9: (2, 2)
    }

    reverse_map = {v: k for k, v in coord_map.items()}

    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol

    def getMove(self, used_coords):
        self.think()

        all_coords = set(range(1, 10))
        used_set = set(used_coords)
        available_coords = list(all_coords - used_set)

        if not available_coords:
            raise Exception("No available moves")

        choice = random.choice(available_coords)
        return self.coord_map[choice]

    def think(self):
        print(f"{self.name.upper()} is thinking...")
        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)
```

---

### 🔧 Benefits of This Refactor

* **Separation of concerns:** `think()` handles the animation; `getMove()` focuses on logic.
* **Cleaner coordinate mapping:** Much easier to read and test.
* **Testable logic:** You can now inject `used_coords` and mock `random.choice` for predictable tests.
* **No side effects:** Doesn’t modify `used_coords` directly, making state management clearer.

---

### 🧪 Example Unit Test

```python
from computer import Computer

def test_get_move_returns_valid_coordinate(monkeypatch):
    comp = Computer("AI", "O")
    monkeypatch.setattr("random.choice", lambda x: 5)
    used = [1, 2, 3]
    result = comp.getMove(used)
    assert result == (1, 1)

def test_no_available_moves():
    comp = Computer("AI", "O")
    used = list(range(1, 10))
    try:
        comp.getMove(used)
        assert False, "Should raise exception if no moves left"
    except Exception as e:
        assert str(e) == "No available moves"
```

---

### Optional: Return the number and coords?

If you still want to know what number was chosen (e.g., for display), you can return a tuple:

```python
return choice, self.coord_map[choice]
```

Let me know if you want to unify this with your `Player` or `Board` class logic too.

"""