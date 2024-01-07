#!/usr/bin/python3
class Rectangle:
  """
  Define class rectangle with private attributes width and height
  args:
      width (int): width
      height (int): height
  functions:
      __init__(self, width, height)
      width(self)
      width(self, value)
      height(self)
      height(self, value)
  """
  def __init__(self, width=0, height=0):
        """Initialize rectangles"""
        self.width = width
        self.height = height

  @property
  def width(self):
        """Getter returns"""
        return self.__width

  @width.setter
  def width(self, value):
        """Setter sets width"""
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

  @property
  def height(self):
        """Getter returns height"""
        return self.__height
  @height.setter
  def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value
