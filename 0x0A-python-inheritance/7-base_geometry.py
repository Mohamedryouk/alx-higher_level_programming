#!/usr/bin/python3
"""
contains the class BaseGeometry
"""


class BaseGeometry:
    """A class with public instance methods area and integer validator"""
    def area(self):
        """raises an exception when called"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """validates that value if its integer > 0"""
        if type(value) is not int:
            raise TypeError("{:} must be an integer".format(name))
        if value <= 0:
            raise ValueError("{:s} must be greater than 0".format(name))
