# Файл desc-person.py

class Name:
    "name descriptor docs"                 # Документация по свойству name
    def __get__(self, instance, owner):
        print('fetch...')                  # извлечение
        return instance._name
    def __set__(self, instance, value):
        print('change...')                 # изменение
        instance._name = value
    def __delete__(self, instance):
        print('remove...')                 # удаление
        del instance._name

class Person:                              # Добавить (object) в Python 2.X
    def __init__(self, name):
        self._name = name
    name = Name()                          # Присвоить дескриптор атрибуту

bob = Person('Bob Smith')                  # Экземпляр bob имеет управляемый атрибут
print(bob.name)                            # Запускается Name.__get__
bob.name = 'Robert Smith'                  # Запускается Name.__set__
print(bob.name)
del bob.name                               # Запускается Name.__delete__

print('-'*20)
sue = Person('Sue Jones')                  # Экзумпляр sue тоже наследует дескриптор
print(sue.name)
print(Name.__doc__)                        # Или help(Name)
