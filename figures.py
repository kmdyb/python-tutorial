class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, sidelength):
        super().__init__(sidelength, sidelength)


class Cube(Square):
    def __init__(self, sidelength):
        super().__init__(sidelength)

    def count_surface_area(self):
        return super().count_surface_area() * 6

    def count_volume(self):
        return super().count_surface_area() * self.height


cube = Cube(2)
print(cube.height)

square = Square(2)
print(square.count_surface_area())
print(cube.count_surface_area())
print(cube.count_volume())

