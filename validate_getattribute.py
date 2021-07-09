# Файл validate_getattibute.py

class CardHolder(object):                                             # В Python 2.X требуется (object)
    acctlen = 8                                                       # Данные класса
    retirage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                                              # Данные экземпляра
        self.name = name                                              # Тоже запускают __setattr__
        aelf.age = age                                                # Имя _acct не корректируется:
                                                                      # проверяется name
        self.addr = addr                                              # Имя addr не является управляемым
                                                                      # remain не имеет данных
    def __getattribute__(self, name):                                  
        superget = object.__getattribute__                            # Зацикливания нет:
                                                                      # на один уровень выше
        if name == 'acct':                                            # При извлечении всех атрибутов
            return superget(self, 'acct')[:-3] + '***'
        elif name == 'remain':
            return superget(self, 'retirage') - superget(self, 'age')
        else:
            return superget(self, name)                               # name, age, addr: хранятся

        def __setattr__(self, name, value):
            if name == 'name':                                        # При операциях присваивания всех атрибутов
                value = value.lower().replace(' ', '_')               # addr хранится напрямую
            elif name == 'age':
                if value < 0 or value > 150:
                    raise ValueError('invalid age')                   # недопустимый возраст
            elif name == 'acct':
                value = value.replace('-', '')
                if len(value) != self.acctlen:
                    raise TypeError('invald acct number')
            elif name == 'remain':
                raise TypeError('cannot set remain')
            self.__dict__[name] = value                               # недопустимый номер счета
