class Graph:
    def __init__(self, x=0, y=0, scale=1):
        self._x = x
        self._y = y
        self._scale = scale
    def move(self, dx, dy):
        self._x += dx
        self._y += dy
        print(f"График перемещен на ({dx}, {dy})")
    def change_scale(self, factor):
        self._scale *= factor
        print(f"Масштаб изменен в {factor} раз")
    def display(self):
        print(f"График: позиция ({self._x}, {self._y}), масштаб {self._scale}")

graph1 = Graph(15, 10, 3)
graph2 = Graph(5, 15, 30)
graph3 = Graph(1, 1, 2)

print("--- До изменений ---")
graph1.display()
graph2.display()
graph3.display()
print("\n--- Применяем изменения ---")
graph1.move(5, -3)
graph2.change_scale(1.5)
print("\n--- После изменений ---")
graph1.display()
graph2.display()
graph3.display()