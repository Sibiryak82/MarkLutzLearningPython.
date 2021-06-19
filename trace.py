# trace.py

class Wrapper:
    def __init__(self, object):
        self.wrapped = object    # Сохранить объект
    def __getattr__(self, attrname):
        print('Trace: ' + attrname)            # Трассировать извлечение                       
        return getattr(self.wrapped, attrname) # Делегировать извлечение
