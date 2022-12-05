class Shape:
    def __init__(self, rotate_angle, translation, scale_size):
        self.rotate_angle = rotate_angle
        self.scale_size = scale_size
        self.translation = translation
        self.center = self.translation

    def draw(self, img):
        """
        :param img: main image of the paint
        :return: None, draw the shape
        """
        pass

    def rotate(self, center, angle):
        """

        :param center: the center you rotate around
        :param angle: the angle of the rotation
        :return: None, rotating the shape by the given angle around the given center
        """
        pass

    def resize(self, center, scale_size):
        """
        :param img: main image of the paint
        :return: None, draw the shape
        """
        pass

    def convertPointsToCenter(self):
        """

        :return: None, convert points from instructions to image dimensions
        """
        pass