from Creator import Creator
import numpy as np
from CompositeShape import CompositeShape
import cv2


class Painter:
    def __init__(self, instructions):
        """

        :param instructions: instructions of the painting
        """
        self.instructions = instructions
        self.creator = Creator()

        self.parsed_shape = self.creator.createCompositeShape(instructions)

    def paintFromJson(self):
        """

        :return: None, paints from the json file
        """
        img = np.zeros((1100, 1200, 3))
        self.parsed_shape.convertPointsToCenter()
        self.parsed_shape.resize(self.parsed_shape.center, self.parsed_shape.scale_size)
        self.parsed_shape.rotate(self.parsed_shape.center, self.parsed_shape.rotate_angle)
        self.parsed_shape.draw(img)
        cv2.imshow('img',img)
        cv2.waitKey(0)

if __name__ == '__main__':
    p = Painter(instructions='neighbourhood.json')
    p.paintFromJson()