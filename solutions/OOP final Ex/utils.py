import json


def convertStringsToTypes(properties):
    """

    :param properties: properties of a given shape
    :return: None, converts all the string types from the instructions to their object types, e.g. (10,10) to a tuple.
    """
    new_properties = []
    for property in properties:
        if type(property) == str:
            if ',' in property:
                property = property.replace('(', '')
                property = property.replace(')', '')
                new_pt = tuple(map(int, property.split(',')))
                new_properties.append(new_pt)
            elif property == 'False' or property == 'True':
                new_properties.append(property == 'True')
            else:
                new_properties.append(float(property))
        elif type(property) != dict:
            if 'json' in property[0]:
                new_properties.append(json.load(open(property[0])))
            else:
                points = []
                for point in property:
                    point = point.replace('(', '')
                    point = point.replace(')', '')
                    new_pt = tuple(map(int, point.split(',')))
                    points.append(new_pt)
                new_properties.append(points)
        else:
            new_properties.append(property)
    return new_properties
