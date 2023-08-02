"""
Create a Shape service.

The methods inside shape service should all be staticmethods.

The Shape service should have the following properties as class properties:

DEFAULT_INNER_COLOR, DEFAULT_OUTER_COLOR - You can choose any string default values

The Shape service should have the following methods:

    create_default_circle(radius) - creates and returns a Circle object,
     with properties for colors form the defaults.
    create_default_rectangle(width, length) - creates and returns a Rectangle object,
     with properties for colors form the defaults.
    create_default_square(side_length) - creates and returns a Square object,
    with properties for colors from defaults.
    color_shapes(list_of_shapes, inner_color, border_color) - set's the colors of all the shapes in
    the list to the colors from the arguments.
"""
from Lesson_22_HomeWork_VictorT.ex1 import Circle, Rectangle, Square


class ShapeService:
    DEFAULT_INNER_COLOR = "yellow"
    DEFAULT_OUTER_COLOR = "blue"

    @staticmethod
    def create_default_circle(radius):
        circle = Circle()
        circle.set_inner_color(ShapeService.DEFAULT_INNER_COLOR)
        circle.set_border_color(ShapeService.DEFAULT_OUTER_COLOR)
        circle.set_radius(radius)
        return circle

    @staticmethod
    def create_default_rectangle(length, width):
        rectangle = Rectangle()
        rectangle.set_inner_color(ShapeService.DEFAULT_INNER_COLOR)
        rectangle.set_border_color(ShapeService.DEFAULT_OUTER_COLOR)
        rectangle.set_length(length)
        rectangle.set_width(width)
        return rectangle

    @staticmethod
    def create_default_square(side_length):
        square = Square()
        square.set_inner_color(ShapeService.DEFAULT_INNER_COLOR)
        square.set_border_color(ShapeService.DEFAULT_OUTER_COLOR)
        square.set_length(side_length)
        return square

    @staticmethod
    def color_shapes(list_of_shapes, inner_color, border_color):
        for shape in list_of_shapes:
            shape.set_inner_color(inner_color)
            shape.set_border_color(border_color)


circle1 = ShapeService.create_default_circle(10)

rectangle1 = ShapeService.create_default_rectangle(20, 15)

square1 = ShapeService.create_default_square(30)

shapes = [circle1, rectangle1, square1]

ShapeService.color_shapes(shapes, "green", "white")


