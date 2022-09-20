import math
from turtle import colormode, Turtle
from typing import Union, Tuple


NINETY_DEGREE_TURN: float = 90
FASTEST_SPEED: float = 0
SETHEADING: float = 0.0


class TurtleImpl:
    def __init__(self):
        self.turtle = Turtle()
        self.color = "black"

        colormode(255)

    def set_color(self, color: Union[str, Tuple]):
        """Sets the color of the turtle."""
        if type(color) == str:
            self.turtle.color(color)
        else:
            self.turtle.color(color[0], color[1], color[2])

    def get_turtle(self):
        return self.turtle

    def draw_rectangle(self, x: float, y: float, length: float, width: float, fill=True) -> None:
        """Draws a rectangle starting at top left corner located at x, y."""
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(SETHEADING)
        self.turtle.pendown()
        self.turtle.speed(FASTEST_SPEED)
        i: int = 0
        if fill:
            self.turtle.begin_fill()
            while i < 2:
                self.turtle.forward(width)
                self.turtle.right(NINETY_DEGREE_TURN)
                self.turtle.forward(length)
                self.turtle.right(NINETY_DEGREE_TURN)
                i = i + 1
            self.turtle.end_fill()
        else:
            while i < 2:
                self.turtle.forward(width)
                self.turtle.right(NINETY_DEGREE_TURN)
                self.turtle.forward(length)
                self.turtle.right(NINETY_DEGREE_TURN)
                i = i + 1
        self.turtle.hideturtle()
        return None

    def draw_square(self, x: float, y: float, width: float, fill=True) -> None:
        """Draws square starting at top-left corner located at x, y."""
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(SETHEADING)
        self.turtle.pendown()
        self.turtle.speed(FASTEST_SPEED)
        i: int = 0
        if fill:
            self.turtle.begin_fill()
            while i < 4:
                self.turtle.forward(width)
                self.turtle.right(NINETY_DEGREE_TURN)
                i = i + 1
            self.turtle.end_fill()
        else:
            while i < 4:
                self.turtle.forward(width)
                self.turtle.right(NINETY_DEGREE_TURN)
                i = i + 1
        self.turtle.hideturtle()
        return None

    def draw_right_triangle(self, x: float, y: float, set_turn: float, leg_1: float, turn_1: float,
                            leg_2: float, turn_2: float, fill=True) -> None:
        """Draws right rectangle starting at bottom left corner located at x, y."""
        hypotenuse = int(math.sqrt(leg_1**2 + leg_2**2))
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(SETHEADING)
        self.turtle.pendown()
        self.turtle.speed(FASTEST_SPEED)
        if fill:
            self.turtle.begin_fill()
            self.turtle.left(set_turn)
            self.turtle.forward(leg_1)
            self.turtle.left(turn_1)
            self.turtle.forward(leg_2)
            self.turtle.left(turn_2)
            self.turtle.forward(hypotenuse)
            self.turtle.end_fill()
        else:
            self.turtle.left(set_turn)
            self.turtle.forward(leg_1)
            self.turtle.left(turn_1)
            self.turtle.forward(leg_2)
            self.turtle.left(turn_2)
            self.turtle.forward(hypotenuse)
        self.turtle.hideturtle()
        return None

    def draw_circle(self, x: float, y: float, radius: float, fill=True) -> None:
        """Draws circle centered at x, y with a radius of radius."""
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(SETHEADING)
        self.turtle.pendown()
        self.turtle.speed(FASTEST_SPEED)
        if fill:
            self.turtle.begin_fill()
            self.turtle.circle(radius)
            self.turtle.end_fill()
        else:
            self.turtle.circle(radius)
        self.turtle.hideturtle()
        return None

    def draw_line(self, x: float, y: float, length: float, direction: float) -> None:
        """Draws line with length of length at angle of direction."""
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(SETHEADING)
        self.turtle.pendown()
        self.turtle.speed(FASTEST_SPEED)
        self.turtle.right(direction)
        self.turtle.forward(length)
        self.turtle.hideturtle()
        return None

    def draw_equilateral_tri(self, x: float, y: float, set_turn: float, side_1: float, turn_1: float,
                             side_2: float, turn_2: float, side_3: float, fill=True) -> None:
        """Draws equilateral triangle starting at bottom left corner located at x, y."""
        self.turtle.penup()
        self.turtle.goto(x, y)
        self.turtle.setheading(SETHEADING)
        self.turtle.pendown()
        self.turtle.speed(FASTEST_SPEED)
        if fill:
            self.turtle.begin_fill()
            self.turtle.left(set_turn)
            self.turtle.forward(side_1)
            self.turtle.left(turn_1)
            self.turtle.forward(side_2)
            self.turtle.left(turn_2)
            self.turtle.forward(side_3)
            self.turtle.end_fill()
        else:
            self.turtle.left(set_turn)
            self.turtle.forward(side_1)
            self.turtle.left(turn_1)
            self.turtle.forward(side_2)
            self.turtle.left(turn_2)
            self.turtle.forward(side_3)
        self.turtle.hideturtle()
        return None
