# Файл makedb.py: сохранение объектов Person в базе данных shelve

from person import Person, Manager   # Загрузить наши классы
bob = Person('Bob Smith')            # Создать объекты для сохранения
sue = Person('Sue Jones', job='dev', pay=100000)
tom = Manager('Tom Jones', 50000)

import shelve
db = shelve.open('persondb')         # Имя файла, в котором хранятся объекты
for obj in (bob, sue, tom):          # Использовать атрибут name объекта
                                     # в качестве ключа
    db[obj.name] = obj               # Сохранить объект в shelve по ключу
db.close()                           # Закрыть после внесения изменений
