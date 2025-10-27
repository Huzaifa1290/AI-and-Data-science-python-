# Grandparent class
class GrandParent:
    def family_name(self):
        print("Family Name: Khan")

# Parent class inherits GrandParent
class Parent(GrandParent):
    def occupation(self):
        print("Occupation: Engineer")

# Child class inherits Parent
class Child(Parent):
    def hobby(self):
        print("Hobby: Painting")


# Example usage
child1 = Child()
child1.family_name()   # From GrandParent
child1.occupation()    # From Parent
child1.hobby()         # From Child
child2 = Child()
child2.family_name()   # From GrandParent
child2.occupation()    # From Parent
child2.hobby()         # From Child