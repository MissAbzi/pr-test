class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__ (self):
        return (f"{self.name} is {self.age} years old."
                f"")
    def speak(self, sound):
        return f"{self.name} says {sound}"
Ophelia = Animal("Ophelia", 67)
print(Ophelia)

class Dog(Animal):
    def speak(self, sound = "Woof"):
        return super() .speak(sound)

class Duck(Animal):
    def speak(self, sound = "Quack"):
        return super() .speak(sound)

class Pig(Animal):
    def speak(selfself, sound = "Oink"):
        return super() .speak(sound)

bob = Dog("Bob", 5)
print(bob)
print(bob.speak())

class Cat(Animal):
    def speak(self, sound = "Meow"):
        return super() .speak(sound)

winston = Dog("Winston", 12)
loki = Dog("Loki", 4)
delilah = Cat("Delilah", 2)
howard = Duck("Howard", 52)
babe = Pig("Babe", 30)

menagerie = [winston, loki, delilah, howard, babe]
for creature in menagerie:
    print(creature)
    print(creature.speak())

menagerie2 = [1, winston, 2, loki, delilah, "hello world", howard, babe]
for creature in menagerie2:
  if isinstance(creature, Animal):
    print(creature)
    print(creature.speak())

