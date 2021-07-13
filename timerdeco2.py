# Файл timerdeco2.py
# не работает, предположительно из-за time.clock() (версии питона)

import time

def timer(label='', trace=True):                     # При аргументах декоратора:
                                                     # сохранение аргументов
    class Timer:
        def __init__(self, func):                    # При декорировании @: сохранение
                                                     # декорированной функции
            self.func = func
            self.alltime = 0
        def __call__(self, *args, **kargs):          # При вызовах: вызов исходной функции
            start = time.clock()
            result = self.func(*args, **kargs)
            elapsed = clock() - start
            self.alltime += elapsed
            if trace:
                format = '%s %s: %.5f, %.5f'
                values = (label, self.func.__name__, elapsed, self.alltime)
                print(format % values)
            return result
    return Timer
            
    
