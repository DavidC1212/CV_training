from BasicShape import BasicShape
from Point import Point
import numpy as np
from math import pi, cos, sin
import cv2


class Rectangle(BasicShape):
    def __init__(self, top_left_pt: Point, bottom_right_pt: Point, line_color: tuple, fill_color: bool, rotate_angle,
                 translation, scale_size):
        """

        :param top_left_pt: top left point of the rectangle
        :param bottom_right_pt: bottom right point of the rectangle
        """
        super().__init__(fill_color, line_color, rotate_angle, translation, scale_size)
        self.p0 = top_left_pt
        self.p1 = Point((top_left_pt.x, bottom_right_pt.y))
        self.p2 = bottom_right_pt
        self.p3 = Point((bottom_right_pt.x, top_left_pt.y))
        self.points = np.array([(self.p0.getPoint()), (self.p1.getPoint()), (self.p2.getPoint()), (self.p3.getPoint())])


    def draw(self, img):
        if self.fill_color:
            cv2.drawContours(img, [self.points], 0, color=self.line_color, thickness=-1)
        else:
            cv2.drawContours(img, [self.points], 0, color=self.line_color)

    def setPoints(self, points):
        self.p0.x, self.p0.y = points[0]
        self.p1.x, self.p1.y = points[1]
        self.p2.x, self.p2.y = points[2]
        self.p3.x, self.p3.y = points[3]
        self.points = points