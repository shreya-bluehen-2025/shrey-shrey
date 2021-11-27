# Project 3- Turtle Alphabet
# If you got help from anyone, please write their emails here:
#  1) acbart@udel.edu
#  2) ...

###############################################################
# Part 1) Setup
# Load turtle module, move it to left side, make turtle faster
import turtle
turtle.reset()
turtle.speed(10)
turtle.penup()
turtle.goto(-300, 0)
turtle.pendown()
turtle.speed(3)

###############################################################
# Part 2) Drawing
# Write the code for each letter below

# First Letter (H)
turtle.color('pink')
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.right(180)
turtle.forward(50)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Second Letter (E)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.right(180)
turtle.forward(25)
turtle.left(90)
turtle.forward(25)
turtle.left(90)
turtle.forward(50)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Third Letter (L)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Fourth Letter (L)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Fifth Letter (O)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(180)
turtle.forward(50)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(100)
turtle.goto(-300, -100)
turtle.pendown()

# Sixth Letter (W)
turtle.color('purple')
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.left(45)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(135)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.left(90)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Seventh Letter (O)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.left(180)
turtle.forward(50)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Eight Letter (R)
turtle.left(90)
turtle.forward(50)
turtle.right(90)
turtle.forward(50)
turtle.right(150)
turtle.forward(57)
turtle.left(125)
turtle.forward(50)
turtle.left(90)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Ninth Letter (L)
turtle.left(90)
turtle.forward(50)
turtle.right(180)
turtle.forward(50)
turtle.left(90)
turtle.forward(50)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Last Letter (D)
turtle.left(90)
turtle.forward(50)
turtle.right(125)
turtle.forward(50)
turtle.right(115)
turtle.forward(49)
turtle.left(90)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

###############################################################
# Part 3) Wrap-up
# Start the turtles!
turtle.mainloop()
