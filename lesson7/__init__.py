from abc import abstractmethod, ABC


class Animals:
    def __init__(self, name,age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"Animal: {self.name}"
    def get_Info(self):
        return f"Name: {self.name}, Age: {self.age}"
    @abstractmethod
    def sound(self):
        pass
class Dog(Animals):
    def __init__(self, name, age):
        super().__init__(name,age)
    @staticmethod
    def sound():
        return 'Bark'
    def get_Info(self):
        super().get_Info()
class Cat(Animals, ABC):
    def sound(self):
        pass


if __name__ == '__main__':

    dog = Dog('Dog',2)
    print(dog)
    print(dog.sound())

    dog2 = Dog(name='Dog',age=2)
    print(dog2)


    cat1 = Cat('Cat', 2)
    print(cat1.get_Info())