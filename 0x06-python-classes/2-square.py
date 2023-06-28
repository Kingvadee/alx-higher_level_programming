#!/usr/bin/python3
class Square:
    """Type class square"""
    def __init__(self, size=0):
        """Init the square classs
        Args:
        param1: size is the type int attribute to make it private
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        self.__size = size
