import math
class Figure:
    def __init__(self, x, y):
        self._x = x
        self._y = y
    def get_coords(self):
        return (self._x, self._y)
    def set_coords(self, x, y):
        self._x = x
        self._y = y
    def display_info(self):
        print(f"Фигура на позиции {self.get_coords()}")

class Circle(Figure):
    def __init__(self, x, y, radius):
        super().__init__(x, y)
        self._radius = radius  
    def get_radius(self):
        return self._radius
    def calculate_area(self):
        return math.pi * (self._radius ** 2)
    def display_info(self):
        print(f"Круг: позиция {self.get_coords()}, радиус {self._radius}, площадь {self.calculate_area():.2f}")

class Square(Figure):
    def __init__(self, x, y, side):
        super().__init__(x, y)
        self._side = side  
    def get_side(self):
        return self._side
    def calculate_area(self):
        return self._side ** 2
    def display_info(self):
        print(f"Квадрат: позиция {self.get_coords()}, сторона {self._side}, площадь {self.calculate_area()}")

shapes = [
    Circle(10, 20, 5),
    Square(30, 40, 6),
    Circle(50, 60, 7),
    Square(70, 80, 8),
    Circle(90, 100, 9)
]
print("Фигуры")
for shape in shapes:
    shape.display_info()

total_area = 0
for shape in shapes:
    total_area += shape.calculate_area()

print(f"Общая площадь всех фигур: {total_area:.2f}")