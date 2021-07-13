# Файл calltaker.py

def tracer(func):                                   # Использовать с __call__ функцию, но не класс
    calls = 0                                       # Иначе self - только экземпляр декоратора
    def onCall(*args, **kwargs):                    # Или применить [onCall.calls += 1]
                                                    # для Python 2.X+3.X
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return onCall

if __name__ == '__main__':
    
    # Применяется к простым функциям

    @tracer
    def spam(a, b, c):                              # spam = tracer(spam)
        print(a + b + c)                            # onCall запоминает spam
    @tracer
    def eggs(N):
        return 2 ** N
    spam(1, 2, 3)                                   # Запускается onCall(1, 2, 3)
    spam(a=4, b=5, c=6)
    print(eggs(32))

    # Применяется также к функциям методов уровня класса!
    class Person:
        def __init__(self, name, pay):
            self.name = name
            self.pay = pay
        @tracer
        def giveRaise(self, percent):               # giveRaise = tracer(giveRaise)
            self.pay *= (1.0 + percent)             # onCall запоминает giveRaise

        @tracer
        def lastName(self):                         # lastName = tracer(lastName)
            return self.name.split()[-1]
    print('methods...')                             # методы...
    bob = Person('Bob Smith', 50000)
    sue = Person('Sue Jones', 100000)
    print(bob.name, sue.name)
    sue.giveRaise(.10)                              # Запускается onCall(sue, .10)
    print(int(sue.pay))                   
    print(bob.lastName(), sue.lastName())           # Запускается onCall(bob)
                                                    # lastName в области видимости
