import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import numpy as np
import os
import Robot

from canvas_class import CanvasApp

if __name__ == "__main__":
    root = tk.Tk()
    world_boundaries = np.array([[-1.6, 1.6], [-1.6, 1.6]])
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir, "blank_canvas.jpg")
    app = CanvasApp(root, world_boundaries, image_path)
    app.run()
