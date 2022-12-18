### Author: Soulacex ###

import turtle

# Create the turtle
t = turtle.Turtle()

# Set the turtle's speed
t.speed(0)

# Set the background color
turtle.bgcolor("black")

# Set the turtle's pen color
t.pencolor("white")

# Set the turtle's pen size
t.pensize(2)

# Set the number of sides in the spiral
num_sides = 20

# Set the length of each side
side_length = 10

# Set the angle to turn after each side
angle = 90

# Draw the spiral
for i in range(num_sides):
    t.forward(side_length)
    t.right(angle)
    side_length += 5

# Keep the window open until it is closed
turtle.mainloop()
