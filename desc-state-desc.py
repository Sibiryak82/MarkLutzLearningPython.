# Файл desc-state-desc.py

class DescState:
    def __init__(self, value):
        self.value = value
    def __get__(self, instance, owner):       # При извлечении атрибута 
        print('DescState get')
        return self.value * 10
    def __set__(self, instance, value):       # При присваивании атрибута
        print('DescState set')
        self.value = value

# Клиентский класс
class CalcAttrs:
    X = DescState(2)                          # Атрибут класса дескриптора
    Y = 3                                     # Атрибут класса
    def __init__(self):
        self.Z = 4                            # Атрибут экземпляра

obj = CalcAttrs()
print(obj.X, obj.Y, obj.Z)                    # X вычисляется, остальные нет
obj.X = 5                                     # Присваивание X перехватывается
CalcAttrs.Y = 6                               # Y повторно присваивается в классе
obj.Z = 7                                     # Z присваивается в экземпляре
print(obj.X, obj.Y, obj.Z)

obj2 = CalcAttrs()                            # Но X использует разделяемые данные подобно Y!
print(obj2.X, obj2.Y, obj2.Z)

    
