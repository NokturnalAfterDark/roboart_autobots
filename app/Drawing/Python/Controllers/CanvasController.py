import tkinter as tk
from tkinter import Canvas, Text
from PIL import Image
from Robot import Robot
from ChatGPTAPI import ChatGPTAPI
from Controllers.RobotController import RobotController
from appsettings import TOGGLE_NLP_CHAT_INTEGRATION

class CanvasController:
    """
    CanvasController class manages the graphical user interface for the Robotic Artist Simulation.

    Attributes:
        root (tk.Tk): The root Tkinter window.
        enable_chat (bool): Flag to enable or disable NLP ChatGPT integration.
        canvas (tk.Canvas): The canvas for drawing.
        robot_controller (RobotController): The controller for managing the robot.
        image_handler: Handles the display of images on the canvas.
        chat_app (ChatGPTAPI): The ChatGPTAPI instance for NLP chat integration.
        chat_frame (tk.Frame): The frame containing the chat window components.
        chat_display (tk.Text): The text widget for displaying chat messages.
        user_input_entry (tk.Entry): The entry widget for user input.
        send_button (tk.Button): The button to send user messages.
    """

    def __init__(self, root, image_handler):
        """
        Initializes the CanvasController with the specified root window and image handler.

        Args:
            root (tk.Tk): The root Tkinter window.
            image_handler: Handles the display of images on the canvas.
        """
        self.root = root
        self.enable_chat = TOGGLE_NLP_CHAT_INTEGRATION
        self.root.title("Robotic Artist Simulation")

        # Create canvas
        self.canvas = Canvas(root, width=400, height=400, bg="white")
        self.canvas.pack(side=tk.LEFT, expand=tk.YES, fill=tk.BOTH)

        self.robot_controller = None

        # Create image handler
        self.image_handler = image_handler
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.image_handler.photo)

        # Run Application
        self.create_chat_application()

    def send_message(self):
        """
        Sends the user input message to the chat application and the robot controller.
        """
        user_input = self.user_input_entry.get()
        self.chat_app.send_message(user_input)
        # Todo: There is a delay, which causes the application to freeze up,
        # which looks weird rendered on the UI.
        self.robot_controller.robot.process_command(user_input)

    def run(self):
        """
        Runs the Tkinter main event loop.
        """
        self.root.mainloop()

    def create_chat_display(self):
        """
        Creates a label for the chat title.
        """
        chat_title_label = tk.Label(self.root, text="NLP ChatGPT Integration", font=("Helvetica", 12, "bold"), fg="red", wraplength=150)
        chat_title_label.pack(side=tk.RIGHT, anchor=tk.N, pady=(0, 5))

        in_dev_label = tk.Label(self.root, text="(In Development)", font=("Helvetica", 12, "italic"), fg="red")
        in_dev_label.pack(side=tk.TOP, anchor=tk.N, pady=(0, 5))

    def create_chat_window(self):
        """
        Creates the chat window components.
        """
        # Create chat window
        self.create_chat_display()
        self.chat_frame = tk.Frame(self.root, width=200, height=400, bg="lightgray")
        self.chat_frame.pack(side=tk.RIGHT, fill=tk.BOTH, padx=10, pady=10)

        self.chat_display = Text(self.chat_frame, wrap="word", state="disabled", width=30, height=20)
        self.chat_display.pack(side=tk.TOP, padx=10, pady=10)

        self.user_input_entry = tk.Entry(self.chat_frame, width=30)
        self.user_input_entry.pack(side=tk.LEFT, padx=10)

        self.send_button = tk.Button(self.chat_frame, text="Send", command=self.send_message)
        self.send_button.pack(side=tk.RIGHT, padx=10)

        # Create chat application
        self.chat_app = ChatGPTAPI(self.chat_display, self.user_input_entry)

    def create_chat_application(self):
        """
        Creates the chat application based on the enable_chat flag.
        """
        if self.enable_chat:
            self.create_chat_window()
        else:
            self.chat_app = None
