# Файл validate_properties.py

class CardHolder(object):                         # В Python 2.X требуется (object)
    acctlen = 8                                   # Данные класса
    retireage = 59.5

    def __init__(self, acct, name, age, addr):
        self.acct = acct                          # Данные экземпляра
        self.name = name                          # Тоже запускают методы установки
                                                  # свойств!
        self.age = age                            # Имя __X корректируется, чтобы
                                                  # содержать имя класса
        self.addr = addr                          # Имя addr не корректируется
                                                  # Свойство remain не имеет данных
    def getName(self):
        return self.__name
    def setName(self, value):
        value = value.lower().replace(' ', '_')
        self.__name = value
    name = property(getName, setName)

    def getAge(self):
        return self.__age
    def setAge(self, value):
        if value < 0 or value > 150:
            raise ValueError('invalid age')       # недопустимый возраст

        else:
            self.__age = value
    age = property(getAge, setAge)

    def getAcct(self):
        return self.__acct[:-3] + '***'
    def setAcct(self, value):
        value = value.replace('-', '')
        if len(value) != self.acctlen:
            raise TypeError('invald acct number')# недопустимый номер счета
        else:
            self.__acct = value
    acct = property(getAcct, setAcct)

    def remainGet(self):                          # Могло быть методом, а не атрибутом
        return self.retireage - self.age          # если только уже не используется
                                                  # как атрибут
    remain = property(remainGet)
        
