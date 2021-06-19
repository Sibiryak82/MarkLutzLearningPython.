# factory.py

def factory(aClass, *pargs, **kargs): # Кортеж или словарь с переменным
                                      # количеством аргументов
    return aClass(*pargs, **kargs)    # Вызывает aClass (или apply в Python 2.X
class Spam:
    def doit(self, message):
        print(message)

class Person:
    def __init__(self, name, job=None):
        self.name = name
        self.job = job
object1 = factory(Spam)                     # Создать объект Spam
object2 = factory(Person, "Arthur", "King") # Создать объект Person
object3 = factory(Person, name = 'Brian')   # То же самое, с ключевым аргу-
                                            # ментом и стандартным значением
                                      
