# Файл decorator4.py

def tracer(func):                               # Состояние через объемлющую область
                                                # видимости  и нелокальную пременную
    calls = 0                                   # Вместо атрибутов класса или глобальных переменных
    def wrapper(*args, **kwargs):               # calls - для каждой функции, 
                                                # не глобальная переменная
        nonlocal calls
        calls += 1
        print('call %s to %s' % (calls, func.__name__))
        return func(*args, **kwargs)
    return wrapper

@tracer
def spam(a, b, c):                              # То же, что и spam = tracer(spam)
    print(a + b + c)

@tracer
def eggs(x, y):                                 # То же, что и eggs = tracer(eggs)
    print(x ** y)

spam(1, 2, 3)                                   # На самом деле вызывается wrapper, привязанный к spam
spam(a=4, b=5, c=6)                             # wrapper вызывает spam

eggs(2, 16)                                     # На самом деле вызывается wrapper, привязанный к eggs
eggs(4, y=4)                                    # Нелокальная переменная _является_ отдельной
                                                # для каждого случая декорирования!
