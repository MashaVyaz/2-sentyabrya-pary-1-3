# Базовый класс Figure (из задачи 5)
class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color
    def display_info(self):
        print(f"Фигура: координаты {self.coords}, ширина {self.width}, цвет {self.color}")

class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length
    def display_info(self):
        super().display_info()
        print(f"  Длина линии: {self.length}")

class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height
    def display_info(self):
        super().display_info()
        print(f"  Высота прямоугольника: {self.height}")

class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius
    def display_info(self):
        super().display_info()
        print(f"  Радиус эллипса: {self.radius}")

line = Line((0, 50), 5, "розовый", 50)
rect = Rect((30, 60), 10, "синий", 50)
ellipse = Ellipse((67, 80), 15, "желтый", 50)

print("Линия")
line.display_info()

print("Прямоугольник")
rect.display_info()

print("Эллипс")
ellipse.display_info()