# Файл validate_descriptors1.py использование разделяемого состояния экземпляра дескриптора

class CardHolder(object):                              # В Python 2.X требуется (object)
    acctlen = 8                                        # Данные класса
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                               # Данные экземпляра
        self.name = name                               # Тоже запускают методы __set__!
        self.age = age                                 # Имя __X не требуется: в дескрипторе
        self.addr = addr                               # Имя addr не является управляемым
                                                       # remain не имеет данных
    class Name(object):
        def __get__(self, instance, owner):            # Имена классов: локальные в CardHolder
            return self.name
        def __set__(self, instance, value):
            value = value.lower().replace(' ', '_')
            self.name = value
    name = Name()    

    class Age(object):
        def __get__(self, instance, owner):
            return self.age                            # Использовать данные дескриптора
        def __set__(self, instance, value):
            if value < 0 or value > 150:
                raise ValueError('invalid age')        # недопустимый возраст
            else:
                self.age = value
    age = Age()

    class Acct(object):
        def __get__(self, instance, owner):
            return self.acct[:-3] + '***'
        def __set__(self, instance, value):
            value = value.replace('-', '')
            if len(value) !=instance.acctlen:          # Использовать данные
                                                       # экземпляра класса
                raise TypeError('invald acct number')  # недопустимый номер счета
            else:
                self.acct = value
    acct = Acct()
    
    class Remain(object):
        def __get__(self, instance, owner):
            return instance.retireage - instance.age   # Запускается Age.__get__
        def __set__(self, instance, value):
            raise TypeError('cannot set remain')       # Установка не разрешена
    remain = Remain()
                                
                                
