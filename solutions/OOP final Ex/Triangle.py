from BasicShape import BasicShape
from Point import Point
import numpy as np
from math import pi, cos, sin
import cv2


class Triangle(BasicShape):
    def __init__(self, p1: Point, p2: Point, p3: Point, line_color: tuple, fill_color: bool, rotate_angle, translation,
                 scale_size):
        """

        :param p1: first point of the triangle
        :param p2: second point of the triangle
        :param p3: third point of the triangle
        """
        super().__init__(fill_color, line_color, rotate_angle, translation, scale_size)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.line_color = line_color
        self.fill_color = fill_color

    def draw(self, img):
        if self.fill_color:
            triangle_cnt = np.array([self.p1.getPoint(), self.p2.getPoint(), self.p3.getPoint()])
            cv2.drawContours(img, [triangle_cnt], 0, self.line_color, -1)
        else:
            cv2.line(img, self.p1.getPoint(), self.p2.getPoint(), self.line_color, 3)
            cv2.line(img, self.p2.getPoint(), self.p3.getPoint(), self.line_color, 3)
            cv2.line(img, self.p1.getPoint(), self.p3.getPoint(), self.line_color, 3)

    def resize(self, center, scale_size):
        points = np.array([(self.p1.getPoint()), (self.p2.getPoint()), (self.p3.getPoint())])
        c_x, c_y = center

        new_points = np.array([[
                px - int((scale_size - 1) * (c_x - px)),
                py - int((scale_size - 1) * (c_y - py))
            ] for px, py in points]).astype(int)

        self.setPoints(new_points)

    def rotate(self, center, angle):
        angle = np.deg2rad(angle)
        points = [self.p1.getPoint(), self.p2.getPoint(), self.p3.getPoint()]
        c_x, c_y = center
        new_points = np.array([[
            c_x + np.cos(angle) * (px - c_x) - np.sin(angle) * (py - c_y),
            c_y + np.sin(angle) * (px - c_x) + np.cos(angle) * (py - c_y)
        ] for px, py in points]).astype(int)

        self.setPoints(new_points)

    def convertPointsToCenter(self):
        self.p1.x = self.p1.x + self.center[0]
        self.p1.y = self.center[1] - self.p1.y
        self.p2.x = self.p2.x + self.center[0]
        self.p2.y = self.center[1] - self.p2.y
        self.p3.x = self.p3.x + self.center[0]
        self.p3.y = self.center[1] - self.p3.y

    def setPoints(self, points):
        self.p1.x, self.p1.y = points[0]
        self.p2.x, self.p2.y = points[1]
        self.p3.x, self.p3.y = points[2]