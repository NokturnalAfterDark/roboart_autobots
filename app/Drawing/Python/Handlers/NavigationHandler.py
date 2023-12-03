from tkinter import Tk, Canvas, PhotoImage
import math
import os
from Handlers.DrawingHandler import DrawingHandler

class NavigationHandler:
    def __init__(self, canvas, x, y, size=20):
        self.drawing_handler = DrawingHandler(canvas, x, y, size)

    def draw(self, event):
        self.drawing_handler.draw(event)

    def follow_path(self):
        self.drawing_handler.follow_path()

    def update_thickness(self, value):
        self.drawing_handler.width = int(value)

    def move(self, dx, dy):
        self.drawing_handler.move(dx, dy)

    def get_position(self):
        return self.drawing_handler.get_position()

    def get_robot_id(self):
        return self.drawing_handler.get_robot_id()
    
    def process_command(self, command):
        self.drawing_handler.process_command(command)