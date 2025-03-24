import tkinter as tk
import math

class AnalogClock:
    def __init__(self, root, height, row, col):
        self.root = root
        self.radius = height/2
        self.center = height/2

        #Create the canvas
        self.canvas = tk.Canvas(root, width=height, height=height, bg='#EFEFEF', highlightthickness=0)
        self.canvas.grid(row=row, column=col, padx=5, pady=5)
    
        # Draw the clock face
        self.canvas.create_oval(0, 0, height, height, fill='#E3E3E3', width=0) 

        # Draw the clock hands
        self.hourAngle = 90
        self.hourRotations = 0
        self.hour_hand = self.canvas.create_line(self.center, self.center, self.center, 0, fill='black', width=height/10)
        
        self.minuteAngle = 0
        self.minuteRotations = 0
        self.minute_hand = self.canvas.create_line(self.center, self.center, height, self.center, fill='black', width=height/10) 

        # Draw the middle to round off the hands
        centerTopLeft = height/2 - height/20
        centerBottomRight = height/2 + height/20 - 1
        self.canvas.create_oval(centerTopLeft, centerTopLeft, centerBottomRight, centerBottomRight, fill='black', outline='black')
    
    def rotateMinute(self, endAngle):
        newX = self.radius + math.cos(math.radians(self.minuteAngle)) * self.radius
        newY = self.radius - math.sin(math.radians(self.minuteAngle)) * self.radius
        self.canvas.coords(self.minute_hand, self.center, self.center, newX, newY) 

        self.minuteAngle += 1
        if self.minuteAngle > endAngle and self.minuteRotations != 0: 
            self.minuteRotations = 0
            return
        if self.minuteAngle >= 360 or self.minuteAngle <= -360: 
            self.minuteRotations += 1 
            self.minuteAngle = 0  # Reset after full rotation

        self.root.after(10, lambda: self.rotateMinute(endAngle))

    def rotateHour(self, endAngle):
        newX = self.radius + math.cos(math.radians(self.hourAngle)) * self.radius
        newY = self.radius - math.sin(math.radians(self.hourAngle)) * self.radius
        self.canvas.coords(self.hour_hand, self.center, self.center, newX, newY) 

        self.hourAngle += 1
        if self.hourAngle > endAngle and self.hourRotations != 0: 
            self.hourRotations = 0
            return
        if self.hourAngle >= 360 or self.hourAngle <= -360:
            self.hourRotations += 1 
            self.hourAngle = 0  # Reset after full rotation

        self.root.after(10, lambda: self.rotateHour(endAngle))

    def horizontalLine(self):
        self.rotateHour(0)
        self.rotateMinute(180)

    def verticalLine(self):
        self.rotateHour(90)
        self.rotateMinute(270)

    def northWestLShape(self):
        self.rotateHour(90)
        self.rotateMinute(0)

    def northEastLShape(self):
        self.rotateHour(90)
        self.rotateMinute(180)

    def southWestLShape(self):
        self.rotateHour(270)
        self.rotateMinute(0)

    def southEastLShape(self):
        self.rotateHour(270)
        self.rotateMinute(180)

    def pointingSW(self):
        self.rotateHour(225)
        self.rotateMinute(225)

    def bothUp(self):
        self.rotateHour(90)
        self.rotateMinute(90)

    def bothDown(self):
        self.rotateHour(270)
        self.rotateMinute(270)

    def bothLeft(self):
        self.rotateHour(180)
        self.rotateMinute(180)

    def bothRight(self):
        self.rotateHour(0)
        self.rotateMinute(0)