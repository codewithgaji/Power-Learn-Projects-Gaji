# Classes & Methods

# Classes allow us to set up "entities" for our objects
class Car:
    def __init__(self, color, model, year):
        self.color = color # These are instances of the variable
        self.model = model
        self.year = year

car1 = Car('blue', 360, 2015) # Now we can create new objects inheriting from the class object: "Car"
car2 = Car('red', 360, 2009)
print(car1.color)


# Inheritance
class Vehicle:
    def __init__(self, wheels):
        self.wheels = wheels

class Car(Vehicle): # This class is inheriting from "Vehicle" class
    pass

car = Car(4) # Now we use the new class created and inheriting the attrs from Vehicle we can assign it to an object
print(car.wheels)

# Polymorphism: The ability for a class to behave differently depending on it's usage

class Dog:
    def speak(self):
        return "Woof!"

class Cat:
    def speak(self):
        return "Meow!"

for animal in [Dog(), Cat()]:
    print(animal.speak())


# Encapsulation: This is the ability of keeping attrs and methods private

class SecretStash:
    def __init__(self):
        self.__chocolates = 10 # This is a private attr

    def take_chocolate(self):
        if self.__chocolates > 0:
            self.__chocolates -= 1
            print("One chocolate Taken!")

        else:
            print("No chocolates left!")

stash = SecretStash()
stash.take_chocolate()


# WEEKLY ASSIGNMENT
class School:
    def __init__(self, name, studentLevel, Grade):
        self.name = name
        self.studentLevel = studentLevel
        self.Grade = Grade

    def CSC101(self):
        self.Grade = "3"

    def GNS101(self):
        self.Grade = "5"


class Lasu(School):
    pass

lasuStudent1 = Lasu("Gaji Yaqub", "300L", "3")
lasuStudent1.CSC101()
print(lasuStudent1.name)
print(lasuStudent1.Grade)