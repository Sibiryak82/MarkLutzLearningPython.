# getattr-computed.py

class AttrSquare:
    def __init__(self, start):
        self.value = start                  # Запускается __setattr__!

    def __getattr__(self, attr):            # При операциях извлечения
                                            # неопределенных атрибутов
        if attr == 'X':
            return self.value ** 2          # value не является неопределенным
        else:
            raise AttributeError(attr)

    def __setattr__(self, attr, value):     # При операциях присваивания всех атрибутов
        if attr == 'X':
            attr = 'value'
        self.__dict__[attr] = value

A = AttrSquare(3)                           # 2 экземпляра класса с перегрузкой
B = AttrSquare(32)                          # Каждый имеет отличающуюся информацию состояния

print(A.X)                                  # 3 ** 2
A.X = 4
print(A.X)                                  # 4 ** 2
print(B.X)                                  # 32 ** 2(1024)
