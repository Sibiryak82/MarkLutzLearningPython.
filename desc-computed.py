# Файл desc-computed.py

class DescSquare:
    def __init__(self, start):            # Кажый дескриптор имеет 
                                          # собственное состояние
        self.value = start
    def __get__(self, instance, owner):   # При извлечении атрибута
        return self.value ** 2
    def __set__(self, inctance, value):   # При присваивании атрибута
            self.value = value            # Операция удаления и строка
                                          # документация отсутствует 
class Client1:
    X = DescSquare(3)                     # Присвоить экземпляр дескриптора атрибуту класса

class Client2:
    X = DescSquare(32)                    # Еще один экземпляр в другом клиентском классе
                                          # Можно было бы также предусмотреть
                                          # два экземпляра в том же самом классе
c1 = Client1()
c2 = Client2()

print(c1.X)                               # 3 ** 2
c1.X = 4
print(c1.X)                               # 4 ** 2
print(c2.X)                               # 32 ** 2
