#!/usr/bin/python3
"""Rectangle class that defines a rectangle by
`width` and `height`
"""


class Rectangle(object):
    """Rectangle class that defines a rectangle by
        `width` and `height`
    """
    # int: class attribute to count number of instance
    #   will be incremented in __init__
    #   and decremented in __del__
    number_of_instances = 0

    # str: class symbol
    print_symbol = "#"

    def __init__(self, width=0, height=0):
        """Initialize Rectangle instance
        Args:
            width(int, optional): width of the rectangle
            height(int, optional): height of the rectangle

        Raises:
            TypeError: This is of different cases
                case1: `width` is not an integer
                    exception message could be `width must be an integer`
                case1b: `height` is not an integer
                    exception message could be `height must be an integer`
            ValueError: This is of different cases
                case1a: `width` is less than 0 (i.e < 0)
                    exception message could be `width must be >= 0`
                case1b: `height` is less than 0 (i.e < 0)
                    exception message could be `height must be >= 0`
        """

        self.width = width
        self.height = height
        # increment number of instances
        type(self).number_of_instances += 1

    @property
    def width(self):
        """int: width of rectangle"""
        return self.__width

    @width.setter
    def width(self, value):
        """Set width of rectangle

        Args:
            value(int): width of the rectangle

        Raises:
            TypeError: `width` is not an integer
                exception message could be `width must be an integer`

            ValueError: `width` is less than 0 (i.e < 0)
                exception message could be `width must be >= 0`
        """
        # ===== Check TypeError =====
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        # ===== Check ValueError =====
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        """int: height of rectangle"""
        return self.__height

    @height.setter
    def height(self, value):
        """Set height of rectangle

        Args:
            value(int): height of the rectangle

        Raises:
            TypeError: `height` is not an integer
                exception message could be `height must be an integer`

            ValueError: `height` is less than 0 (i.e < 0)
                exception message could be `height must be >= 0`
        """
        # ===== Check TypeError =====
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        # ===== Check ValueError =====
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value

    # ======= Instance Methods =========
    def area(self):
        """Get the calculated area of the rectangle instance
            based on the `width` and `height`

        Note: if width or height is equal to 0, perimeter is equal to 0

        Returns:
            int: calculated area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """Get the calculated perimeter of the rectangle instance
            based on the `width` and `height`

        Returns:
            int: calculated perimeter of the rectangle
        """

        if self.width == 0 or self.height == 0:
            return 0

        return (self.width * 2) + (self.height * 2)

    def __str__(self):
        f"""Printable version of the instance with `{self.print_symbol}`

        Returns: diagram of rectangle using `{self.print_symbol}`
        """

        if self.width == 0 or self.height == 0:
            return ""
        # hash lines of rectangle
        _symbol = str(self.print_symbol)
        lines = [_symbol * self.width for _ in range(self.height)]
        return "\n".join(lines)

    def __repr__(self):
        """Representation of the rectangle instance

        Returns: a string to recreate a new instance by using eval()
        """
        return f"Rectangle({self.width}, {self.height})"

    def __del__(self):
        """Called when instance is deleted"""
        print("Bye rectangle...")
        # decrement number of instances
        type(self).number_of_instances -= 1
