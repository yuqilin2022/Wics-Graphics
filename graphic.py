"""Here is the file where you will design your graphic for the WiCS website."""

# Remember: to get your image to be drawn press the green play button or run the following command in the terminal:
# python -m graphic

from turtleimpl import *
from turtle import Screen, done

# you can change the size of your image here
PIXEL_WIDTH: int = 800
PIXEL_HEIGHT: int = 800


def main() -> None:
    """Entrypoint of your graphic drawing. Place all code to be drawn here."""
    screen_setup(PIXEL_WIDTH, PIXEL_HEIGHT)
    turtle1 = TurtleImpl()
    # insert drawing code here
    #
    #
    #
    done()
    return None


def screen_setup(pixel_width, pixel_height) -> None:
    """Function to set up window size for your image."""
    screen = Screen()
    screen.setup(pixel_width, pixel_height, None, None)
    return None


if __name__ == "__main__":
    main()
