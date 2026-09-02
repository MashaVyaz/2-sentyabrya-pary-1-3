class Figure:
    def __init__(self, coords, width, color):
        self.coords = coords  
        self.width = width    
        self.color = color   
    def display_info(self):
        print(f"Фигура: координаты {self.coords}, ширина {self.width}, цвет {self.color}")

figure1 = Figure((5, 7), 5, "розовый")
figure2 = Figure((30, 60), 10, "синий")
figure3 = Figure((67, 67), 15, "желтый")

figure1.display_info()
figure2.display_info()
figure3.display_info()