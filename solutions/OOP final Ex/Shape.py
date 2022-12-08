# CR: When defining an abstract class it is advised to use abc library in python
from abc import ABC, abstractmethod


class Shape(ABC):
    def __init__(self, rotate_angle, translation, scale_size, center):
        self.rotate_angle = rotate_angle
        self.scale_size = scale_size
        self.translation = translation
        self.center = center

    @abstractmethod
    def draw(self, img):
        """
        :param img: main image of the paint
        :return: None, draw the shape
        """
        pass

    @abstractmethod
    def rotate(self, center, angle):
        """

        :param center: the center you rotate around
        :param angle: the angle of the rotation
        :return: None, rotating the shape by the given angle around the given center
        """
        pass

    @abstractmethod
    def resize(self, center, scale_size):
        """
        :param img: main image of the paint
        :return: None, draw the shape
        """
        pass

    @abstractmethod
    def convertPointsToCenter(self):
        """

        :return: None, convert points from instructions to image dimensions
        """
        pass

    def translate(self, center):
        """

        :param center: given center
        :return: None, translates the cordinates given the center
        """
        pass