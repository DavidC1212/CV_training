import numpy as np
import cv2
from Shape import Shape


class BasicShape(Shape):
    def __init__(self, fill_color, line_color, rotate_angle, translation, scale_size):
        """

        :param fill_color: boolean if to fill the shape with color
        :param line_color: the color of the shape
        :param rotate_angle: the angle to rotate the shape
        :param translation: the translation of the shape in the space of the image
        :param scale_size: the scale size of the shape
        """
        super().__init__(rotate_angle, translation, scale_size)
        self.line_color = line_color
        self.fill_color = fill_color
        self.rotate_angle = rotate_angle
        self.translation = translation
        self.scale_size = scale_size

    def setPoints(self, points):
        """

        :param points: given points
        # CR: triangle?
        :return: None, sets the points to the triangle points
        """
        pass
