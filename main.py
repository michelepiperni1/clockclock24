import tkinter as tk
from number_from_six_clocks import NumberFromSixClocks

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ClockClock24")
    root.configure(bg="#EFEFEF")
    root.geometry("1000x400")

    frame = tk.Frame(root, bg="#EFEFEF")
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Center frame in the window

    for col in range(4):
        digit = NumberFromSixClocks(frame, 0, col)
        digit.digitZero()
        # digit1.allHorizontal()

    root.mainloop()