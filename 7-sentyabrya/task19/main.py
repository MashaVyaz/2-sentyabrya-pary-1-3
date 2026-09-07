class CPU:
    def __init__(self, name, fr):
        self.name = name
        self.fr = fr

class Memory:
    def __init__(self, name, volume):
        self.name = name
        self.volume = volume

class MotherBoard:
    def __init__(self, name, cpu, *memories):
        self.name = name
        self.cpu = cpu
        self.total_mem_slots = 4
        # Сохраняем максимум 4 модуля памяти
        self.mem_slots = list(memories)[:self.total_mem_slots]

    def get_config(self):
        # Собираем информацию о памяти в одну строку
        mem_info = []
        for mem in self.mem_slots:
            mem_info.append(f"{mem.name} - {mem.volume}")
        
        mem_str = "; ".join(mem_info)
        
        # Возвращаем список из 4 строк, как в задании
        return [
            f"Материнская плата: {self.name}",
            f"Центральный процессор: {self.cpu.name}, {self.cpu.fr}",
            f"Слотов памяти: {self.total_mem_slots}",
            f"Память: {mem_str}"
        ]

# --- Создаем объекты по заданию ---
cpu = CPU("Intel Core i5", "3.2 GHz")
mem1 = Memory("Kingston", "8 GB")
mem2 = Memory("Corsair", "16 GB")

mb = MotherBoard("ASUS Prime", cpu, mem1, mem2)

# Проверка: выводим конфигурацию
for line in mb.get_config():
    print(line)