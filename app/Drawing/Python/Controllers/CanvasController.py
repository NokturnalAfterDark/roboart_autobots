import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
from Robot import Robot

class CanvasController:
    def __init__(self, root, image_handler):
        self.root = root
        self.root.title("Robotic Artist Simulation")

        self.canvas = Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.image_handler = image_handler
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_handler.photo)

    def run(self):
        self.root.mainloop()