# Файл typesub-class.ру

# Создание подкласса встроенного типа/класса списка
# Отображает 1..N на 0..N-1; обращается к встроенной версии

class MyList(list):
    def __getitem__(self, offset):
        print('(indexing %s at %s)' % (self, offset))
        return list.__getitem__(self, offset - 1)
if __name__ == '__main__':
    print(list('abc'))
    x = MyList('abc')            # Метод __init__, унаследованного от списка
    print(x)                     # Метод __repr__, унаследованного от списка

    print(x[1])                  # MyList.__getitem__
    print(x[3])                  # Настраиваемый метод из суперкласса

    x.append('spam'); print(x)   # Атрибуты из суперкласса списка
    x.reverse(); print(x)
