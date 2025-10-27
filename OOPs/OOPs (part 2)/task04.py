# Father class
class Father:
    def skills(self):
        return "Scientist"

# Mother class 1
class Mother_01:
    def skills(self):
        return "Freelancer"
    
# Mother class 2
class Mother_02:
    def skills(self):
        return "Teacher"

# Child class inherits from all three
class Child(Father, Mother_01, Mother_02):
    def skills(self):
        father_skill = Father.skills(self)
        mother_01_skill = Mother_01.skills(self)
        mother_02_skill = Mother_02.skills(self)
        return father_skill + ", " + mother_01_skill + " and " + mother_02_skill


# Example usage
child1 = Child()
print("Child Skills:", child1.skills())