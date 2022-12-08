from Creator import Creator
from Point import Point
from Circle import Circle
from Rectangle import Rectangle
from Line import Line
from Triangle import Triangle


class CreatorBasicShape(Creator):
    def __init__(self):
        """
        Class that creates basic shapes
        """
        super().__init__()
        self.shapes = {'Point': self.createPoint,
                       'Circle': self.createCircle,
                       'Rectangle': self.createRectangle,
                       'Line': self.createLine,
                       'Triangle': self.createTriangle}

    def createShape(self, center, instructions):
        return self.shapes[list(instructions.keys())[0]](center, list(instructions.values())[0])

    def createPoint(self, center, instructions):
        """

        :param center: center of the shape
        :param instructions: instructions of the given shape
        :return: Point with the given instructions
        """
        return Point(line_color=instructions[1], fill_color=instructions[2],
                     rotate_angle=instructions[3], translation=(instructions[4][0],
                     instructions[4][1]),
                     scale_size=instructions[5], center=center)

    def createCircle(self, center, instructions):
        """

        :param center: center of the shape
        :param instructions: instructions of the given shape
        :return: Circle with the given instructions
        """
        return Circle(radius=instructions[1], line_color=instructions[2],
                      fill_color=instructions[3], rotate_angle=instructions[4],
                      translation=(instructions[4][0],
                      instructions[4][1]),
                      scale_size=instructions[6], center=center)

    def createRectangle(self, center, instructions):
        """

        :param center: center of the shape
        :param instructions: instructions of the given shape
        :return: Rectangle with the given instructions
        """
        return Rectangle(top_left_pt=Point(instructions[0][0]), bottom_right_pt=Point(instructions[0][1]),
                         line_color=instructions[1], fill_color=instructions[2], rotate_angle=instructions[3],
                         translation=(instructions[4][0],
                         instructions[4][1]),
                         scale_size=instructions[5], center=center)

    def createTriangle(self, center, instructions):
        """

        :param center: center of the shape
        :param instructions: instructions of the given shape
        :return: Triangle with the given instructions
        """
        return Triangle(p1=Point(instructions[0][0]), p2=Point(instructions[0][1]), p3=Point(instructions[0][2]),
                        line_color=instructions[1], fill_color=instructions[2], rotate_angle=instructions[3],
                        translation=(instructions[4][0],
                        instructions[4][1]),
                        scale_size=instructions[5], center=center)

    def createLine(self, center, instructions):
        """

        :param center: center of the shape
        :param instructions: instructions of the given shape
        :return: Line with the given instructions
        """
        return Line(p1=Point(instructions[0][0]), p2=Point(instructions[0][0]), line_color=instructions[1],
                    fill_color=instructions[2], rotate_angle=instructions[3],
                    translation=(instructions[4][0],
                    instructions[4][1]),
                    scale_size=instructions[5], center=center)


