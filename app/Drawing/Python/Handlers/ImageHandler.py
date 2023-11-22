import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
from Robot import Robot
import os

class ImageHandler:
    def __init__(self, image_path):
        self.image = Image.open(image_path)
        self.photo = ImageTk.PhotoImage(self.image)