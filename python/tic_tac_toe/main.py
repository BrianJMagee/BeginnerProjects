from board import Board
from player import Player
from tic_tac_toe import TicTacToe

print("*************")
print("|", "1", "|", "2", "|", "3", "|")
print("|", "4", "|", "5", "|", "6", "|")
print("|", "7", "|", "8", "|", "9", "|")
print("Here is the key")
print("*************")

board = Board()
player1 = Player("Jim", "x")
player2 = Player("Bob", "o")
active_player = player1
game = TicTacToe(board, active_player, player1, player2) #, computer_player

play = True

while play:
    play = game.play()