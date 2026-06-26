from tkinter import *
import time
from Ball import Ball  # Import the Ball class

# Initialize window
window = Tk()
window.geometry("1080x720")
WIDTH, HEIGHT = 1080, 720

canvas = Canvas(window, width=WIDTH, height=HEIGHT, bg="black")
canvas.pack()

# Create Ball instance
ball = Ball(canvas, x=50, y=50, diameter=50, xvelocity=5, yvelocity=3, color="white")

# Animation loop
def animate():
    while True:
        ball.move(WIDTH, HEIGHT)
        window.update()
        time.sleep(0.01)  # Controls speed

# Run animation
animate()

window.mainloop()