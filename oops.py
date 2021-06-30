# Файл oops.py

def oops():
    raise IndexError()

def doomed():
    try:
        oops()
    except IndexError:
        print('caught an index error!')    # перехвачена ошибка индекса!
    else:
        print('no error caught...')        # никакие ошибки
                                           # не перехватывались
if __name__ == '__main__': doomed()
