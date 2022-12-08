from Creator import Creator
from utils import convertStringsToTypes
from CompositeShape import CompositeShape
from CreatorBasicShape import CreatorBasicShape
import copy

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
        return self.createShape((int(WIDTH / 2), -int(HEIGHT / 2)), self.instructions)

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
                                       translation=center, scale_size=1, center=(0,0))
                children_names = []
                for child in properties:
                    if list(child.keys())[0] in SHAPES:
                        parsed_child = self.createShape((center[0],
                                                         center[1]), child)
                        paint.add(parsed_child)
                    else:
                        for idx, parsed_child in enumerate(paint.children):
                            if list(child.keys())[0] == parsed_child.name:
                                prt = convertStringsToTypes(list(child.values())[0])
                                child = copy.deepcopy(parsed_child)
                                child.rotate_angle = prt[1]
                                child.translation = prt[2]
                                child.scale_size = prt[3]
                                paint.add(child)
                                break

                        if type(child) != dict:
                            continue
                        parsed_child = self.createShape((center[0],
                                          center[1]), child)
                        children_names.append(parsed_child.name)
                        paint.add(parsed_child)

                return paint

            elif name not in SHAPES:
                center = center[0] + properties[2][0], center[1] - properties[2][1]
                new_shape = CompositeShape([], name=name, rotate_angle=properties[1],
                                           translation=(properties[2][0], properties[2][1]),
                                           scale_size=properties[3], center=center)
                for child_new_shape in list(properties[0].values())[0]:
                    # if list(child_new_shape.keys())[0] in
                    new_shape.add(self.createShape((center[0],
                                                        center[1]), child_new_shape))

                return new_shape

            else:
                center = center[0] + properties[4][0], center[1] - properties[4][1]
                instructions[list(instructions.keys())[0]] = properties
                return self.creatorBasicShape.createShape((center[0],
                                                        center[1]), instructions)
