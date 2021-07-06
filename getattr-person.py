# Файл getattr-person.py

class Person:                                  # Код переносимый: Python 2.X или 3.X
    def __init__(self, name):                  # При [Person()]
        self._name = name                      # Запускается __setattr__!
    def __getattr__(self, attr):               # При [obj. неопределенный_атрибут]
        print('get: ' + attr)
        if attr == 'name':                     # Перехват имени name: не хранится в экземпляре
            return self._name                  # Зацикливания нет: реальный атрибут
        else:                                  # Остальные являются ошибками
            raise AttributeError(attr)
    def __setattr__(self, attr, value):        # При [obj.любой_атрибут = value]
        print('set: ' + attr)
        if attr == 'name':
            attr = '_name'                     # Установка внутреннего имени
        self.__dict__[attr] = value            # Избегание зацикливания
    def __delattr__(self, attr):               # При [del obj.любой_атрибут]
        print('del: ' + attr)
        if attr == 'name':
            attr = '_name'                     # Избегание зацикливания,
        del self.__dict__[attr]                # но оно гораздо менее распространено
bob = Person('Bob Smith')                      # Экземпляр bob имеет управляемый атрибут
print(bob.name)                                # Запускается __getattr__
bob.name = 'Robert Smith'                      # Запускается __setattr__
print(bob.name)
del bob.name                                   # Запускается __delattr__
print('-'*20)
sue = Person('Sue Jones')                      # Экземпляр sue также наследует свойство
print(sue.name)
#print(Person.name.__doc__)                    # Эквивалент здесь отсутвует
    
