# !python
# Файл testmixin.py (Python 2.X + 3.X)
"""
Обобщенный инструмент тестирования подмешиваемых классов вывода списков:
он похож на средство транзитивной перезагрузки модулей из главы 25 первого
тома, но ему передается объект класса (не функции), а в testByNames
добавлена загрузка модуля и класса по стороковым именам в соответствии с
паттерном проектирования 'Фабрика'.
"""
import importlib
def tester(listerclass,sept = False):
    class Super:
        def __init__(self):         # Метод __init__ суперкласса
            self.data1 = 'spam'     # Создать атрибуты экземпляра
        def ham(self):
            pass
    class Sub(Super, listerclass):  # Подмешиваем ham и __str__
        def __init__(self):         # Классы, выводящие списки атрибутов, 
                                    # имеют доступ к self
            Super.__init__(self)
            self.data2 = 'eggs'     # Дополнительные атрибуты экземпляра
            self.data3 = 42
        def spam(self):             # Определить здесь ещё один метод
            pass
    instance = Sub()                # Возвратить экземпляр с помощью __str__
                                    # класса, выводящего список
    print(instance)                 # Выполняется подмешанный метод __str__
                                    #  (или через str(x))
    if sept: print('-' * 80)

def testByNames(modname, classname, sept=False):
    modobject = importlib.import_module(modname)  # Импортировать по
                                                  # по строковым именам
    listerclass = getattr(modobject, classname)   # Извлечь атрибуты по
                                                  # строковым именам
    tester(listerclass, sept)

if __name__ == '__main__':
    testByNames('listinstance', 'ListInstance', True) # Протестировать все
                                                      # три класса
    testByNames('listinherited', 'ListInherited', True)
    testByNames('listtree', 'ListTree', False)
                
