from BasicShape import BasicShape
from Point import Point
import numpy as np
from math import cos, sin, pi
import cv2


class Line(BasicShape):
    def __init__(self, p1: Point, p2: Point,  line_color, rotate_angle, translation, scale_size, fill_color=False):
        """

        :param p1: first point of the line
        :param p2: second point of the line
        """
        super().__init__(fill_color, line_color,  rotate_angle, translation, scale_size)
        self.p1 = p1
        self.p2 = p2
        self.line_color = line_color

    def draw(self, img):
        cv2.line(img, self.p1.getPoint(), self.p2.getPoint(), self.line_color, 3)

    def resize(self, center, scale_size):
        points = np.array([(self.p1.getPoint()), (self.p2.getPoint())])
        c_x, c_y = center

        new_points = np.array([[
                px - int((scale_size - 1) * (c_x - px)),
                py - int((scale_size - 1) * (c_y - py))
            ] for px, py in points]).astype(int)

        self.setPoints(new_points)

    def rotate(self, center, angle):
        angle = np.deg2rad(angle)
        points = [self.p1.getPoint(), self.p2.getPoint()]
        c_x, c_y = center

        new_points = np.array([[
            c_x + np.cos(angle) * (px - c_x) - np.sin(angle) * (py - c_y),
            c_y + np.sin(angle) * (px - c_x) + np.cos(angle) * (py - c_y)
        ] for px, py in points]).astype(int)

        self.setPoints(new_points)

    def convertPointsToCenter(self):
        self.p1.x += self.center[0]
        self.p1.y = self.center[1] - self.p1.y
        self.p2.x += self.center[0]
        self.p2.y = self.center[1] - self.p2.y

    def setPoints(self, points):
        self.p1.x, self.p1.y = points[0]
        self.p2.x, self.p2.y = points[1]