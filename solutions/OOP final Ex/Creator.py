import json
from CompositeShape import CompositeShape
from utils import convertStringsToTypes

HEIGHT, WIDTH = 1100,1200
class Creator:
    def createCompositeShape(self, instructions):
        '''

        :param instructions: json file to open the instructions
        :return: CompositeShape of the image
        '''
        f = open(instructions)
        data = json.load(f)
        for shape in list(data.keys()):
            properties = data[shape]
            properties = convertStringsToTypes(properties)
            paint = CompositeShape([], name=shape, rotate_angle=properties[1],
                                   translation=(int(HEIGHT/2 + properties[2][0]), int(WIDTH/2 - properties[2][1])),
                                   scale_size=properties[3])
            if type(properties[0]) == list:
                for child in properties[0]:
                    paint.add(child)

        return paint