# Файл bothmethods.py

class Methods:
    def imeth(self, x):     # Нормальный метод экpемпляра: передается self
        print([self, x])

    def smeth(x):           # Статический метод: экземпляр не передается
        print([x])

    def cmeth(cls, x):      # Метод класс: получает класс, а не экземпляр
        print([cls, x])

    smeth = staticmethod(smeth) # Делает smeth статическим методов (или @: впереди)
    cmeth = classmethod (cmeth) # Делает cmeth методом класса (или @: впереди)
