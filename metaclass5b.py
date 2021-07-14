# Файл metaclass5b.py

class SuperMeta(type):
    def __call__(meta, classname, supers, classdict):            # По имени, 
                                                                 # не встроенное
        print('In SuperMeta.call:', classname)
        return type.__call__(meta, classname, supers, classdict)

class SubMeta(SuperMeta):                                        # Создается стандартным type
    def __init__(Class, classname, supers, classdict):           # Переопределение
                                                                 # type.__init__
        print('In SubMeta init:', classname)

print(SubMeta.__class__)
print([n.__name__ for n in SubMeta.__mro__])
print()
print(SubMeta.__call__)                                          # Не дескриптор данных, если найден по имени
print()
SubMeta.__call__(SubMeta, 'xxx', (), {})                         # Явные вызовы работают:
                                                                 # наследование классов
print()
SubMeta('yyy', (), {})                                           # Но неявные обращения к встроенным именам
                                                                 # не работают: type
