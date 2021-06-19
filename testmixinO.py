# Файл testmixinO.py
from listinstance import ListInstance # Получить класс инструмента для
                                      #вывода списка атрибутов

class Super:
    def __init__(self):         # Метод __init__ суперкласса
        self.data1 = 'spam'     # Создать атрибуты экземпляра
    def ham(self):
        pass

class Sub(Super, ListInstance): # Подмешbвание ham и __str__
    def __init__(self):         # Классы, выводящие списки атрибутов,
                                # имеют доступ к self
        Super.__init__(self)
        self.data2 = 'eggs'     # Дополнительные атрибуты экземпляра
        self.data3 = 42 
    def spam(self):             # Определить здесь еще один метод
        pass

if __name__ == '__main__':
    X = Sub()
    print(X)                    # Выполняется подмешанный метод __str__
