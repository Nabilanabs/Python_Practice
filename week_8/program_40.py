# Existing classes
class Animal:
    def eat(self):
        print("Eating...")

class Pet:
    def play(self):
        print("Playing...")

# New class inheriting from Animal and Pet
class Dog(Animal, Pet):
    def bark(self):
        print("Barking...")

# Example usage
my_dog = Dog()
my_dog.eat()   # from Animal
my_dog.play()  # from Pet
my_dog.bark()  # from Dog itself
