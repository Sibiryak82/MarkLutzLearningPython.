# Файл decorator5.py

def tracer(func):                                 # Сщстояние через объемлющую область
                                                  # видимости и атрибуты функций
    def wrapper(*args, **kwargs):                 # calls - для каждой функции
                                                  # не глобальная переменная
        wrapper.calls += 1
        print('call %s to %s' % (wrapper.calls, func.__name__))
        return func(*args, **kwargs)
    wrapper.calls = 0
    return wrapper

@tracer
def spam(a, b, c):                                # То же, что и spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):                                   # То же, что и eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)                                     # На самом деле вызывает wrapper, присвоенный spam
spam(a=4, b=5, c=6)                               # wraper вызывает spam

eggs(2, 16)                                       # На самом деле вызывается wrapper, присвоенный eggs
eggs(4, y=4)                                      # Значение wrapper.calls _относится_
                                                  # к каждому случаю декорирования
