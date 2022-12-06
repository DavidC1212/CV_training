from CreatorCompositeShape import CreateCompositeShape
import numpy as np
from CompositeShape import CompositeShape
import cv2


class Painter:
    def __init__(self):
        self.creator = CreateCompositeShape()

    def paintFromJson(self, instructions):
        """

        :return: None, paints from the json file
        """
        img = np.zeros((1100, 1100, 3))
        self.parsed_shape = self.creator.createParsedShape(instructions)
        self.parsed_shape.convertPointsToCenter()
        self.parsed_shape.resize(self.parsed_shape.center, self.parsed_shape.scale_size)
        self.parsed_shape.rotate(self.parsed_shape.center, self.parsed_shape.rotate_angle)
        self.parsed_shape.draw(img)
        cv2.imshow('img',img)
        cv2.waitKey(0)

if __name__ == '__main__':
    p = Painter()
    p.paintFromJson(instructions='neighbourhood.json')