import json
HEIGHT, WIDTH = 800, 800


class Creator:
    def createParsedShape(self, instructions):
        """

        :param instructions: instructions of the shape
        :return: The parsed shaped
        """
        pass

    def createShape(self, center, instructions):
        '''
        :return: creates shape
        '''
        pass

    def _parseJson(self, instructions):
        """

        :param instructions: instructions of the shape
        :return: None, loads the json file to dict type
        """
        f = open(instructions)
        self.instructions = json.load(f)


