# Файл skipper.py

class SkipObject:
    def __init__(self, wrapped):   # сохранить объект для использования
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped) # каждый раз новый итератор

class SkipIterator:
    def __init__(self,wrapped):
        self.wrapped = wrapped # Информация о состоянии итератора
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped): # Прекратить итерацию
            raise StopIteration
        else:
            item = self.wrapped[self.offset] # Иначе возвратить и пропустить
            self.offset += 2
            return item
if __name__ == '__main__':
    alpha = 'abcdef'
    skipper = SkipObject(alpha)         # Создать объект контейнер
    I = iter(skipper)                   # Создать на нем итератор
    print(next(I), next(I), next(I))    # Посетить смещения 0, 2, 4

    for x in skipper:                   # for автоматически вызывает __iter__
        for y in skipper:               # Вложенные for снова каждый раз
                                        # вызывают __iter__
            print(x + y, end=' ')       # Каждый итератор имеет собственное
                                        # состояние, смещения
