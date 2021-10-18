#!/usr/bin/python3


from models.rectangle import Rectangle


class Square(Rectangle):
    """
    contains def __init__(self, size, x=0, y=0, id=None
    """
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size, size, x, y, id)
        self.size = seze

    @property
    def size(self):
        """size getter"""
        return self.width

    @size.setter
    def size(self, value):
        """sets wisth and height as size"""
        self.width = value
        self.height = value
