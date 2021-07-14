# Файл metaclass1.py


class MetaOne(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaOne.new:', meta, classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

class Eggs:
    pass

print('making class')                   # создание класса
class Spam(Eggs, metaclass=MetaOne):    # Наследуется от Eggs, экземпляр MetaOne
    data = 1                            # Атрибут данных класса
    def meth(self, arg):                # Атрибут метода класса
        return self.data + arg

print('making instance')                # создание экземпляра
X = Spam()
print('data:', X.data, X.meth(2))
        
