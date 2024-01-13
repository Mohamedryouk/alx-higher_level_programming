#!/usr/bin/pyhon3
"""
Class to calculate the recangle then getting
the area at the end
"""
class Rectangle:
    """
    Defines class rectangle with private attribute width and height
    Args:
        width (int): width
        height (int): height
    Functions:
        __init__(self, width, height)
        width(self)
        width(self, value)
        height(self)
        height(self, value)
    """

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
    @property
    def width(self):
        """Getter returns width"""
        return self.__width

    @width.setter
    def width(self, value):
        """Setter for width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value
    @property
    def height(self):
        """Getter for height"""
        return self.__height
    @height.setter
    def height(self, value):
        """Setter for height"""
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Calculates and returns the area"""
        return self.width * self.height

    def perimeter(self):
        """Calculates and return the perimeter"""
        return 2 * (self.width + self.height)