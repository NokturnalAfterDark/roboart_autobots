from tkinter import Tk, Canvas, PhotoImage
import math
import os

class DrawingHandler:
    def __init__(self, canvas, x, y, size=20):
        self.canvas = canvas
        self.size = size
        self.points = []
        self.robot_id = canvas.create_rectangle(x - size, y - size, x + size, y + size, fill="blue")
        self.width = 1
        self.current_point_index = 0
        self.move_speed = 2

    def draw(self, event):
        x, y = event.x, event.y
        self.points.append((x, y))

    def follow_path(self):
        if self.current_point_index < len(self.points) - 1:
            current_x, current_y = self.get_position()
            target_x, target_y = self.points[self.current_point_index + 1]
            self.canvas.create_line(target_x - 5, target_y - 5, target_x + 5, target_y + 5, fill="red", width=self.width)
            distance = math.sqrt((target_x - current_x)**2 + (target_y - current_y)**2)
            self.move_speed = max(1, min(10, distance / 100))
            dx = (target_x - current_x) / self.move_speed
            dy = (target_y - current_y) / self.move_speed
            self.move(dx, dy)
            if abs(current_x - target_x) < 1 and abs(current_y - target_y) < 1:
                self.current_point_index += 1
            self.canvas.after(10, self.follow_path)

    def move(self, dx, dy):
        self.canvas.move(self.robot_id, dx, dy)

    def get_position(self):
        coords = self.canvas.coords(self.robot_id)
        x = (coords[0] + coords[2]) / 2
        y = (coords[1] + coords[3]) / 2
        return x, y

    def get_robot_id(self):
        return self.robot_id