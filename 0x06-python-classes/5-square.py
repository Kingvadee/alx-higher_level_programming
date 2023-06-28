#!/usr/bin/python3
class Square:
    """Type class square"""
    def __init__(self, size):
        """Init the square class
        Args:
        Param1: size is the type int attribute to make it private
        """
        self.size = size

    @property
    def size(self):
        """Private attribute to get the size of a square"""
        return (self.__size)

    @size.setter
    def size(self, value):
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Return the area of the square"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print in stdout a square with #"""
        if self.__size == 0:
            print("")
        for i in range(0, self.__size):
            [print("#", end="") for j in range(self.__size)]
            print("")
