#多态
import abc
class Animal(metaclass=abc.ABCMeta):
    @abc.abstractmethod
    def talk(self):
        pass

class Cat(Animal):
    def talk(self):
        print("say miaomiao")

class Dog(Animal):
    def talk(self):
        print("say wangwang")

class Pig(Animal):
    def talk(self):
        print("say aoao")

