import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
from Robot import Robot

class RobotController:
    def __init__(self, canvas, world_coordinates_boundaries):
        """Initialize the RobotController.

        Args:
            canvas (tk.Canvas): The tkinter Canvas where the robot will be displayed.
            world_coordinates_boundaries: The boundaries of the world coordinates.

        Returns:
            None

        This method initializes the RobotController with the specified canvas and world coordinate boundaries.

        Example:
            controller = RobotController(canvas_instance, boundaries_instance)
        """
        self.robot = Robot(canvas, x=200, y=200)
        # Bring the robot to the front
        canvas.tag_raise(self.robot.drawing_handler.get_robot_id())

        self.world_coordinates_boundaries = world_coordinates_boundaries

        #Todo: We might be able to decouple this (scaling widget for thickness, submit button) now that the RobotController instance is being passed to the CanvasController.

        # Add a Scale widget for controlling line thickness

        congfig_settings = tk.Label(canvas.master, text="SETTINGS: ", font=("Helvetica", 12, "bold"))
        congfig_settings.pack()
        self.thickness_scale = tk.Scale(canvas.master, from_=1, to=10, orient=tk.HORIZONTAL, label="Line Thickness",
                                        command=self.update_thickness)
        self.thickness_scale.pack()
        self.line_thickness = 1

        # Create a textbox (Entry widget) and a submit button
        chat_title_label = tk.Label(canvas.master, text="NLP Shape Prompt: ", font=("Helvetica", 12, "bold"))
        chat_title_label.pack()

        entry = tk.Entry(canvas.master)
        entry.pack()

        submit_button = tk.Button(canvas.master, text="Submit", command=lambda: self.robot.process_command(entry.get()))
        submit_button.pack()

        canvas.bind("<B1-Motion>", self.robot.draw)
        canvas.bind("<ButtonRelease-1>", lambda event: self.robot.follow_path())
        
    def update_thickness(self, value):
        """Update the line thickness based on the specified value.

        Args:
            value (int): The new line thickness value.

        Returns:
            None

        This method updates the line thickness of the robot's drawing.

        Example:
            update_thickness(2)
        """
        self.line_thickness = int(value)
        # Plugging in the width so the robot can adjust for various thicknesses
        self.robot.update_thickness(value)