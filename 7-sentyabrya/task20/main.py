class Table:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class TV:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Notebook:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Cup:
    def __init__(self, name, price):
        self.name = name
        self.price = price
class Cart:
    def __init__(self):
        self.goods = [] 
    def add(self, gd):
        self.goods.append(gd)
    def remove(self, indx):
        del self.goods[indx]
    def get_list(self):
        result = []
        for item in self.goods:
            result.append(f"{item.name}: {item.price}")
        return result
cart = Cart()
cart.add(TV("Samsung TV", 50000))
cart.add(TV("LG TV", 45000))
cart.add(Table("Office Table", 15000))
cart.add(Notebook("MacBook", 150000))
cart.add(Notebook("Lenovo", 80000))
cart.add(Cup("Coffee Cup", 500))

for item in cart.get_list():
    print(item)