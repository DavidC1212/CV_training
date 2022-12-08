import numpy as np
import cv2
from Shape import Shape


class BasicShape(Shape):
    def __init__(self, fill_color, line_color, rotate_angle, translation, scale_size, center):
        """

        :param fill_color: boolean if to fill the shape with color
        :param line_color: the color of the shape
        :param rotate_angle: the angle to rotate the shape
        :param translation: the translation of the shape in the space of the image
        :param scale_size: the scale size of the shape
        :param center: the center of the shape
        """
        super().__init__(rotate_angle, translation, scale_size, center)
        self.points = None
        self.line_color = line_color
        self.fill_color = fill_color

    def setPoints(self, points):
        """

        :param points: given points
        :return: None, sets the points to the given shape
        """
        pass

    def rotate(self, center, angle):
        angle = np.deg2rad(angle)
        points = self.points
        c_x, c_y = center
        new_points = np.array([[
                c_x + np.cos(angle) * (px - c_x) - np.sin(angle) * (py - c_y),
                c_y + np.sin(angle) * (px - c_x) + np.cos(angle) * (py - c_y)
            ] for px, py in points]).astype(int)

        self.setPoints(new_points)

    def resize(self, center, scale_size):
        points = self.points
        c_x, c_y = center

        new_points = np.array([[
                px - int((scale_size - 1) * (c_x - px)),
                py - int((scale_size - 1) * (c_y - py))
            ] for px, py in points]).astype(int)

        self.setPoints(new_points)

    def convertPointsToCenter(self):
        points = self.points

        new_points = np.array([[
                px + self.center[0],
                self.center[1] - py
            ] for px, py in points]).astype(int)

        self.setPoints(new_points)

    def translate(self, center):
        self.center = center[0] + self.translation[0],  center[1] - self.translation[1]