import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
from Robot import Robot
import os

class ImageHandler:
    """Handles image-related operations in the application."""

    def __init__(self, image_path):
        """Initialize the ImageHandler with the given image path.

        Args:
            image_path (str): The path to the image file.
        """
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)
