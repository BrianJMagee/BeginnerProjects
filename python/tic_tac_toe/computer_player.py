import random
import time

class Computer:
    def __init__(self, name, symbol):
        self.name =name
        self.symbol = symbol

    def getMove(self, used_coords):
        print(f"{self.name.upper()} is thinking...")

        for i in range(3, 0, -1):
            print(i)
            time.sleep(1)


        all_coords = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        available_coords = []

        for coords in all_coords:
            if coords not in used_coords:
                available_coords.append(coords)

        computer_choice = random.choice(available_coords)
        
        match computer_choice:
            case 1:
                used_coords.append(1) 
                return (0, 1)
            case 2:
                used_coords.append(2)  
                return (0, 3)
            case 3:
                used_coords.append(3)  
                return (0, 5)
            case 4:
                used_coords.append(4) 
                return (1, 1)
            case 5: 
                used_coords.append(5) 
                return (1, 3)
            case 6: 
                used_coords.append(6) 
                return (1, 5)
            case 7: 
                used_coords.append(7)
                return (2, 1)
            case 8: 
                used_coords.append(8) 
                return (2, 3)
            case 9: 
                used_coords.append(9)
                return (2, 5)
            
