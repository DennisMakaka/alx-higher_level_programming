#!/usr/bin/python3

class Square:
    """Square class definition.

    This class represents a square. it is currently empty and can be extended to include attributes and methods specific to a square.

    Attributes:
        No attributes currently defined.
    """

    def __init__(self, size=0):
        """Initialization method.

        Args:
            size (int): The size of the square.
        """
        self.__size = size
        self.__validate_size()

    @property
    def size(self):
        """Getter method to retrieve size attribute."""
        return self.__size

    @size.setter
    def size(self, value):
        """Settr method to set the size attribute.

        Args:
            value (int): The new value for the size attribute."""
        self.__size = value
        self.__validate_size()

    def __validate_size(self):
        """Private method to validate the size attribute."""
        if not isinstance(self.__size, int):
            raise TypeError("size must be an integer")
        if self.__size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
            """Calculate the area of the square."""
            return self.__size ** 2
