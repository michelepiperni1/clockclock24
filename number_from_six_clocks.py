import tkinter as tk
from analog_clock import AnalogClock

SW_L_SHAPE = ()

class NumberFromSixClocks:
    def __init__(self, root, row, col):
        frameGrid = tk.Frame(root, bg="#EFEFEF")
        frameGrid.grid(row=row, column = col)

        self.clocks = []

        for row in range(3):
            for col in range(2):
                clock = AnalogClock(frameGrid, 100, row, col)
                self.clocks.append(clock)
       
    def digitZero(self):
        self.clocks[0].rotateHour(0, 270)      
        self.clocks[1].rotateHour(0, 270)      
        self.clocks[1].rotateMinute(0, 180)      
        self.clocks[2].rotateMinute(0, 270)      
        self.clocks[3].rotateMinute(0, 270)      
        self.clocks[5].rotateMinute(0, 180)        

    def allHorizontal(self):
        for clock in self.clocks:
            clock.horizontalLine()