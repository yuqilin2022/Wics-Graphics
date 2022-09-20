"""Demo file to provide examples of how Python's turtle graphic library works!"""

from turtle import colormode, done

from turtleimpl import TurtleImpl

# a link to the API docs can be found here if you want to check out the available methods:
# https://docs.python.org/3/library/turtle.html

# to have your image drawn you will need to either press the green play button in the top or
# run the following command in your terminal:
# python -m demo

# step 1: instantiating a turtle
turtle = TurtleImpl()

_turtle = turtle.get_turtle()

# step 2: calling methods on your turtle
# always use the following syntax:
# turtle_object_variable.method_name()
_turtle.forward(5)
_turtle.left(90)
_turtle.forward(10)
_turtle.right(90)
_turtle.forward(5)

# step 3: drawing shapes
# since we don't have a lot of time in the meeting, we have provided some helpful
# utility functions for drawing
# they can be found in the utility_funcs.py file
turtle.draw_circle(-50, 50, 25)
turtle.draw_square(-200, -200, 100)

# step 4: goto, penup, pendown
# prevents the turtle from drawing unwanted lines by having the "pen" on the paper as the turtle moves
_turtle.penup()
# will move a turtle to a given (x,y) location
_turtle.goto(300, 200)
# puts the turtle back on the paper to continue drawing
_turtle.pendown()
_turtle.forward(50)

# **Note: all utility functions have implemented penup(), goto(), and pendown()
# methods so stray lines are not drawn **

# step 5: pen color, fill color, & other color commands
turtle.set_color("blue")
colormode(255)
turtle.draw_circle(50, -50, 10)
# allows you to change the color of your turtle by passing in RGB values
turtle.set_color((99, 204, 250))
turtle.draw_circle(-50, -100, 10)

# in order to prevent the window from closing, place the done() function after all of your turtle drawing code
done()
