from tkinter import Tk, Canvas, PhotoImage
import math
import os
import nltk
from Handlers.NLPHandler import NLPHandler

class DrawingHandler:
    """Handles drawing-related operations on a canvas."""

    def __init__(self, canvas, x, y, size=20):
        """Initialize the DrawingHandler with a canvas, position, and size.

        Args:
            canvas (Canvas): The canvas to draw on.
            x (int): The x-coordinate of the starting position.
            y (int): The y-coordinate of the starting position.
            size (int): The size of the drawing.
        """
        self.canvas = canvas
        self.size = size
        self.points = []
        self.robot_id = canvas.create_rectangle(x - size, y - size, x + size, y + size, fill="blue")
        self.width = 1
        self.current_point_index = 0
        self.move_speed = 2
        self.nlp_handler = NLPHandler()

    def draw(self, event):
        """Draw points on the canvas based on user input.

        Args:
            event: The event triggering the drawing operation.
        """
        x, y = event.x, event.y
        self.points.append((x, y))

    def process_command(self, command):
        """Process a command and generate points to follow.

        Args:
            command (str): The command to be processed.
        """
        interpreted_command = self.nlp_handler.interpret_command(command)
        self.generate_points(interpreted_command)
        self.current_point_index = 0
        self.follow_path()

    def generate_points(self, shape):
        """Generate points based on the specified shape.

        Args:
            shape (str): The shape to generate points for.
        """
        if shape == 'circle':
            x, y = self.get_position()
            radius = 50
            self.points = self.generate_circle_points(x, y, radius, num_points=100)
        elif shape == 'triangle':
            x, y = self.get_position()
            side_length = 50
            self.points = self.generate_triangle_points(x, y, side_length)
        elif shape == 'rectangle':
            x, y = self.get_position()
            width, height = 80, 40
            self.points = self.generate_rectangle_points(x, y, width, height)
        elif shape == 'ellipse':
            x, y = self.get_position()
            major_axis, minor_axis = 60, 30
            self.points = self.generate_ellipse_points(x, y, major_axis, minor_axis, num_points=100)
        elif shape == 'square':
            x, y = self.get_position()
            side_length = 50
            self.points = self.generate_square_points(x, y, side_length)
        elif shape == 'pentagon':
            x, y = self.get_position()
            side_length = 40
            self.points = self.generate_pentagon_points(x, y, side_length, num_points=100)
        elif shape == 'hexagon':
            x, y = self.get_position()
            side_length = 30
            self.points = self.generate_hexagon_points(x, y, side_length, num_points=100)
        elif shape == 'octagon':
            x, y = self.get_position()
            side_length = 35
            self.points = self.generate_octagon_points(x, y, side_length, num_points=100)
        else:
            print("Invalid shape specified.")

    def follow_path(self):
        """Follow the path by moving the drawing element on the canvas."""
        if self.current_point_index < len(self.points) - 1:
            current_x, current_y = self.get_position()
            target_x, target_y = self.points[self.current_point_index + 1]
            self.canvas.create_line(self.points[self.current_point_index], self.points[self.current_point_index + 1], fill='red', width=self.width)
            distance = math.sqrt((target_x - current_x)**2 + (target_y - current_y)**2)
            self.move_speed = max(1, min(10, distance / 100))
            dx = (target_x - current_x) / self.move_speed
            dy = (target_y - current_y) / self.move_speed

            self.move(dx, dy)
            if abs(current_x - target_x) < 1 and abs(current_y - target_y) < 1:
                self.current_point_index += 1
            self.canvas.after(10, self.follow_path)

    def move(self, dx, dy):
        """Move the drawing element on the canvas.

        Args:
            dx (float): The change in the x-coordinate.
            dy (float): The change in the y-coordinate.
        """
        self.canvas.move(self.robot_id, dx, dy)

    def get_position(self):
        """Get the current position of the drawing element.

        Returns:
            tuple: A tuple containing the x and y coordinates.
        """
        coords = self.canvas.coords(self.robot_id)
        x = (coords[0] + coords[2]) / 2
        y = (coords[1] + coords[3]) / 2
        return x, y

    def get_robot_id(self):
        """Get the ID of the drawing element on the canvas.

        Returns:
            int: The ID of the drawing element.
        """
        return self.robot_id

    def generate_circle_points(self, x, y, radius, num_points):
        """Generate points for a circle.

        Args:
            x (float): The x-coordinate of the center.
            y (float): The y-coordinate of the center.
            radius (float): The radius of the circle.
            num_points (int): The number of points to generate.

        Returns:
            list: A list of (x, y) points representing the circle.
        """
        circle_points = []
        for i in range(num_points):
            angle = (2 * math.pi * i) / num_points
            point_x = x + radius * math.cos(angle)
            point_y = y + radius * math.sin(angle)
            circle_points.append((point_x, point_y))
        return circle_points

    def generate_rectangle_points(self, x, y, width, height):
        """Generate points for a rectangle.

        Args:
            x (float): The x-coordinate of the center.
            y (float): The y-coordinate of the center.
            width (float): The width of the rectangle.
            height (float): The height of the rectangle.

        Returns:
            list: A list of (x, y) points representing the rectangle.
        """
        points = [(x - width/2, y - height/2),
                    (x + width/2, y - height/2),
                    (x + width/2, y + height/2),
                    (x - width/2, y + height/2),
                    (x - width/2, y - height/2)]
        return points

    def generate_triangle_points(self, x, y, side_length):
        """Generate points for an equilateral triangle.

        Args:
            x (float): The x-coordinate of the center.
            y (float): The y-coordinate of the center.
            side_length (float): The side length of the triangle.

        Returns:
            list: A list of (x, y) points representing the triangle.
        """
        height = (3 ** 0.5 / 2) * side_length
        x1, y1 = x, y - height / 2
        x2, y2 = x - side_length / 2, y + height / 2
        x3, y3 = x + side_length / 2, y + height / 2

        points = [(x1, y1), (x2, y2), (x3, y3)]
        points.append((x1, y1))  # Close the shape

        return points

    def generate_ellipse_points(self, center_x, center_y, major_axis, minor_axis, num_points):
        """Generate points for an ellipse.

        Args:
            center_x (float): The x-coordinate of the center.
            center_y (float): The y-coordinate of the center.
            major_axis (float): The length of the major axis.
            minor_axis (float): The length of the minor axis.
            num_points (int): The number of points to generate.

        Returns:
            list: A list of (x, y) points representing the ellipse.
        """
        points = []
        for i in range(num_points):
            angle = 2 * math.pi * i / num_points
            x = center_x + major_axis * math.cos(angle)
            y = center_y + minor_axis * math.sin(angle)
            points.append((x, y))
        return points

    def generate_square_points(self, x, y, side_length):
        """Generate points for a square.

        Args:
            x (float): The x-coordinate of the center.
            y (float): The y-coordinate of the center.
            side_length (float): The side length of the square.

        Returns:
            list: A list of (x, y) points representing the square.
        """
        points = []
        x1, y1 = x - side_length / 2, y - side_length / 2
        x2, y2 = x + side_length / 2, y - side_length / 2
        x3, y3 = x + side_length / 2, y + side_length / 2
        x4, y4 = x - side_length / 2, y + side_length / 2

        points.append((x1, y1))
        points.append((x2, y2))
        points.append((x3, y3))
        points.append((x4, y4))
        points.append((x1, y1))  # Close the shape

        return points

    def generate_pentagon_points(self, x, y, side_length, num_points):
        """Generate points for a regular pentagon.

        Args:
            x (float): The x-coordinate of the center.
            y (float): The y-coordinate of the center.
            side_length (float): The side length of the pentagon.
            num_points (int): The number of points to generate.

        Returns:
            list: A list of (x, y) points representing the pentagon.
        """
        angle_offset = math.pi / 2  # Start angle at 90 degrees
        points = []
        for i in range(num_points):
            angle = angle_offset + 2 * math.pi * i / 5
            x_i = x + side_length * math.cos(angle)
            y_i = y + side_length * math.sin(angle)
            points.append((x_i, y_i))

        return points

    def generate_hexagon_points(self, x, y, side_length, num_points):
        """Generate points for a regular hexagon.

        Args:
            x (float): The x-coordinate of the center.
            y (float): The y-coordinate of the center.
            side_length (float): The side length of the hexagon.
            num_points (int): The number of points to generate.

        Returns:
            list: A list of (x, y) points representing the hexagon.
        """
        angle_offset = 0  # Start angle at 0 degrees
        points = []
        for i in range(num_points):
            angle = angle_offset + 2 * math.pi * i / 6
            x_i = x + side_length * math.cos(angle)
            y_i = y + side_length * math.sin(angle)
            points.append((x_i, y_i))

        return points

    def generate_octagon_points(self, x, y, side_length, num_points):
        """Generate points for a regular octagon.

        Args:
            x (float): The x-coordinate of the center.
            y (float): The y-coordinate of the center.
            side_length (float): The side length of the octagon.
            num_points (int): The number of points to generate.

        Returns:
            list: A list of (x, y) points representing the octagon.
        """
        angle_offset = math.pi / 8  # Start angle at 22.5 degrees
        points = []
        for i in range(num_points):
            angle = angle_offset + 2 * math.pi * i / 8
            x_i = x + side_length * math.cos(angle)
            y_i = y + side_length * math.sin(angle)
            points.append((x_i, y_i))     
        return points