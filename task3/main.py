class Car:
    def __init__(self):
        self._engine_temperature = 20 
    def start_engine(self):
        self._engine_temperature = 90
        print("Двигатель прогрет")
    def drive(self):
        if self._engine_temperature >= 90:
            print("Поехали!")
        else:
            print("Ошибка: Двигатель не прогрет! Сначала вызовите start_engine().")

my_car = Car()

print(f"Текущая температура двигателя: {my_car._engine_temperature}")
my_car.drive()
my_car.start_engine()
print(f"Температура после прогрева: {my_car._engine_temperature}")
my_car.drive()