# Файл classexc.py

class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

def raiser0():
    X = General()                                 # Генерирует экземпляр суперкласса
    raise X

def raiser1():
    X = Specific1()                               # Генерирует экземпляр подкласса
    raise X

def raiser2():
    X = Specific2()                               # Генерирует экземпляр другого подкласса
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:                               # Соответсвует суперклассу General1 или любому его подклассу
        import sys
        print('caught: %s' % sys.exc_info()[0])
