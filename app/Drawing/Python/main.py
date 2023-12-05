import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
import numpy as np
import os
import Robot
from Controllers.CanvasController import CanvasController
from Handlers.ImageHandler import ImageHandler
from Controllers.RobotController import RobotController
from ChatGPTAPI import ChatGPTAPI

if __name__ == "__main__":
    root = tk.Tk()
    world_boundaries = np.array([[-1.6, 1.6], [-1.6, 1.6]])
    script_dir = os.path.dirname(os.path.abspath(__file__))
    image_path = os.path.join(script_dir+"\\Images\\", "blank_canvas.jpg")

    image_handler = ImageHandler(image_path)
    canvas_controller = CanvasController(root, image_handler)
    robot_controller = RobotController(canvas_controller.canvas, world_boundaries)
    canvas_controller.robot_controller = robot_controller
    chat_app = ChatGPTAPI(root, robot_controller)

    canvas_controller.run()
