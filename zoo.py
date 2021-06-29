# Файл zoo.py

class Animal:
    def reply(self): self.speak()           # Обратно в подкласс
    def speak(self): print('spam')          # Специальное сообщение

class Mammal(Animal):
    def speak(self): print('huh?')

class Cat(Mammal):
    def speak(self): print('meow')

class Dog(Mammal):
    def speak(self): print('bark')

class Primate(Mammal):
    def speak(self): print('Hello world!')

class Hacker(Primate): pass                 # Унаследован от Primate
