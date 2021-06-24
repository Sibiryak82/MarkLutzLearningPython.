# Файл mylist.py

class MyList:
    def __init__(self, start):
        # self.wrapped = start[:]              # Копировать start, чтобы не было
                                               # побочных эффектов
        self.wrapped = list(start)             # Обеспечить здесь наличие списка
    def __add__(self, other):
        return MyList(self.wrapped + other)
    def __mul__(self, time):
        return MyList(self.wrapped * time)
    def __getitem__(self, offset):             # В Python 3.X также передается срез
        return self.wrapped[offset]            # для итерирования, если нет __iter__
    def __len__(self):
        return len(self.wrapped)
    def __getslice__(self, low, high):         # В Python 3.X игнорируется:
        return MyList(self.wrapped[low:high])  # используется __getitem__
    def append(self, node):
        self.wrapped.append(node)
    def __getattr__(self, name):               # Остальные методы: сортировка/
        return getattr(self.wrapped, name)     # обращение порядка/ и.т.д
    def __repr__(self):                        # Обобщенный метод отображения
        return repr(self.wrapped)

if __name__ =='__main__':
    x = MyList('spam')
    print(x)
    print(x[2])
    print(x[1:])
    print(x + ['eggs'])
    print(x * 3)
    x.append('a')
    x.sort()
    print(''.join(c for c in x))
