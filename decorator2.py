# Файл decoratot2.py

class tracer:                                         # Состояние через атрибуты экземпляра
    def __init__(self, func):                         # При декодировании @
        self.calls = 0                                # Сохранить функцию для вызова в будущем
        self.func = func
    def __call__(self, *args, **kwargs):              # При вызове исходной функции
        self.calls += 1
        print('call %s to %s' % (self.calls, self.func.__name__))   # При вызове исходной функции
        return self.func(*args, **kwargs)
    
@tracer
def spam(a, b, c):                                    # То же, что и spam = tracer(spam)
    print(a + b + c)                                  # Запускается tracer.__init__

@tracer
def eggs(x, y):                                       # То же, что и eggs = tracer(eggs)
    print(x ** y)                                     # eggs помещается в объект tracer

spam(1, 2, 3)                                         # Вызывается экземпляр tracer:
                                                      # запускается tracer.__call__
spam(a=4, b=5, c=6)                                   # spam - атрибут экземпляра

eggs(2, 16)                                           # Вызывается экземпляр tracer, self.func - это eggs
eggs(4, y=4)                                          # self.calls - значения для каждого случая декорирования
