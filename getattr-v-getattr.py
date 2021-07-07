# Файл getattr-v-getattr.py

class GetAttr:
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattr__(self, attr):                        # Только при операциях извлечения
                                                        # неопределенных атрибутов
        print('get: ' + attr)                           # Не при извлечении атрибута attr1:
                                                        # наследуется из класса
        if attr == 'attr3':                             # Не при извлечении атрибута attr2:
                                                        # хранится в экземпляре
            return 3
        else:
            raise AttributeError(attr)

X = GetAttr()
print(X.attr1)
print(X.attr2)
print(X.attr3)
print('-'*20)

class GetAttribute(object):                             # Добавить (object) в Python 2.X
    attr1 = 1
    def __init__(self):
        self.attr2 = 2
    def __getattribute__(self, attr):                   # При операциях извлечения всех атрибутов
        print('get: ' + attr)                           # Использование суперкласса во избежании
                                                        # зацикливания
        if attr == 'attr3':
            return 3
        else:
            return object.__getattribute__(self, attr)

X = GetAttribute()
print(X.attr1)
print(X.attr2)
print(X.attr3)

