from tkinter import Tk, Canvas, PhotoImage
import math
import os
from Handlers.NavigationHandler import NavigationHandler
from Handlers.DrawingHandler import DrawingHandler
#import RobotInterface

class Robot:
    """Represents a robot that can move and draw on a canvas."""

    def __init__(self, canvas, x, y, size=20):
        """Initialize the Robot.

        Args:
            canvas (Canvas): The Tkinter Canvas on which the robot moves and draws.
            x (int): The initial x-coordinate of the robot.
            y (int): The initial y-coordinate of the robot.
            size (int): The size of the robot (default is 20).
        """
        self.drawing_handler = NavigationHandler(canvas, x, y, size)

    def draw(self, event):
        """Handle drawing on the canvas based on user input.

        Args:
            event (Event): The Tkinter event containing information about the user input.
        """
        self.drawing_handler.draw(event)

    def follow_path(self):
        """Follow the path on the canvas as defined by the DrawingHandler."""
        self.drawing_handler.follow_path()

    def update_thickness(self, value):
        """Update the thickness of the lines drawn on the canvas.

        Args:
            value (int): The new thickness value.
        """
        self.drawing_handler.update_thickness(value)

    def move(self, dx, dy):
        """Move the robot on the canvas.

        Args:
            dx (float): The change in the x-coordinate.
            dy (float): The change in the y-coordinate.
        """
        self.drawing_handler.move(dx, dy)

    def get_position(self):
        """Get the current position of the robot.

        Returns:
            Tuple: A tuple containing the x and y coordinates of the robot.
        """
        return self.drawing_handler.get_position()

    def process_command(self, command):
        """Process a command related to drawing shapes on the canvas.

        Args:
            command (str): The command received for drawing shapes.
        """
        self.drawing_handler.process_command(command)
