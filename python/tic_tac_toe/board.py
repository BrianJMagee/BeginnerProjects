"""Purpose: Manages the game board, printing, and checking win conditions.

Attributes:
grid: 2D list or flat list representing the board state

Methods:
display(): prints the board

update(position, symbol): places a move on the board

is_full(): checks if the board is full

check_winner(symbol): checks if a player with symbol has won

is_valid_move(position): checks if the move is allowed"""

class board:
    def __init__(self):
        self.grid = [["|", " ", "|", " ", "|", " ", "|", " ", "|"], 
                     ["|", " ", "|", " ", "|", " ", "|", " ", "|"],
                     ["|", " ", "|", " ", "|", " ", "|", " ", "|"]]

    def display(self):
        for row in self.grid:
           print("".join(row))    
           
    def update(position, symbol):
        pass

    def isFull():
        pass

    def checkWinner(symbol):
        pass

    def isValidMove(position):
        pass