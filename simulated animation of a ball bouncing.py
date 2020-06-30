import tkinter as tk
import numpy as np

size = w, h = 700, 700  # pixels

root = tk.Tk()
root.title("Boing!")
canvas = tk.Canvas(root, width=w, height=h)
canvas.pack()
g = 10
r = np.array([350., 350., 10., 0.])
c = r[1]


# Stepper function to update the state of the system (i.e. the position and velocity of the ball)
def step(dt):
    # Save a copy of the original state
    r0 = r.copy()

    # Update the position using the Euler method - nice and easy!
    r[:2] += r[2:] * dt
    r[3] += g
    # bounce off walls. Reverse x component of velocity and correct ball overshoot
    if r[0] > (w - rball):
        r[2] *= -1.
        r[0] += w - rball - r[0] - 1.
    if r[0] < rball:
        r[2] *= -1.
        r[0] += rball - r[0] + 1
    if r[1] > (h - rball):
        r[1] += (h - rball) - r[1] + (r[3] - r0[3])
        r[3] -= (r[3] - r0[3])
        r[3] *= -1

    print(r[1])

    # Find difference of the original and new position and pass to move function
    dx = r[0] - r0[0]
    dy = r[1] - r0[1]
    canvas.move(ball, dx, dy)




# Ball radius
rball = 40

# Get the 4 corners of a box surrounding each ball and draw a circle
x1, y1, x2, y2 = r[0] - rball, r[1] - rball, r[0] + rball, r[1] + rball
ball = canvas.create_oval(x1, y1, x2, y2, fill='blue')


# This bit repeatedly calls the stepper function after a short (1 ms) interval
def animation():
    """docstring for animation"""
    step(0.1)
    root.after(40, animation)


root.after(0, animation)
root.mainloop()