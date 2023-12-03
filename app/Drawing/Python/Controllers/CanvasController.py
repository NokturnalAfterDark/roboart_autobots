import tkinter as tk
from tkinter import Canvas
from PIL import Image, ImageTk
from Robot import Robot

class CanvasController:
    def __init__(self, root, image_handler):
        """Initialize the CanvasController.

        Args:
            root (tk.Tk): The root Tkinter window.
            image_handler: The image handler for the canvas.

        Returns:
            None

        This method initializes the CanvasController with the specified root window and image handler.

        Example:
            canvas_controller = CanvasController(root_instance, image_handler_instance)
        """
        self.root = root
        self.root.title("Robotic Artist Simulation")

        self.canvas = Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(expand=tk.YES, fill=tk.BOTH)

        self.image_handler = image_handler
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_handler.photo)

    def run(self):
        """Run the Tkinter main event loop.

        Args:
            None

        Returns:
            None

        This method starts the Tkinter main event loop, allowing the GUI to run.

        Example:
            canvas_controller.run()
        """
        self.root.mainloop()