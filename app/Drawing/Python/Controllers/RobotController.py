import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
from Robot import Robot
#from Handlers.NLPHandler import NLPHandler

class RobotController:
    def __init__(self, canvas, world_coordinates_boundaries):
        self.robot = Robot(canvas, x=200, y=200)
        # Bring the robot to the front
        canvas.tag_raise(self.robot.drawing_handler.get_robot_id())

        self.world_coordinates_boundaries = world_coordinates_boundaries

        # Add a Scale widget for controlling line thickness
        self.thickness_scale = tk.Scale(canvas.master, from_=1, to=10, orient=tk.HORIZONTAL, label="Line Thickness",
                                        command=self.update_thickness)
        self.thickness_scale.pack()
        canvas.bind("<B1-Motion>", self.robot.draw)
        canvas.bind("<ButtonRelease-1>", lambda event: self.robot.follow_path())
        self.line_thickness = 1

    def update_thickness(self, value):
        self.line_thickness = int(value)
        # Plugging in the width so the robot can adjust for various thicknesses
        self.robot.update_thickness(value)

    # def process_command(self, command):
    #     self.nlp_handler.process_command(command)