from tkinter import Tk, Canvas, PhotoImage
import math
import os
class Robot:
    def __init__(self, canvas, x, y, size=20):
        self.canvas = canvas
        self.size = size
        self.points = []
        self.robot_id = None  # Initialize to None
        self.current_point_index = 0
        self.move_speed = 2  # Adjust the speed as needed
        self.width = 1

        # Create the initial robot

        #Todo: Switch out rectangle for robot image
        # script_dir = os.path.dirname(os.path.abspath(__file__))
        # image_path = os.path.join(script_dir, "robot_image.png")
        # x, y = 200, 200
        # size = 5
        # self.og_robot_image = PhotoImage(file=image_path)
        # self.robot_image = self.resize_image(self.og_robot_image, 10)
        # x_adjusted = x - self.size
        # y_adjusted = y - self.size

        # self.robot_id = self.canvas.create_image(x_adjusted, y_adjusted, image=self.robot_image, anchor='nw')

        self.robot_id = canvas.create_rectangle(x - size, y - size, x + size, y + size, fill="blue")

        print("Robot initialized!")
        #THIS CODE NEEDS TO BE DECOUPLED FROM THE ROBOT WHEN MERGING, TESTING ONLY

    def move(self, dx, dy):
        self.canvas.move(self.robot_id, dx, dy)

    def resize_image(self, image, new_size):
        return image.subsample(int(image.width() / new_size), int(image.height() / new_size))


    def get_position(self):
        coords = self.canvas.coords(self.robot_id)
        x = (coords[0] + coords[2]) / 2
        y = (coords[1] + coords[3]) / 2
        return x, y
    
    def draw(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))

        #self.canvas.create_line(x - 5, y - 5, x + 5, y + 5, fill="red", width=2)

    def follow_path(self):
        if self.current_point_index < len(self.points) - 1:
            current_x, current_y = self.get_position()
            #self.canvas.create_line(current_x - 5, current_y - 5, current_x + 5, current_y + 5, fill="red", width=2)
            target_x, target_y = self.points[self.current_point_index + 1]
            self.canvas.create_line(target_x - 5, target_y - 5, target_x + 5, target_y + 5, fill="red", width=self.width)

            # Calculate the distance between current and target points
            distance = math.sqrt((target_x - current_x)**2 + (target_y - current_y)**2)

            # Adjust the move_speed based on the distance
            self.move_speed = max(1, min(10, distance / 100))

            # Calculate the movement vector
            dx = (target_x - current_x) / self.move_speed
            dy = (target_y - current_y) / self.move_speed

            # Move the robot
            self.move(dx, dy)

            # Check if the robot has reached the target point
            if abs(current_x - target_x) < 1 and abs(current_y - target_y) < 1:
                self.current_point_index += 1

            # Schedule the next movement
            self.canvas.after(10, self.follow_path)