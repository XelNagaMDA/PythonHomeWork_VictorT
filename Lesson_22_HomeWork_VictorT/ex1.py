"""
Create the classes listed below. Use Inheritance.

For all the properties, use underscores inside the class to hide the properties (example self._inner_color),
 and declare get and set methods (example set_inner_color).

Create a Class that describes a Shape

The shape class should have the following properties:

    inner color
    border color

Create another class Circle which extends Shape.

The circle class should have the following additional properties.

    radius

Create another class Rectangle which also extends Shape

The rectangle class should have the following additional properties.

    width
    length

Create another class Square that extends Rectangle

The Square class should make sure that the width and length are equal when one of them is set.
For example if I set square.set_length(4), square.get_width() should also be 4.
"""


class Shape:
    def __init__(self):
        self._inner_color = ""
        self._border_color = ""

    def get_inner_color(self):
        return f"{self._inner_color} is the inner color"

    def set_inner_color(self, color):
        self._inner_color = color

    def get_border_color(self):
        return f"{self._border_color} is the border color"

    def set_border_color(self, color):
        self._border_color = color


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self._radius = 0

    def set_radius(self, radius):
        self._radius = radius

    def get_radius(self):
        return f"{self._radius} is the radius of the circle"


class Rectangle(Shape):
    def __init__(self):
        super().__init__()
        self._width = 0
        self._length = 0

    def get_width(self):
        return f"The rectangle width is {self._width}"

    def set_width(self, width):
        self._width = width
        self._length = width

    def set_length(self, length):
        self._length = length
        self._width = length

    def get_length(self):
        return f"The rectangle width is {self._length}"


class Square(Rectangle):
    def __init__(self):
        super().__init__()

    def set_length(self, length):
        super().set_length(length)
        super().set_width(length)

    def set_width(self, width):
        super().set_width(width)
        super().set_length(width)


circle = Circle()
circle.set_inner_color("blue")
print(circle.get_inner_color())

circle.set_radius(666)
print(circle.get_radius())

rectangle = Rectangle()
rectangle.set_inner_color("black")
rectangle.set_border_color("white")
rectangle.set_length(33)
rectangle.set_width(11)
print(rectangle.get_inner_color(), rectangle.get_border_color(), rectangle.get_length(), rectangle.get_width())

square = Square()
square.set_length(111)
print(square.get_width())

square.set_inner_color("yellow")
print(square.get_inner_color())
