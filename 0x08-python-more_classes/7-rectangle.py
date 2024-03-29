#!/usr/bin/python3
"""
Module 3-rectangle
contains rectangle with attributes width and height
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
        area(self)
        perimeter(self)
    """
    number_of_instances = 0
    print_symbol = '#'

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        """Getter for width"""
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
        """Calculate and return the area of the rectangle"""
        return self.width * self.height

    def perimeter(self):
        """Calculate and return the perimeter of the rectangle"""
        if self.width > 0 and self.height > 0:
            return 2 * (self.width + self.height)
        else:
            return 0

    def __str__(self):
        """Return a string representation of the rectangle"""
        if self.width == 0 or self.height == 0:
            return ""
        rectangle_str = ""
        for _ in range(self.height):
            rectangle_str += str(self.print_symbol) * self.width + '\n'
        return rectangle_str.rstrip('\n')

    def __repr__(self):
        """Return a string representation for recreation using eval()"""
        return f"Rectangle({self.width},{self.height})"

    def __del__(self):
        """Print a message when an instance is eleted"""
        print("Bye rectangle...")
        Rectangle.number_of_instances -= 1
