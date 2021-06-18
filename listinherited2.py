# listinherited2

def __attrnames(self, indent=' '*4):
    result = 'Unders%s\n%s%%s\nOther%s\n' % ('-'*77, indent, '-'*77)
    unders = []
    for attr in dir(self):                         # dir() экземпляра
        if attr[:2] == '__' and attr[-2:] == '__': # Пропуск внутренних имен
            unders.append(attr)
        else:
            display = str(getattr(self, attr))[:82-(len(indent) + len(attr))]
            result += '%s%s=%s\n' % (indent, attr,display)
    return result % ', '.join(unders)
