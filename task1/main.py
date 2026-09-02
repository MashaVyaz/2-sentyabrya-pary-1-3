class Cat:
    def __init__(self, breed, name, age):
        self.breed = breed
        self.name = name
        self.age = age

cat1 = Cat("Сиамская", "Шотя", 3)
cat2 = Cat("Ориентальная", "Китнес", 13)
cat3 = Cat("Сфинкс", "Пряник", 4)
print(f"Кот 1: Имя - {cat1.name}, Порода - {cat1.breed}, Возраст - {cat1.age} года")
print(f"Кот 2: Имя - {cat2.name}, Порода - {cat2.breed}, Возраст - {cat2.age} лет")
print(f"Кот 3: Имя - {cat3.name}, Порода - {cat3.breed}, Возраст - {cat3.age} года")