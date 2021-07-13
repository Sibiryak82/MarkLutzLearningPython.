# Файл singletons.py
# Python 3.X и 2.X: глобальная таблица

instances = {}

def singleton(aClass):                                  # При декорировании @
    def onCall(*args, **kwargs):                        # Присоздании экземпляров
        if aClass not in instances:                     # Один элемент словаря на класс
            instances[aClass] = aClass(*args, **kwargs)
        return instances[aClass]
    return onCall

@singleton                                              # Person = singleton(Person)
class Person:                                           # Повторная привязка Person к onCall
    def __init__(self, name, hours, rate):              # onCall запоминает Person
        self.name = name
        self.hours = hours
        self.rate = rate
    def pay(self):
        return self.hours * self.rate

@singleton                                              # Spam = singleton(Spam)
class Spam:                                             # Повторная привязка Spam к onCall
    def __init__(self, val):                            # onCall запоминает Spam
        self.attr = val

bob = Person('Bob', 40, 10)                             # В действительности вызывается onCall
print(bob.name, bob.pay())

sue = Person('Sue', 50, 20)                             # То же самое, единственный объект
print(sue.name, sue.pay())

X = Spam(val=42)                                        # Один экземпляр Person,
                                                        # один экземпляр Spam
Y = Spam(99)
print(X.attr, Y.attr)

