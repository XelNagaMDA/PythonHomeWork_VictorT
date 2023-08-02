"""
Using your classes Shape, Circle, Rectangle and Square.

Implement the necessary methods to:

    Get the area of the shape (Circle, Rectangle, Square), as a property. Except for Shape
    (shape can't have an area)
    Be able to compare shapes (only shapes of the same type can be compared)
        Only shapes of the same type can be compared:
            I should be able to compare a Circle with another circle
            I should not be able to compare a Circle with a Square
        I should be able to compare a Square and a Rectangle, because they have the same properties.
        When comparing Rectangles, compare the area of the rectangle (not the width and length)
    Be able to perform addition, subtraction and multiplication of shapes (for example rectangle1 + rectangle2)
        When performing such operations, perform the operations on the common properties of the 2 objects
         ( width/length/radius)
        When performing subtraction, the value of properties of a shape should not be less than 0.
        Only shapes with the same properties can have the operations performed (ex: Circle and Square can not
         be added, Square and Rectangles can). You can use the isinstance and issubclass checks to perform
         the checks.
        When performing multiplication, also allow to multiply the object with a number.
            Example: Rectangle(2,4) * 2 = Rectangle(4,8)

"""
import math


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

    @property
    def area(self):
        return None

    def __eq__(self, other):
        if isinstance(self, type(other)):
            return self.area == other.area
        raise ValueError(" These are different shapes to compare")

    def __lt__(self, other):
        if isinstance(self, type(other)):
            return self.area < other.area
        raise ValueError(" These are different shapes to compare")

    def __gt__(self, other):
        if isinstance(self, type(other)):
            return self.area > other.area
        raise ValueError(" These are different shapes to compare")

    def __le__(self, other):
        if isinstance(self, type(other)):
            return self.area <= other.area
        raise ValueError(" These are different shapes to compare")

    def __ge__(self, other):
        if isinstance(self, type(other)):
            return self.area >= other.area

    def __add__(self, other):
        if isinstance(self, type(other)):
            pass


class Circle(Shape):
    def __init__(self):
        super().__init__()
        self._radius = 0

    def set_radius(self, radius):
        self._radius = radius

    def get_radius(self):
        return f"{self._radius} is the radius of the circle"

    @property
    def area(self):
        return math.pi * self._radius ** 2


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

    @property
    def area(self):
        return self._width * self._length


class Square(Rectangle):
    def __init__(self):
        super().__init__()

    def set_length(self, length):
        super().set_length(length)
        super().set_width(length)

    def set_width(self, width):
        super().set_width(width)
        super().set_length(width)


my_circle = Circle()
my_circle.set_radius(20)
print(my_circle.area)

my_circle2 = Circle()
my_circle2.set_radius(21)

print(my_circle > my_circle2)


