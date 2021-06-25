# Файл multiset.py

from setwrapper import Set

class MultiSet(Set):
    
    """
Насдедует все имена Set, но расширяет intersect и union для поддержки
множества операндов;
обратите внимание, что self - по-прежнему первый аргумент (теперь хранящийся
в *args);
кроме того, унаследованные операции & и | здесь вызывает новые методы с
2 аргументами, но обработка более 2 аргументов требует вызова метода, не
выражения; intersect не удаляет дубликаты: это делает конструктор Set.
"""

def intersect(self, *others):
    res = []
    for x in self:                    # Просмотр первой последовательности
        for other in others:          # Для всех оставшихся аргументов
            if x not in other: break  # Элемент в каждой последовательности?
        else:                         # Нет: выйти из цикла
            res.append(x)             # Да: добавить элемент в конец
    return Set(res)

def union(*args):                     # self - это args[0]
    res = []
    for seg in args:                  # Для всех аргументов
        for x in seg:                 # Для всех узлов
            if not x in res:
                res.append(x)         # Добавить новые элементы к результату
    return Set(res)

