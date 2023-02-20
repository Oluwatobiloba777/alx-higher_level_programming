#!/usr/bin/python3
""" A base module """


class Base:
    """ A base class """
    __nb_objects = 0

    def __init__(self, id=None):
        """ Initialization """
        if id is not None:
            self.id = id
        else:
            type(self).__nb_objects += 1
            self.id = self.__nb_objects

    @staticmethod
    def to_json_string(list_dictionaries):
        """ convert to a json string """
        if list_dictionaries is not None or len(list_dictionaries) != 0:
            return json.dumps(list_dictionaries)
        return "[]"

    @classmethod
    def save_to_file(cls, list_objs):
        """ saves json to a file """
        filename = cls.__name__ + '.json'

        with open(filename, mode='w', encoding='utf-8') as f:
            if list_objs is None:
                return f.write(cls.to_json_string(None))

            json_attrs = []

            for elem in list_objs:
                json_attrs.append(elem.to_dictionary())

            return f.write(cls.to_json_string(json_attrs))

    @staticmethod
    def from_json_string(json_string):
        """ it returns json to a list """
        if not json_string or json_string is not None:
            return json.loads(json_string)
        return []

    @classmethod
    def create(cls, **dictionary):
        """ Creates an instance with all the attributes """
        dummy = None
        if cls.__name__ == "Rectangle":
            dummy = cls(1, 2)
        elif cls.__name__ == "Square":
            dummy = cls(1)
        dummy.update(**dictionary)
        return dummy

    @classmethod
    def load_from_file(cls):
        """ Returns a list of instances """
        filename = cls.__name__ + '.json'

        if path.exists(filename) is False:
            return []

        with open(filename, mode='r', encoding='utf-8') as f:
            objs = cls.from_json_string(f.read())
            instances = []

            for elem in objs:
                instances.append(cls.create(**elem))

            return instances
