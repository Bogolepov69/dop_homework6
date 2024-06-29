class Figure:
    sides_count = 0

    def __init__(self, color, *args):
        self.__sides = [1] * self.sides_count if len(args) != self.sides_count else list(args)
        self.__color = color

    def __is_valid_color(self, r, g, b):
        return all(0 <= x <= 255 for x in (r, g, b))

    def set_color(self, r, g, b):
        if self.__is_valid_color:
            self.__color = (r, g, b)

    def get_color(self):
        return self.__color

    def __is_valid_sides(self, *args):
        return all(x > 0 for x in args) and len(args) == self.sides_count

    def set_sides(self, *args):
        if self.__is_valid_sides(*args):
            self.__sides = list(args)

    def get_sides(self):
        return self.__sides

    def __len__(self):
        return sum(self.__sides)


class Circle(Figure):
    sides_count = 1

    def __init__(self, color, radius):
        super().__init__(color, radius)

    def get_square(self):
        return 3.14159265359 * self.__sides[0] ** 2


class Triangle(Figure):
    sides_count = 3

    def __init__(self, color, *args):
        super().__init__(color, *args)

    def get_square(self):
        a, b, c = self.__sides
        p = (a + b + c) / 2
        return (p * (p - a) * (p - b) * (p - c)) ** 0.5


class Cube(Figure):
    sides_count = 12

    def __init__(self, color, side):
        super().__init__(color, *[side] * self.sides_count)

    def get_volume(self):
        return self.__sides[0]


circle1 = Circle((200, 200, 100), 10)
cube1 = Cube((222, 35, 130), 6)

# Проверка на изменение цветов:
circle1.set_color(55, 66, 77)
cube1.set_color(300, 70, 15)
print(circle1.get_color())
print(cube1.get_color())

# Проверка на изменение сторон:
cube1.set_sides(5, 3, 12, 4, 5)
circle1.set_sides(15)
print(cube1.get_sides())
print(circle1.get_sides())

# Проверка периметра (круга), это и есть длина:
print(len(circle1))

# Проверка объёма (куба):
print(cube1.get_volume)
