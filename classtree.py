#! pyton

"""classtree.py: подьем по деревьям наследования с применением связей между
пространствами имен и отображением находящихся выше суперклассов с отступом согласно
высоте
"""

def classtree(cls, indent):
    print('.' * indent + cls.__name__)     # Вывести здесь имя класса    
    for supercls in cls.__bases__:         # Вызвать рекурсивно для всех
                                           # суперклассов
            classtree(supercls, indent+3)  # Может посетить суперкласс
                                           # более одного раза
def instancetree(inst):
    print('Tree of %s' % inst)
    classtree(inst.__class__, 3)

def selftest():
    class A: pass
    class B(A): pass
    class C(A): pass
    class D(B, C): pass
    class E: pass
    class F(D, E): pass
    instancetree(B())
    inctancetree(F())
    

if __name__ == '__main__': selftest()
