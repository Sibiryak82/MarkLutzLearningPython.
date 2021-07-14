"""
Файл access1.py (Python 3.X + 2.X)

Защита для атрибутов, извлекаемых из экземпляра класса.
Пример использования приведен в коде самотестирования в конце файла.

Декоратор такой же, как Doubler = Private('data', 'size')(Doubler).
Private возвращает onDecorator, onDecorator возвращает onInstance,
а в каждом экземпляре onInstance внедрен экземпляр Doubler.
"""

traceMe = False
def trace(*args):
    if traceMe: print('[' + ' '.join(map(str, args)) + ']')

def Private(*privates):                                                  # privates в объемлющей видимости
    def onDecorator (aClass):                                            # aClass в объемлющей области видимости
        class onInstance:                                                # wrapped в атрибуте экземпляра
            def __init__(self, *args, **kargs):
                self.wrapped = aClass(*args, **kargs)

            def __getattr__(self, attr):                                 # Для собственных атрибутов
                                                                         # getattr не вызывается
                trace('get:', attr)                                      # Предполагается, что остальные внутри wrapped
                if attr in privates:
                    raise TypeError('private attribute fetch: ' + attr)
                else:
                    return getattr(self.wrapped, attr)

            def __setattr__(self, attr, value):                          # Операции доступа извне
                trace('set:', attr, value)                               # Остальные выполняются нормально
                if attr == 'wrapped':                                    # Разрешить доступ к собственым
                                                                         # атрибутам
                    self.__dict__[attr] = value                          # Избежать зацикливания
                elif attr in privates:
                    raise TypeError('private attribute change: ' + attr)
                else:
                    setattr(self.wrapped, attr, value)                   # Атрибуты внутреннего объекта
        return onInstance                                                # Либо использовать __dict__
    return onDecorator

if __name__ == '__main__':

    traceMe = True

    @Private('data', 'size')                                             # Doubler = Private(...)(Doubler)
    class Doubler:
        def __init__(self, label, start):
            self.label = label                                           # Операции доступа внутри целевого класса
            self.data = start                                            # Не перехватываются: выполняются нормально
        def size(self):
            return len(self.data)                                        # Методы запускаются без какой-либо проверки
        def double(self):                                                # Потому что защита не наследуется
            for i in range(self.size()):
                self.data[i] = self.data[i] * 2
        def display(self):
            print('%s => %s' % (self.label, self.data))

X = Doubler('X is', [1, 2, 3])
Y = Doubler('Y is', [-10, -20, -30])


print(X.label)                                                           # Операции доступа извне целевого класса
X.display(); X.double(); X.display()                                     # Перехватываются: проверяются
                                                                         # делегтруются
print(Y.label)
Y.display(); Y.double()
Y.label = 'Spam'
Y.display()
            




        
                    


