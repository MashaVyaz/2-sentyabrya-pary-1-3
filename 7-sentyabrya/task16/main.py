import random
class Line:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Rect:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

class Ellipse:
    def __init__(self, a, b, c, d):
        self.sp = (a, b)
        self.ep = (c, d)

elements = []
classes = [Line, Rect, Ellipse]

for _ in range(217):
    random_class = random.choice(classes)
    a, b, c, d = random.randint(0, 100), random.randint(0, 100), random.randint(0, 100), random.randint(0, 100)
    elements.append(random_class(a, b, c, d))
for obj in elements:
    if isinstance(obj, Line):
        obj.sp = (0, 0)
        obj.ep = (0, 0)

for i in range(3):
    print(f"Объект {i}: тип={type(elements[i]).__name__}, sp={elements[i].sp}, ep={elements[i].ep}")