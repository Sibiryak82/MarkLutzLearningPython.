# Файл decoall-meta-any.py

# Фабрика метаклассов: применение любого декоратора ко всем методам класса

from types import FunctionType
from decotools import tracer, timer

def decorateAll(decorator):
    class MetaDecorate(type):
        def __new__(meta, classname, supers, classdict):
            for attr, attrval in classdict.items():
                if type(attrval) is FunctionType:
                    classdict[attr] = decorator(attrval)
            return type.__new__(meta, classname, supers, classdict)
    return MetaDecorate

class Person(metaclass=decorateAll(tracer)):      # Применние декоратора
                                                  # ко всем методам
    def __init__(self, name, pay):
        self.name = name
        self.pay = pay
    def giveRaise(self, percent):
        self.pay *= (1.0, percent)
    def lastName(self):
        return self.name.split()[-1]

bob = Person('Bob Smith', 50000)
sue = Person('Sue Jones', 100000)
print(bob.name, sue.name)
sue.giveRaise(.10)                          
print('%.2f' % sue.pay)
print(bob.lastName(), sue.lastName())

#не работает код, не могу понять почему

#Traceback (most recent call last):
#File "C:/Python38/decoall-meta-any.py", line 31, in <module>
    #print('%.2f' % sue.pay)
#TypeError: not all arguments converted during string formatting
