import sys

class DataBase:
    lst_data = []
    FIELDS = ('id', 'name', 'old', 'salary')
    def insert(self, data):
        for line in data:
            parts = line.split()
            record = {
                'id': parts[0],
                'name': parts[1],
                'old': parts[2],
                'salary': parts[3]
            }
            self.lst_data.append(record)

    def select(self, a, b):
        return self.lst_data[a:b+1]

db = DataBase()
test_data = [
    "1 Сергей 35 120000",
    "2 Федор 23 12000",
    "3 Иван 13 1200"
]

db.insert(test_data)
print("Выборка с 0 по 1 индекс:", db.select(0, 1))