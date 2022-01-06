class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def count_surface_area(self):
        return self.width * self.height


class Square(Rectangle):
    def __init__(self, sidelength):
        super().__init__(sidelength, sidelength)


class Cube:
    def __init__(self, a_square: Square):
        self.square = a_square
        self.height = square.height

    def count_surface_area(self):
        return self.square.count_surface_area() * 6

    def count_volume(self):
        return self.square.count_surface_area() * self.height


class Cuboid:
    def __init__(self, figure, height):
        self.base = figure                  # przyporządkowanie
        self.height = height

    def count_volume(self):
        return self.base.count_surface_area() * self.height

    def count_surface_area(self):
        return self.base.count_surface_area() * 2 + self.height * self.base.width + 2 * self.base.height * self.height


# przyporządkowanie to są:
# agregacja (łączy w całość, gromadzeni) tworzy obiekt składowy
# kompozycja (obiekt nie może istnieć bez klasy, do której jest przyporządkowywany)

square = Square(2)
cube = Cube(square)
print(square.count_surface_area())
print(cube.count_surface_area())
print(cube.count_volume())

cuboid = Cuboid(Rectangle(2, 3), 4)
print(cuboid.count_volume())
