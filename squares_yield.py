# Файл squares_yield.py

class Squares:                       # Генератор на основе __iter__ + yield
    def __init__(self, start, stop): # Метод __next__ является
                                     #   автоматическим/подразумеваемым
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop +1):
            yield value ** 2
    
                                     
