# Файл validate_getattr.py

class CardHolder:
    acctlen = 8                                           # Данные класса
    retirage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                                  # Данные экземпляра
        self.name = name                                  # Тоже запускают __setattr__
        self.age = age                                    # Имя _acct не корректируются
                                                          # проверяется name
        self.addr = addr                                  # Имя addr не является управляемым
                                                          # remain не имеет данных
    def __getattr__(self, name):
        if name == 'acct':                                # При извлечении неопределенных атрибутов
            return self._acct[:-3] + '***'                # name, age, addr определены
        elif name == 'remain':
            return self.retirage - self.age               #  Не запускает __getattr__
        else:
            raise AttributeError(name)

    def __setattr__(self, name, value):
        if name == 'name':                                # При операциях присваивания всех атрибутов
            value = value.lower().replace(' ', '_')       # addr храниться напрямую
        elif name == 'age':                               # acct корректируется в _acct
            if value < 0 or value > 150:
                raise ValueError('invalid age')           # недопустимый возраст
        elif name == 'acct':
            name = 'acct'
            value = value.replace('-','')
            if len(value) != self.acctlen:
                raise TypeError('invald acct number')     # недопустимый номер счета
        elif name == 'remain':
            raise TypeError('cannot set remain')
        self.__dict__[name] = value                       # Избегание зацикливания
                                                          # (или через object)
