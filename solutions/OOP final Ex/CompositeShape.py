from Shape import Shape
from Triangle import Triangle
from Point import Point
from Circle import Circle
from Rectangle import Rectangle
from Line import Line
from utils import convertStringsToTypes

SHAPES = ['triangle', 'point', 'circle', 'rectangle', 'line']


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

    def add(self, shape):
        """

        :param shape: given sub-shape of the composite shape
        :return: None, adds the sub-shape to the composite shape children's
        """
        name = list(shape.keys())[0]
        shape[name] = convertStringsToTypes(list(shape.values())[0])
        if name not in SHAPES:
            new_shape = CompositeShape([], name=name, rotate_angle=list(shape.values())[0][1],
                                       translation=(self.center[0] + list(shape.values())[0][2][0],
                                                    self.center[1] + list(shape.values())[0][2][1]),
                                       scale_size=list(shape.values())[0][3])
            for child_new_shape in list(shape.values())[0][0]:
                new_shape.add(child_new_shape)
            self.children.append(new_shape)
        else:
            child_properties = list(shape.values())[0]
            if name == 'triangle':
                self.children.append(Triangle(p1=Point(child_properties[0][0]),
                                              p2=Point(child_properties[0][1]),
                                              p3=Point(child_properties[0][2]),
                                              line_color=child_properties[1], fill_color=child_properties[2],
                                              rotate_angle=child_properties[3],
                                              translation=(self.center[0] + child_properties[4][0],
                                              self.center[1] - child_properties[4][1]), scale_size=child_properties[5]))
            elif name == 'circle':
                self.children.append(Circle(radius=child_properties[1], line_color=child_properties[2],
                                            fill_color=child_properties[3], rotate_angle=child_properties[4],
                                            translation=(self.center[0] + child_properties[5][0],
                                            self.center[1] - child_properties[5][1]), scale_size=child_properties[6]))
            elif name == 'rectangle':
                self.children.append(Rectangle(top_left_pt=Point(child_properties[0][0]),
                                               bottom_right_pt=Point(child_properties[0][1]),
                                               line_color=child_properties[1], fill_color=child_properties[2],
                                               rotate_angle=child_properties[3],
                                               translation=(self.center[0] + child_properties[4][0],
                                               self.center[1] - child_properties[4][1]),
                                               scale_size=child_properties[5]))
            elif name == 'line':
                self.children.append(Line(p1=Point(child_properties[0][0]),
                                          p2=Point(child_properties[0][0]),
                                          line_color=child_properties[1], fill_color=child_properties[2],
                                          rotate_angle=child_properties[3],
                                          translation=(self.center[0] + child_properties[4][0],
                                          self.center[1] - child_properties[4][1]),
                                          scale_size=child_properties[5]))
            else:
                self.children.append(Point(line_color=child_properties[1], fill_color=child_properties[2],
                                           rotate_angle=child_properties[3],
                                           translation=(self.center[0] + child_properties[4][0],
                                           self.center[1] - child_properties[4][1]),
                                           scale_size=child_properties[5]))

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
