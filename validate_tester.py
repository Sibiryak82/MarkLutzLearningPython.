# Файл validate_tester.py

# выдает ошибку


def loadclass():
    import sys, importlib
    modulename = sys.argv[1]                                           # Имя модуля в командной строке
    module = importlib.import_module(modulename)                       # Импортирование модуля
                                                                       # по имени в строке
    print('[Using: %s]' % module.CardHolder)                           # getattr() здесь не требуется
    return module.CardHolder

def printholder(who):
    print(who.acct, who.name, who.age, who.remain, who.addr, sep=' / ')

if __name__ == '__main__':
    CardHolder = loadclass()
    bob = CardHolder('12345-5678', 'Bob Smith', 40, '123 main st')
    printholder(bob)
    bob.name = 'Bob Q. Smith'
    bob.age = 50
    bob.acct = '23-45-67-89'
    printholder(bob)

    sue = CardHolder('5678-12-34', 'Sue Jones', 35, '124 main st')
    printholder(sue)
    try:
        sue.age = 200
    except:
        print('Bad age for Sue')                                       # Недопустимый возраст для sue
    try:
       sue.remain = 5
    except:
        print("Can't set sue.remain")                                  # Невозможно установить sue.remain
    try:
        sue.acct = '1234567'
    except:
        print('Bad acct for Sue')                                      # Недопустимый номер счета для sue
