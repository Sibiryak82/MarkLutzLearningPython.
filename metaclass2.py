# Файл metaclass2.py

class MetaTwo(type):
    def __new__(meta, classname, supers, classdict):
        print('In MetaTwo.new:', classname, supers, classdict, sep='\n...')
        return type.__new__(meta, classname, supers, classdict)

    def __init__(Class, classname, supers, classdict):
        print('In MetaTwo.init:', classname, supers, classdict, sep='\n...')
        print('...init class object:', list(Class.__dict__.keys()))

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaTwo):    # Наследуется от Eggs, экземпляр MetaTwo
    data = 1                            # Атрибут данных класса
    def meth(self, arg):                # Атрибут метода класса
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
