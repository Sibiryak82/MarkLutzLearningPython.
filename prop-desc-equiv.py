# Файл prop-desc-equiv.py

class Property:
    def __init__(self, fget=None, fset=None, fdel=None, doc=None):
        self.fget = fget
        self.fset = fset
        self.fdel = fdel                                            # Сохранить несвязанный метод
        self.__doc__ = doc                                          # или другие вызываемые объекты
    def __get__(self, instance, instancetype=None):
        if instance is None:
            return self
        if self.fget is None:
            return self
        if self. fget is None:
            raise AttributeError("can't get attribute")             # нельзя извлечь атрибут
        return self.fget(instance)                                  # Передать instance экземпляру self
                                                                    # в методах доступа к свойствам
    def __set__(self, instance, value):
        if self.fset is None:
            raise AttributeError("can't get attribute")             # нельзя установить атрибут
        self.fset(instance, value)
    def __delete__(self, instance):
        if self.fdel is None:
            raise AttributeError("can't get attribute")             # нельзя удалить атрибут
        self.fdel(instance)
class Person:
    def getName(self): print('getName...')
    def setName(self, value): print('setName...')
    name = Property(getName, setName)                               # Использовать подобно property()
x = Person()
x.name
x.name = 'Bob'
del x.name
