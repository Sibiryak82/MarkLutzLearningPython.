# Файл adder.py

class Adder:
    def add(self, x, y):
        print('Not implemented!')          # не реализован
    def __init__(self, start = []):
        self.data = start
    def __add__(self, other):              # Или в подклассах
        return self.add(self.data, other)  # Или возвращаемый тип?

class ListAdder(Adder):
    def add(self, x, y):
        return x + y

class DictAdder(Adder):
    def add(self, x, y):
        new = {}
        for k in x.keys(): new[k] = x[k]
        for k in y.keys(): new[k] = y[k]
        return new
