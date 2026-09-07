class Graph:
    def __init__(self, data):
        # Создаем копию списка, чтобы у каждого объекта был свой
        self.data = list(data)
        self.is_show = True

    def set_data(self, data):
        self.data = list(data)

    def show_table(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print(" ".join(map(str, self.data)))

    def show_graph(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print("Графическое отображение данных: " + " ".join(map(str, self.data)))

    def show_bar(self):
        if not self.is_show:
            print("Отображение данных закрыто")
        else:
            print("Столбчатая диаграмма: " + " ".join(map(str, self.data)))

    def set_show(self, fl_show):
        self.is_show = fl_show

# --- Код из условия (не менять) ---
# считывание списка из входного потока (эту строку не менять)
data_graph = list(map(int, input().split()))

# здесь создаются объекты классов и вызываются нужные методы
gr = Graph(data_graph)
gr.show_bar()
gr.set_show(False)
gr.show_table()