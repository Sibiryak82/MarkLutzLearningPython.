# Файл oops2.py

class MyError(Exception): pass

def oops():
    raise MyError('Spam!')

def doomed():
    try:
        oops()
    except IndexError:
        print('caught an index error!')         # перехвачена ошибка индекса!
    except MyError as data:
        print('caught error:', MyError, data)   # перехвачена ошибка
    else:
        print('no error caught...')             # никакие ошибки
                                                # не перехватывались
if __name__ == '__main__':
    doomed()
