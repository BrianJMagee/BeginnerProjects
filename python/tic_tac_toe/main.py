from board import Board
from player import Player
from tic_tac_toe import TicTacToe
from computer_player import Computer

loop = True
while loop:
    try:
        answer = int(input("Would you like to play (1) PvP or (2) PvAI: "))

        match answer:
            case 1: 
                player1 = Player("Jim", "x")
                player2 = Player("Bob", "o")
                loop = False
            case 2:
                player1 = Player("Jim", "x")
                player2 = Computer("El Computo", "o")
                loop = False
            case _:
                raise Exception("Invalid input")
    except Exception as e:
        print(f"Error: {e}")

print("*************")
print("|", "1", "|", "2", "|", "3", "|")
print("|", "4", "|", "5", "|", "6", "|")
print("|", "7", "|", "8", "|", "9", "|")
print("Here is the key")
print("*************")


board = Board()
game = TicTacToe(board, player1, player2, [])

play = True
while play:
    play = game.play()