# Файл registry-deco.py
# Регистрация декорированных объектов в API-интерфейсе

registry = {}
def register(obj):                               # Декоратор для классов и функций
    registry[obj.__name__] = obj                 # Добавление в реестр
    return obj                                   # Возвращение самого объекта, не оболочки

@register
def spam(x):
    return(x ** 2)                               # spam = register(spam)

@register
def ham(x):
    return(x ** 3)

@register
class Eggs:                                      # Eggs = register(Eggs)
    def __init__(self, x):
        self.data = x ** 4
    def __str__(self):
        return str(self.data)

print('Registry:')                               # Реестр
for name in registry:
    for name in registry:
        print(name, '=>', registry[name], type(registry[name]))

print('\mManual calls:')                         # Вызовы
print(spam(2))                                   # Обращение к объектам вручную
print(ham(2))                                    # Последующие вызовы не перехватываются
X = Eggs(2)
print(X)

print('\nRegistry calls:')                       # Вызовы из реестра
for name in registry:
    print(name, '=>', registry[name] (2))        # Обращение из реестра
