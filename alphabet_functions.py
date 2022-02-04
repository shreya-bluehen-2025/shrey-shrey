# Project 4- Alphabet Functions
# If you got help from anyone, please write their emails here:
#  1) acbart@udel.edu

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
def draw_H(x_position: int, y_position: int) -> int:
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
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
    turtle.left(90)
    return(x_position + 80)
x_position = draw_H(-300, 100)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Second Letter (E)
def draw_E(x_position: int, y_position: int) -> int:
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
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
    return(x_position + 80)
x_position = draw_E(x_position, 100)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Third Letter (L)
def draw_L(x_position: int, y_position: int) -> int:
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    return(x_position + 80)
x_position = draw_L(x_position, 100)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Fourth Letter (L)
x_position = draw_L(x_position, 100)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Fifth Letter (O)
def draw_O(x_position: int, y_position: int) -> int:
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
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
    return(x_position + 80)
draw_O(x_position, 100)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(100)
turtle.goto(-300, 0)
turtle.pendown()

turtle.color('purple')
# Sixth Letter (W)
def draw_W(x_position: int, y_position: int) -> int:
    turtle.penup()
    turtle.goto(-300, 0)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.left(135)
    turtle.forward(35)
    turtle.right(90)
    turtle.forward(35)
    turtle.left(135)
    turtle.forward(50)
    turtle.right(180)
    turtle.forward(50)
    turtle.left(90)
    return(x_position + 80)
x_position = draw_W(-300, 0)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Seventh Letter (O)
x_position = draw_O(x_position, 0)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Eight Letter (R)
def draw_R(x_position: int, y_position: int) -> int:
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(150)
    turtle.forward(57)
    turtle.left(125)
    turtle.forward(50)
    turtle.left(90)
    return (x_position + 80)
x_position = draw_R(x_position, 0)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Ninth Letter (L)
x_position = draw_L(x_position, 0)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# Tenth Letter (D)
def draw_D(x_position: int, y_position: int) -> int:
    turtle.penup()
    turtle.goto(x_position, y_position)
    turtle.pendown()
    turtle.left(90)
    turtle.forward(50)
    turtle.right(125)
    turtle.forward(50)
    turtle.right(115)
    turtle.forward(49)
    turtle.left(90)
    return (x_position + 80)
x_position = draw_D(x_position, 0)

turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 11th Letter
turtle.color("blue")
x_position = draw_D(-300, 200)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 12th Letter
x_position = draw_E(x_position, 200)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 13th Letter
x_position = draw_L(x_position, 200)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 14th Letter
x_position = draw_L(x_position, 200)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 15th Letter
turtle.color("green")
x_position = draw_H(-300, -100)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 16th Letter
x_position = draw_E(x_position, -100)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 17th Letter
x_position = draw_R(x_position, -100)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 18th Letter
x_position = draw_D(x_position, -100)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 19th Letter
turtle.color("orange")
x_position = draw_L(-300, 280)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 20th Letter
x_position = draw_E(x_position, 280)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()

# 21st Letter
x_position = draw_E(x_position, 280)

# Space for next letter
turtle.penup()
turtle.setheading(0)
turtle.forward(30)
turtle.pendown()
###############################################################
# Part 3) Wrap-up
# Start the turtles!
turtle.mainloop()

