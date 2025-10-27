# Parent class
class Animal:
    def make_sound(self):
        print("Some generic animal sound.")

# Child class
class Dog(Animal):
    # Overriding parent method
    def make_sound(self):
        print("Bark!")

# Example usage
a1 = Animal()
a1.make_sound()   # Calls parent class method

d1 = Dog()
d1.make_sound()   # Calls child class method (overridden)
d2 = Dog()
d2.make_sound()   # Calls child class method (overridden)