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
        self.points = np.array([(self.p1.getPoint()), (self.p2.getPoint())])

    def draw(self, img):
        cv2.line(img, self.p1.getPoint(), self.p2.getPoint(), self.line_color, 3)

    def setPoints(self, points):
        self.p1.x, self.p1.y = points[0]
        self.p2.x, self.p2.y = points[1]
        self.points = points