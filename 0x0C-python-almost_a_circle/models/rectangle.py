#!/usr/bin/python3
"""Rectangle base class"""
import Base


class Rectangle(Base):
    """Rectangle base class"""

    def __init__(self, width, height, x=0, y=0, id=None):
        """Initialize an instance of Rectangle class

        Args:
            width(int): Width of the rectangle
            height(int): Height of the rectangle
            x(int): [Optional] X coordinate
            y(int): [Optional] Y coordinate
            
            id(int): instance id
        """
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    # ======= GETTERS AND SETTERS ======================
    @property
    def width(self):
        """get the value of width"""
        return self.__width

    @width.setter
    def width(self, value):
        """value(int): set the value of width"""
        self.__width =  value

    @property
    def height(self):
        """get the value of height"""
        return self.__height

    @height.setter
    def height(self, value):
        """value(int): set the value of height"""
        self.__height =  value

    @property
    def x(self):
        """get the value of x"""
        return self.__x

    @height.setter
    def x(self, value):
        """value(int): set the value of x"""
        self.__x =  value

    @property
    def y(self):
        """get the value of y"""
        return self.__y

    @height.setter
    def y(self, value):
        """value(int): set the value of y"""
        self.__y =  value
