import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import numpy as np

class CanvasApp:
    def __init__(self, root, world_coordinates_boundaries, image_path):
        self.root = root
        self.root.title("Canvas App")

        self.world_coordinates_boundaries = world_coordinates_boundaries

        self.canvas = Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)

        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.photo)

        self.canvas.bind("<B1-Motion>", self.draw_line)

    def world_to_pixel(self, x, y):
        x_range = [-1.6, 1.6]
        y_range = [-1.6, 1.6]

        pixel_x = np.interp(x, x_range, [0, 400])
        pixel_y = np.interp(y, y_range, [400, 0])

        return pixel_x, pixel_y

    def draw_line(self, event):
        x, y = event.x, event.y
        world_coords = self.pixel_to_world(x, y)
        print("World Coordinates:", world_coords)

        self.canvas.create_line(x - 5, y - 5, x + 5, y + 5, fill="black", width=2)
        self.canvas.create_line(x - 5, y + 5, x + 5, y - 5, fill="black", width=2)

    def pixel_to_world(self, x, y):
        x_range = [0, 400]
        y_range = [400, 0]

        world_x = np.interp(x, x_range, [-1.6, 1.6])
        world_y = np.interp(y, y_range, [-1.6, 1.6])

        return world_x, world_y