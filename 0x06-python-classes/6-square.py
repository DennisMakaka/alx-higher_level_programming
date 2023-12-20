#!/usr/bin/python3

class Square:
    """Square class definition.

    This class represents a square. It includes private instance attributes 'size'
    and 'position' for controlling the type and value of the square's size and position.

    Attributes:
        size (int): The size of the square.
        position (tuple): The position of the square.
    """
    def __init__(self, size=0, position=(0, 0)):
         """Initialization method.

        Args:
            size (int): The size of the square. Defaults to 0.
            position (tuple): The position of the square. Defaults to (0, 0).
        """
        self.size = size
        self.position = position
    
    @property
    def size(self):
        """Getter method to retrieve the size attribute."""
        return self._size

    @size.setter
    def size(self, value):
        """Setter method to set the size attribute.

        Args:
            value (int): The new value for the size attribute.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self._size = value

    @property
    def position(self, value):
        """Setter method to set the position attribute.

        Args:
            value (tuple): The new value for the position attribute.
        """
        if not isinstance(value, tuple) or len(value) != 2 or not all(isinstance(i, int) for i in value) or any(i < 0 for i in value):
            raise TypeError("position must be a tuple of 2 positive integers")
        self._position = value

     def area(self):
        """Calculate the area of the square."""
        return self._size ** 2

    def my_print(self):
        """Print the square with the character # and position."""
        if self._size == 0:
            print()
        else:
            for _ in range(self._position[1]):
                print()
            for _ in range(self._size):
                print(" " * self._position[0] + "#" * self._size)



