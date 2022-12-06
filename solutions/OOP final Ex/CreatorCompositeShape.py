from Creator import Creator
from utils import convertStringsToTypes
from CompositeShape import CompositeShape
from CreatorBasicShape import CreatorBasicShape

HEIGHT, WIDTH = 1100, 1100
SHAPES = ['Triangle', 'Point', 'Circle', 'Rectangle', 'Line']


class CreateCompositeShape(Creator):
    def __init__(self):
        """
        factory of the shapes
        """
        super().__init__()
        self.creatorBasicShape = CreatorBasicShape()

    def createParsedShape(self, instructions):
        self._parseJson(instructions)
        return self.createShape((int(WIDTH / 2), int(HEIGHT / 2)), self.instructions)

    def createShape(self, center, instructions):
        """

        :return: creates all the collection of the composite shapes
        """
        for shape in list(instructions.keys()):
            name = shape
            properties = instructions[shape]
            properties = convertStringsToTypes(properties)


            if type(properties[1]) != float and type(properties[1]) != tuple:
                paint = CompositeShape([], name=shape, rotate_angle=0,
                                       translation=(center[0], center[1]), scale_size=1)
                for child in properties:
                    paint.add(self.createShape((center[0],
                                                center[1]), child))

                return paint

            elif name not in SHAPES:
                center = center[0] + properties[2][0], center[1] - properties[2][1]
                new_shape = CompositeShape([], name=name, rotate_angle=properties[1],
                                           translation=(center[0],
                                                        center[1]),
                                           scale_size=properties[3])
                for child_new_shape in list(properties[0].values())[0]:
                    new_shape.add(self.createShape((center[0],
                                                        center[1]), child_new_shape))

                return new_shape

            else:
                center = center[0] + properties[4][0], center[1] - properties[4][1]
                instructions[list(instructions.keys())[0]] = properties
                return self.creatorBasicShape.createShape((center[0],
                                                        center[1]), instructions)
