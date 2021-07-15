# Файл decoall-meta.py

# Метакласс, который добавляет декоратор трассировки к каждому методу
# клиентского класса

from types import FunctionType
from decotools import tracer

class MetaTrace(type):
    def __new__(meta, classname, supers, classdict):
        for attr, attrval in classdict.items():
            if type(attrval) is FunctionType:                     # Метод?
                classdict[attr] = tracer(attrval)                 # Декорировать его
        return type.__new__(meta, classname, supers, classdict)   # Создать класс

class Person(metaclass=MetaTrace):
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay

    def giveRaise(self, percent):
        self.pay *= (1.0 + percent)
    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())
