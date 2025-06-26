class TicTacToe:
    def __init__(self, board, player1, player2, used_coords):
        self.board = board
        self.active_player = player1
        self.player1 = player1
        self.player2 = player2
        self.used_coords = used_coords

    def switchPlayer(self):
        if self.active_player == self.player1: self.active_player = self.player2
        elif self.active_player == self.player2: self.active_player = self.player1

    def play(self):
        #ask for an input
        position = self.active_player.getMove(self.used_coords)

        #check if a valid input
        valid = self.board.isValidMove(position)

        #update the board
        if self.active_player == self.player1 and valid: 
            self.board.update(position, self.active_player.symbol)
        elif self.active_player == self.player2 and valid: 
            self.board.update(position, self.active_player.symbol)

        #display the board
        self.board.display()

        #check if someone won
        win = self.board.checkWinner(self.active_player.symbol)
        if win == True: 
            return TicTacToe.endGame(self, self.active_player.name)
        elif valid:
            #toggle player
            TicTacToe.switchPlayer(self)
            return True
        else: return True

    def endGame(self, winner):
        print(f"{winner} has won!!!!")
        return False
