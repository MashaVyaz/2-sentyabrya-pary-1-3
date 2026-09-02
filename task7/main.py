class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords
        self.width = width
        self.color = color
    def draw(self):
        print("Рисуется фигура")

class Line(Figure):
    def __init__(self, coords, width, color, length):
        super().__init__(coords, width, color)
        self.length = length
    def draw(self):
        print(f"Рисуется линия длиной {self.length}")

class Rect(Figure):
    def __init__(self, coords, width, color, height):
        super().__init__(coords, width, color)
        self.height = height
    def draw(self):
        print(f"Рисуется прямоугольник высотой {self.height}")

class Ellipse(Figure):
    def __init__(self, coords, width, color, radius):
        super().__init__(coords, width, color)
        self.radius = radius
    def draw(self):
        print(f"Рисуется эллипс с радиусом {self.radius}")

line = Line((0, 50), 5, "розовый", 50)
rect = Rect((30, 60), 10, "синий", 67)
ellipse = Ellipse((67, 80), 15, "желтый", 40)

shapes = [line, rect, ellipse]

for shape in shapes:
    shape.draw()