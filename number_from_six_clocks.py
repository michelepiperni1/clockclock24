import tkinter as tk
from analog_clock import AnalogClock

class NumberFromSixClocks:
    def __init__(self, root, row, col):
        frameGrid = tk.Frame(root, bg="#EFEFEF")
        frameGrid.grid(row=row, column = col)

        self.clocks = []

        for row in range(3):
            for col in range(2):
                clock = AnalogClock(frameGrid, 100, row, col)
                self.clocks.append(clock)
       
    def digit(self, number):
        match number:
            case 0:
                self.clocks[0].southWestLShape()     
                self.clocks[1].southEastLShape()
                self.clocks[2].verticalLine()      
                self.clocks[3].verticalLine()      
                self.clocks[4].northWestLShape()      
                self.clocks[5].northEastLShape()
            case 1:
                self.clocks[0].pointingSW()     
                self.clocks[1].bothDown()
                self.clocks[2].pointingSW()      
                self.clocks[3].verticalLine()      
                self.clocks[4].pointingSW()      
                self.clocks[5].bothUp()
            case 2:
                self.clocks[0].bothRight()     
                self.clocks[1].southEastLShape()
                self.clocks[2].southWestLShape()      
                self.clocks[3].northEastLShape()      
                self.clocks[4].northWestLShape()      
                self.clocks[5].bothLeft()
            case 3:
                self.clocks[0].bothRight()     
                self.clocks[1].southEastLShape()
                self.clocks[2].bothRight()      
                self.clocks[3].northEastLShape()      
                self.clocks[4].bothRight()       
                self.clocks[5].northEastLShape()
            case 4:
                self.clocks[0].bothDown()     
                self.clocks[1].bothDown()
                self.clocks[2].northWestLShape()      
                self.clocks[3].verticalLine()      
                self.clocks[4].pointingSW()      
                self.clocks[5].bothUp()
            case 5:
                self.clocks[0].southWestLShape()     
                self.clocks[1].bothLeft()
                self.clocks[2].northWestLShape()      
                self.clocks[3].southEastLShape()      
                self.clocks[4].bothRight()      
                self.clocks[5].northEastLShape()
            case 6:
                self.clocks[0].southWestLShape()     
                self.clocks[1].bothLeft()
                self.clocks[2].verticalLine()      
                self.clocks[3].southEastLShape()      
                self.clocks[4].northWestLShape()      
                self.clocks[5].northEastLShape()
            case 7:
                self.clocks[0].bothRight()     
                self.clocks[1].southEastLShape()
                self.clocks[2].pointingSW()      
                self.clocks[3].verticalLine()      
                self.clocks[4].pointingSW()      
                self.clocks[5].bothUp()
            case 8:
                self.clocks[0].southWestLShape()     
                self.clocks[1].southEastLShape()
                self.clocks[2].northWestLShape()      
                self.clocks[3].northEastLShape()      
                self.clocks[4].northWestLShape()      
                self.clocks[5].northEastLShape()
            case 9:
                self.clocks[0].southWestLShape()     
                self.clocks[1].southEastLShape()
                self.clocks[2].northWestLShape()      
                self.clocks[3].verticalLine()      
                self.clocks[4].bothRight()       
                self.clocks[5].northEastLShape()