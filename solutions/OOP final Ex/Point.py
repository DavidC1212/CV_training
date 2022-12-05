from BasicShape import BasicShape
import numpy as np
import cv2

class Point(BasicShape):
    def __init__(self, translation: tuple, rotate_angle=0, scale_size=1, line_color=(0,0,255), fill_color=False):
        super().__init__(fill_color, line_color, rotate_angle, translation, scale_size)
        self.x = self.translation[0]
        self.y = self.translation[1]
        self.line_color = line_color
        self.radius = 0

    def draw(self, img):
        cv2.circle(img, (self.x, self.y), radius=self.radius, color=self.line_color, thickness=-1)

    def getPoint(self):
        """

        :return: point as a tuple
        """
        return (self.x, self.y)

    def rotate(self, center, angle):
        pass

    def resize(self, center, scale_size):
        self.radius = scale_size