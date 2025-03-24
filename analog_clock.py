import tkinter as tk
import math

class AnalogClock:
    def __init__(self, root, height, row, col):
        self.root = root
        self.radius = height/2
        self.center = height/2

        #Create the canvas
        self.canvas = tk.Canvas(root, width=height, height=height, bg='#EFEFEF', highlightthickness=0)
        self.canvas.grid(row=row, column=col, padx=5, pady=5)  # Add padding for spacing
    
        # Draw the clock face
        self.canvas.create_oval(0, 0, height, height, fill='#E3E3E3', width=0) 

        # Draw the clock hands
        self.hour_hand = self.canvas.create_line(self.center, self.center, self.center, 0, fill='black', width=height/10)
        self.minute_hand = self.canvas.create_line(self.center, self.center, height, self.center, fill='black', width=height/10) 

        # Draw the middle to round off the hands
        centerTopLeft = height/2 - height/20
        centerBottomRight = height/2 + height/20 - 1
        self.canvas.create_oval(centerTopLeft, centerTopLeft, centerBottomRight, centerBottomRight, fill='black', outline='black')
    
    def rotateMinute(self, angle, endAngle):
        angleR = math.radians(angle)
        newX = self.radius + math.cos(angleR) * self.radius
        newY = self.radius - math.sin(angleR) * self.radius
        self.canvas.coords(self.minute_hand, self.center, self.center, newX, newY) 

        angle += 1
        if(angle > endAngle): return
        if angle >= 360 or angle <= -360: angle = 0  # Reset after full rotation

        self.root.after(10, lambda: self.rotateMinute(angle, endAngle))

    def rotateHour(self, angle, endAngle):
        angleR = math.radians(angle)
        newX = self.radius + math.cos(angleR) * self.radius
        newY = self.radius - math.sin(angleR) * self.radius
        self.canvas.coords(self.hour_hand, self.center, self.center, newX, newY) 

        angle += 1
        if(angle > endAngle): return
        if angle >= 360 or angle <= -360: angle = 0  # Reset after full rotation

        self.root.after(10, lambda: self.rotateHour(angle, endAngle))

    def horizontalLine(self):
        self.rotateHour(90, 180)
        self.rotateMinute(359, 360)
