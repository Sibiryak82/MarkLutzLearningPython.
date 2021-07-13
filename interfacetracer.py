# Файл interfacetracer.py

def Tracer(aClass):                                # При декодировании @
    class Wrapper:
        def __init__(self, *args, **kargs):        # При создании экземпляров
            self.fetches = 0
            self.wrapped = aClass(*args, **kargs)  # Использование имени из 
                                                   # объемлющей области видимости
        def __getattr__(self, attrname):
            print('Trace: ' + attrname)            # Перехват всех атрибутов кроме собственных
            self.fetches += 1
            return getattr(self.wrapped, attrname) # Делегирование
                                                   # внутреннеум объекту
    return Wrapper

if __name__ == '__main__':
    @Tracer
    class Spam:                                    # Spam = Tracer(Spam)
        def display(self):                         # Spam повторно привязывается к Wrapper
            print('Spam!' * 8)

    @Tracer
    class Person:                                  # Person = Tracer(Person)
        def __init__(self, name, hours, rate):     # Wrapper запоминает Person
            self.name = name
            self.hours = hours
            self.rate = rate
        def pay(self):                             # Операции доступа извне класса отслеживаются
            return self.hours * self.rate          # Операции доступа внутри
                                                   # методов не отслеживаются
                                                   
food = Spam()                                      # Запускается Wrapper()
food.display()                                     # Запускается __getattr__
print([food.fetches])

bob = Person('Bob', 40, 50)                        # bob - на самом деле экземпляр Wrapper
print(bob.name)                                    # Wrapper содержит внедренный экземпляр Person
print(bob.pay())

print('')
sue = Person('Sue', rate=100, hours=60)            # sue - другой экзумпляр Wrapper
print(sue.name)                                    # с другим экземпляром Person
print(sue.pay())

print(bob.name)                                    # bob имеет отличающееся состояние
print(bob.pay())
print([bob.fetches, sue.fetches])                  # Атрибуты Wrapper не отслеживаются


        




            
