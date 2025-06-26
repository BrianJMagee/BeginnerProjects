class Player:
    def __init__(self, name, symbol):
        self.name = name
        self.symbol = symbol
    
    def getMove(self):
        while True:
            try:
                print(self.name.upper())
                user_choice = int(input("Please enter your choice as a number 1-9: "))

                match user_choice:
                    case 1: return (0, 1)
                    case 2: return (0, 3)
                    case 3: return (0, 5)
                    case 4: return (1, 1)
                    case 5: return (1, 3)
                    case 6: return (1, 5)
                    case 7: return (2, 1)
                    case 8: return (2, 3)
                    case 9: return (2, 5)
                    case _: 
                        print("That was an invalid input")
                        raise Exception("That was an invalid number")
            
            except Exception as e:
                print(f"Error: {e}")

