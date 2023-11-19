import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import numpy as np

from canvas_class import CanvasApp

if __name__ == "__main__":
    root = tk.Tk()
    world_boundaries = np.array([[-1.6, 1.6], [-1.6, 1.6]])
    image_path = "path/to/your/white-empty-canvas.jpg"  # Replace with the actual path
    app = CanvasApp(root, world_boundaries, image_path)
    root.mainloop()
