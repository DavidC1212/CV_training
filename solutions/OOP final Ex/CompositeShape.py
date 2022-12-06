from Shape import Shape
from Triangle import Triangle
from Point import Point
from Circle import Circle
from Rectangle import Rectangle
from Line import Line
from utils import convertStringsToTypes

SHAPES = ['triangle', 'point', 'circle', 'rectangle', 'line']
# CR: CompositeShape should not be coupled with the basic shapes and know what they are (what if I were to add another
# shape?). Refactor the code so that the factory (Creator) is the only class that "knows" the details of Shapes and how
# to create them.

class CompositeShape(Shape):
    def __init__(self, children, name, rotate_angle, translation, scale_size):
        """

        :param children: the sub-shapes of the composite shapes
        :param name: name of the shape, given in the instructions
        """
        super().__init__(rotate_angle, translation, scale_size)
        self.children = children
        self.name = name
        self.rotate_angle = rotate_angle
        self.translation = translation
        self.scale_size = scale_size
        self.children_rotated = False
        self.children_resized = False

    # CR: CompositeShape should interact purely with other shapes (not to know at all that there is a JSON behind the
    # scenes. Refactor your code in such a way that you need not call convertStringToTypes or construct shapes from
    # within CompositeShape (Creator should be responsible to all the constructions).
    def add(self, shape):
        """

        :param shape: given sub-shape of the composite shape
        :return: None, adds the sub-shape to the composite shape children's
        """
        self.children.append(shape)

    def draw(self, img):
        for child in self.children:
            child.draw(img)

    def rotate(self, center, rotate_angle):
        if not self.children_rotated:
            for child in self.children:
                child.rotate(child.center, child.rotate_angle)

        self.children_rotated = True

        for child in self.children:
            child.rotate(center, rotate_angle)

    def resize(self, center, scale_size):
        if not self.children_resized:
            for child in self.children:
                child.resize(child.center, child.scale_size)

        self.children_resized = True

        for child in self.children:
            child.resize(center, scale_size)

    def convertPointsToCenter(self):
        for child in self.children:
            child.convertPointsToCenter()
