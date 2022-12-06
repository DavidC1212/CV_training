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
        # CR: Notice that all shapes have points. Point and Circle have 1 point, Line has 2, Triangle has 3 and
        # Rectangle has 4. Try to think of a way to generalize this so you don't access each point individually
        # when you come to rotate, resize and translate.s
        self.p0 = top_left_pt
        self.p1 = Point((top_left_pt.x, bottom_right_pt.y))
        self.p2 = bottom_right_pt
        self.p3 = Point((bottom_right_pt.x, top_left_pt.y))
        # CR: line_color is initialized at BasicShape, why do it again here?
        self.line_color = line_color
        self.fill_color = fill_color

    def draw(self, img):
        points = np.array([(self.p0.getPoint()), (self.p1.getPoint()), (self.p2.getPoint()), (self.p3.getPoint())])
        if self.fill_color:
            cv2.drawContours(img, [points], 0, color=self.line_color, thickness=-1)
        else:
            cv2.drawContours(img, [points], 0, color=self.line_color)

    # CR: Duplicated code. resize should basically be the same for all shapes by resizing its points around the center.
    # Try to think of a way to eliminate this duplication.
    def resize(self, center, scale_size):
        points = np.array([(self.p0.getPoint()), (self.p1.getPoint()), (self.p2.getPoint()), (self.p3.getPoint())])
        c_x, c_y = center

        new_points = np.array([[
                px - int((scale_size - 1) * (c_x - px)),
                py - int((scale_size - 1) * (c_y - py))
            ] for px, py in points]).astype(int)

        self.setPoints(new_points)

    # CR: Duplicated code. rotate should basically be the same for all shapes by rotating its points around the center.
    # Try to think of a way to eliminate this duplication.
    def rotate(self, center, angle):
        angle = np.deg2rad(angle)
        points = [self.p0.getPoint(), self.p1.getPoint(), self.p2.getPoint(), self.p3.getPoint()]
        c_x, c_y = center
        new_points = np.array([[
                c_x + np.cos(angle) * (px - c_x) - np.sin(angle) * (py - c_y),
                c_y + np.sin(angle) * (px - c_x) + np.cos(angle) * (py - c_y)
            ] for px, py in points]).astype(int)

        self.setPoints(new_points)

    # CR: Duplicated code. the same logic is done in other shapes (i.e. Triangle, but on 3 points instead of 4).
    # convertPointsToCenter (translation) should basically be the same for all shapes but on different amount of points.
    # Try to think of a way to eliminate this duplication.
    def convertPointsToCenter(self):
        points = [self.p0.getPoint(), self.p1.getPoint(), self.p2.getPoint(), self.p3.getPoint()]

        new_points = np.array([[
                px + self.center[0],
                self.center[1] - py
            ] for px, py in points]).astype(int)

        self.setPoints(new_points)

    def setPoints(self, points):
        self.p0.x, self.p0.y = points[0]
        self.p1.x, self.p1.y = points[1]
        self.p2.x, self.p2.y = points[2]
        self.p3.x, self.p3.y = points[3]