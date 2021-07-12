# decorator3.py

calls = 0
def tracer(func):                                         # Состояние через объемлющую область
                                                          # видимости и глобальную переменную
    def wrapper(*args, **kwargs):                         # Вместо атрибутов класса
        global calls                                      # глобальная переменная, не для каждой функции
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):                                        # То же, что и spam = tracer(spam)
    print(a + b + c)        

@tracer
def eggs(x, y):                                           # То же, что и eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)                                             # На самом деле вызывается wrapper, присвоенный spam
spam(a=4, b=5, c=6)                                       # wrapper вызывает spam

eggs(2, 16)                                               # На самом деле вызывается wrapper, присвоенный eggs
eggs(4, y=4)                                              # Глобальная переменная calls не является
                                                          # отдельной для каждого случая декориования!
