# Classes are used to define types which have their own methods and attributes

class Vehicle:
    def move(self):
        print("Moving...")

    def park(self):
        print("Parking...")

    def start(self):
        print("Starting engine...")


urvan = Vehicle()

urvan.move()
urvan.park()
urvan.start()

print("* " * 25)


# Using constructors
# Constructors are defined and initialized with "__init__(self):"

class Human:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def eat(self):
        print("Eating...")

    def sleep(self):
        print("Sleeping...")

    def walk(self):
        print("Walking...")

    def introduce(self):
        print(f"Hello! My name is {self.name} and I am {self.age} years old.")


man = Human("Jones", 45)
woman = Human("Jane", 52)

man.introduce()
woman.introduce()
