# Файл suare_nonyield.py

class Squares:
    def __init__(self, start, stop): # Генератор, не основанный на yield
        self.start = start           # Множество просомотров: дополительный объект
        self.stop = stop
    def __iter__(self):
        return SquaresIter(self.start, self.stop)

class SquaresIter:
    def __init__(self,start, stop):
        self.value = start - 1
        self.stop = stop
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value +=1
        return self.value ** 2
    
    
