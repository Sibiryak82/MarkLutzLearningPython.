# Файл person.py (начало)

class Person:  # Начало класса
    def __init__(self, name, job, pay):
        self.name = name
        self.job = job
        self.pay = pay

# Добавление стандартных значений для аргументов конструктора
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.name = job
        self.pay = pay

# Добавление кода самотестирования
class Person:
    def __init__(self, name, job=None, pay=0):
        self.name = name
        self.job = job
        self.pay = pay
bob = Person('Bob Smith')       # Тестирование класса
sue = Person('Sue Jones', job='dev', pay=10000)

print(bob.name, bob.pay)
print(sue.name, sue.pay)
class Person:
    def __init__(self, name, job=None, pay=0):
	    self.name = name
	    self.job = job
	    self.pay = pay
		
if __name__ == '__main__':
	bob = Person('Bob Smith')
	sue = Person('Sue Jones', job='dev', pay=100000)
	print(bob.name, bob.pay)
	print(sue.name, sue.pay)
	print(bob.name.split()[-1])
	sue.pay *= 1.10
	print('%.2f' % sue.pay)

# Добавление методов для инкапсуляции операций с
# целью повышения удобства сопровождения
class Person:
    def __init__(self, name, job=None, pay=0):
	    self.name = name
	    self.job = job
	    self.pay = pay
    def lastName(self):                    # Методы реализации поведения
        return self.name.split()[-1]       # self - подразумеваемый объект
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))  # Потребуется изменять только здесь
        
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob.name, bob.pay)
    print(sue.name, sue.pay)
    print(bob.lastName(), sue.lastName())  # Использовать новые методы
    sue.giveRaise(.10)                     # вместо жесткого кодирования
    print(sue.pay)

class Person:
    def __init__(self, name, job=None, pay=0):
	    self.name = name
	    self.job = job
	    self.pay = pay
    def lastName(self):
        return self.name.split()[-1]
    def giveRaise(self, percent):
        self.pay = int(self.pay * (1 + percent))
    def __repr__(self):                                   # Добавленный метод
        return '[Person: %s, %s]' % (self.name, self.pay) # Строка для вывода
    
if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())  
    sue.giveRaise(.10)                     
    print(sue)

class Manager(Person):                                  # написание подклассов
    def giveRaise(self, percent, bonus=.10):
        self.pay = int(self.pay * (1 + percent + bonus)) # Плохой способ:
                                                         # вырезание и вставка
class Manager(Person):
    def giveRaise(self, persent, bonus=.10):
        Person.giveRaise(self, persent + bonus)          # Хороший способ: 
                                                         # расширение исходной версии

# Добывление настройки поведения в подкласс        
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
        return '[Person: %s, %s]' % (self.name, self.pay)

class Manager(Person):
    def giveRaise(self, percent, bonus=.10): # Переопределить на этом уровне
        Person.giveRaise(self, percent + bonus) # Вызвать версию из Person

if __name__ == '__main__':
    bob = Person('Bob Smith')
    sue = Person('Sue Jones', job='dev', pay=100000)
    print(bob)
    print(sue)
    print(bob.lastName(), sue.lastName())
    sue.giveRaise(.10)
    print(sue)
tom = Manager('Tom Jones', 'mgr', 50000)  # Создать экземпляр
Manager:'__init__'
tom.giveRaise(.10)                        # Выполняется спец. версия
print(tom.lastName())                     # Выполняется унаследованный метод
print(tom)                                # Выполняется унаследованный __repr__

if __name__ == '__main__':
    ...
    print('--All three--')
    for obj in (bob, sue, tom): # Обработать объекты обобщенным образом        
        obj.giveRaise(.10)      # Выполнить метод giveRaise этого объекта
        print(obj)              # Выполнить общий метод __repr__
    
