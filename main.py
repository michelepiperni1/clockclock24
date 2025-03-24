import tkinter as tk
from number_from_six_clocks import NumberFromSixClocks
import time

if __name__ == "__main__":
    root = tk.Tk()
    root.title("ClockClock24")
    root.configure(bg="#EFEFEF")
    root.geometry("1000x400")

    frame = tk.Frame(root, bg="#EFEFEF")
    frame.place(relx=0.5, rely=0.5, anchor="center")  # Center frame in the window
    digits  = []

    for col in range(4):
        digit = NumberFromSixClocks(frame, 0, col)
        digits.append(digit)

    # Function to update the time
    def update_clock():
        hour = time.strftime("%I")
        hourDigit1, hourDigit2 = int(hour[0]), int(hour[1])

        minute = time.strftime("%M")
        minuteDigit1, minuteDigit2 = int(minute[0]), int(minute[1])

        digits[0].digit(hourDigit1)
        digits[1].digit(hourDigit2)
        digits[2].digit(minuteDigit1)
        digits[3].digit(minuteDigit2)

        root.after(60000, update_clock)  # Update every 60 second

    # Start updating the clock
    update_clock()

    root.mainloop()