from abc import ABC , abstractmethod

class Animal(ABC):
    @abstractmethod
    def sound(self,name):
        pass
class Dog(Animal):
    def sound(self,name):
        return f"{name} always makes sound as Bow Bow.."

class Cat(Animal):
    def sound(self,name):
        return f"{name} always makes soound as Meow Meow..."
        
obj1 = Dog()
obj2 = Cat()

print(obj1.sound("German shephard"))
print(obj2.sound("Cat"))


class Animal:
    def __init__(self,sound):
        self.sound = sound
        
    def soundMethod(self):
        return f"{self.sound}"
class Dog(Animal):
    def soundMethod(self):
        return f"{self.sound}"
        
class Cat(Dog):
    def soundMethod(self):
        return f"{self.sound}"
        
obj1 = Dog("Bow Bow..")
obj2 = Cat("Meow Meow..")

print(obj1.soundMethod())
print(obj2.soundMethod())
        
