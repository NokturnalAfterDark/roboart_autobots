from tkinter import Tk, Canvas, PhotoImage
import math
import os
from Handlers.NavigationHandler import NavigationHandler
from Handlers.DrawingHandler import DrawingHandler
#import RobotInterface

class Robot():
    def __init__(self, canvas, x, y, size=20):
        self.drawing_handler = NavigationHandler(canvas, x, y, size)

    def draw(self, event):
        self.drawing_handler.draw(event)

    def follow_path(self):
        self.drawing_handler.follow_path()

    def update_thickness(self, value):
        self.drawing_handler.update_thickness(value)

    def move(self, dx, dy):
        self.drawing_handler.move(dx, dy)

    def get_position(self):
        return self.drawing_handler.get_position()
    
    def process_command(self, command):
        self.drawing_handler.process_command(command)