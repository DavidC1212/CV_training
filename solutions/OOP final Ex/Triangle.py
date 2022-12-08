from BasicShape import BasicShape
from Point import Point
import numpy as np
from math import pi, cos, sin
import cv2


class Triangle(BasicShape):
    def __init__(self, p1: Point, p2: Point, p3: Point, line_color: tuple, fill_color: bool, rotate_angle, translation,
                 scale_size, center):
        """

        :param p1: first point of the triangle
        :param p2: second point of the triangle
        :param p3: third point of the triangle
        """
        super().__init__(fill_color, line_color, rotate_angle, translation, scale_size, center)
        self.p1 = p1
        self.p2 = p2
        self.p3 = p3
        self.points = np.array([(self.p1.getPoint()), (self.p2.getPoint()), (self.p3.getPoint())])

    def draw(self, img):
        if self.fill_color:
            cv2.drawContours(img, [self.points], 0, self.line_color, -1)
        else:
            cv2.line(img, self.p1.getPoint(), self.p2.getPoint(), self.line_color, 3)
            cv2.line(img, self.p2.getPoint(), self.p3.getPoint(), self.line_color, 3)
            cv2.line(img, self.p1.getPoint(), self.p3.getPoint(), self.line_color, 3)


    def setPoints(self, points):
        self.p1.x, self.p1.y = points[0]
        self.p2.x, self.p2.y = points[1]
        self.p3.x, self.p3.y = points[2]
        self.points = points