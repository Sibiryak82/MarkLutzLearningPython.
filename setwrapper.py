# setwrapper.py

class Set:
    def __init__(self, value = []):   # Конструктор
        self.data = []                # Управляет списком
        self.concat(value)

    def intersect(self, other):       # other - любая последовательность
        res = []                      # self - подчиненый объект
        for x in self.data:
            if x in other:            # Выбрать общие элементы
                res.append(x)
        return Set(res)               # Возвратить новый объект Set

    def union(self, other):           # other - любая последовательность
        res = self.data[:]            # Копировать список
        for x in other:               # Добавить элементы в other
            if not x in res:
                res.append(x)
        return Set(res)

    def concat(self, value):          # value: список, Set...
        for x in value:               # Удаляет дубликаты
            if not x in self.data:
                self.data.append(x)

#def __len__(self): return len(self.data   # len(self), если self истинно
#def __getitem__(self, key): return self.data[key]       # self[i], self[i:j]
#def __and__(self, other): return self.intersect(other)  # self & other
#def __or__(self, other): return self.union(other)       # self | other
#def __repr__(self): return 'Set:' + repr(self.data)     # print(self),...
#def __iter__(self): return iter(self.data)              # for x in self
        
