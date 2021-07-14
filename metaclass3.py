# Файл metaclass3.py

# Простая функция тоже может служить в качестве метакласса

def MetaFunc(classname, supers, classdict):
    print('In MetaFunc: ', classname, supers, classdict, sep='\n...')
    return type(classname, supers, classdict)

class Eggs:
    pass

print('making class')
class Spam(Eggs, metaclass=MetaFunc):   # В конце запускается простая функция
    data = 1                            # Функция возвращает класс
    def meth(self, arg):
        return self.data + arg

print('making instance')
X = Spam()
print('data:', X.data, X.meth(2))
    
