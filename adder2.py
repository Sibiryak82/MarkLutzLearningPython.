# Файл adder2.py

class Adder:
    def __init__(self, start=[]):
        self.data = start
    def __add__(self, other):       # Передавать одиночный аргумент
        return self.add(other)      # То, что слева от операции - это self
    def add(self, y):
        print('not implemented!')

class ListAdder(Adder):
    def add(self, y):
        return self.data + y

class DictAdder(Adder):
    def add(self, y):
        d = self.data.copy()        # Изменить для использования self.data вместо x
        d.update(y)                 # Или "смошенничать" путём использования
        return d                    # более быстрой встроенной функции

x = ListAdder([1, 2, 3])
y = x + [4, 5, 6]
print(y)

z = DictAdder(dict(name='Bob')) + {'a':1}
print(z)
