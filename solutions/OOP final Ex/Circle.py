from BasicShape import BasicShape
from Point import Point
import numpy as np
from math import pi, cos, sin
import cv2


class Circle(BasicShape):
    def __init__(self, radius: float, line_color, fill_color, rotate_angle, translation, scale_size):
        """

        :param radius: radius of the circle
        """
        super().__init__(line_color, fill_color, rotate_angle, translation, scale_size)
        self.center_point = translation
        self.radius = radius

    def draw(self, img):
        if self.fill_color:
            cv2.circle(img, self.center, radius=self.radius, color=self.line_color, thickness=-1)
        else:
            cv2.circle(img, self.center, radius=self.radius, color=self.line_color)

    def resize(self, ceneter, scale_size):
        self.radius *= scale_size

    def rotate(self, center, angle):
        pass

    def convertPointsToCenter(self):
        pass
