# Файл getattr-delegate.py

class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):
        return'[Person: %s, %s]' % (self.name, self.pay)
    

class Manager:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)            # Внедрение объекта Person
    def giveRaise(self, percent, bonus=.10):
        self.person.giveRaise(percent + bonus)            # Перехват и делегирование
    def __getattr__(self, attr):
        return getattr(self.person, attr)                 # Делегирование всех
                                                          # остальных атрибутов
    def __repr__(self):
        return str(self.person)                           # Снова требуется перегрузка в Python 3.X)

class Manager2:
    def __init__(self, name, pay):
        self.person = Person(name, 'mgr', pay)
    def giveRaise(self, percent, bonus=.20):
        self.person.giveRaise(percent + bonus)
    def __getattr__(self, attr):
        return getattr(self.person, attr)

    def __repr__(self):
        return str(self.person)                           # Снова требуется перегрузка (в Python 3.X)
    
    

if __name__ =='__main__':
    sue = Person('Sue Jones', job='dev', pay=100000)      
    print(sue.lastName())
    sue.giveRaise(.10)
    print(sue)
    tom = Manager('Tom Smith', 50000)                     # Manager.__init__
    print(tom.lastName())                                 # Manager.__getattr__ -> Person.lastName
    tom.giveRaise(.10)                                    # Manager.giveRaise -> Person.giveRaise
    print(tom)                                            # Manager.__repr__ -> Person.__repr__
    bob = Manager2('Bob Davis', 200000)
    print(bob.lastName())
    bob.giveRaise(.10)
    print(bob)
    
    
