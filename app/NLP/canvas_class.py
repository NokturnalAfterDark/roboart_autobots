import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import numpy as np
import os
from Robot import Robot  # Import the Robot class from robot.py
import turtle

class CanvasApp:
    def __init__(self, root, world_coordinates_boundaries, image_path):
        self.root = root
        self.root.title("Robotic Artist Simulation")

        self.world_coordinates_boundaries = world_coordinates_boundaries

        self.canvas = Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
        self.robot = Robot(self.canvas, x=200, y=200)
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        # Bring the robot to the front
        self.canvas.tag_raise(self.robot.robot_id)
        # Add a Scale widget for controlling line thickness
        self.thickness_scale = tk.Scale(root, from_=1, to=10, orient=tk.HORIZONTAL, label="Line Thickness",
                                        command=self.update_thickness)
        self.thickness_scale.pack()
        self.canvas.bind("<B1-Motion>", self.robot.draw)
        self.canvas.bind("<ButtonRelease-1>", lambda event: self.robot.follow_path())
        self.line_thickness = 1

    def update_thickness(self, value):
        self.line_thickness = int(value)
        #Plugging in the width so the robot can adjust for various thicknesses
        self.robot.width = int(value)
    
    def run(self):
        self.root.mainloop()  