class Board:
    def __init__(self):
        self.grid = [["|", " ", "|", " ", "|", " ", "|"], 
                     ["|", " ", "|", " ", "|", " ", "|"],
                     ["|", " ", "|", " ", "|", " ", "|"]]

    def display(self):
        print("*******")
        for row in self.grid:
           print("".join(row)) 
        print("*******")
   
           
    def update(self, position, symbol):
        #position is the coordinates for a 2d array
        #at postiotion, add symbol to self.grid
        x = position[0]
        y = position[1]

        self.grid[x][y] = symbol

    def isFull(self):
        for row in self.grid:
            for element in row:
                if element == " ":
                    return False
        return True

    def checkWinner(self, symbol):
        winning_positions = [
            # Rows
            [(0,1), (0,3), (0,5)],
            [(1,1), (1,3), (1,5)],
            [(2,1), (2,3), (2,5)],
            
            # Columns
            [(0,1), (1,1), (2,1)],
            [(0,3), (1,3), (2,3)],
            [(0,5), (1,5), (2,5)],
            
            # Diagonals
            [(0,1), (1,3), (2,5)],
            [(0,5), (1,3), (2,1)]
        ]

        for positions in winning_positions:
            matched = True
            for x, y in positions:
                if self.grid[x][y] != symbol:
                    matched = False
                    break
            if matched:
                return True

        return False

    def isValidMove(self, position):
        x = position[0]
        y = position[1]

        if self.grid[x][y] == " ": return True
        else: return False