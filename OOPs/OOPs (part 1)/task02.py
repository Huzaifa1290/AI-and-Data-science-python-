class Student:
    def __init__(self, name, roll_no, marks=0):
        # private attributes
        self.__name = name
        self.__roll_no = roll_no
        self.__marks = marks

    # Setter for marks (only allows 0–100)
    def set_marks(self, marks):
        if 0 <= marks <= 100:
            self.__marks = marks
            print("Marks updated successfully.")
        else:
            print("Invalid marks! Please enter a value between 0 and 100.")

    # Getter for name
    def get_name(self):
        return self.__name

    # Getter for roll number
    def get_roll_no(self):
        return self.__roll_no

    # Getter for marks
    def get_marks(self):
        return self.__marks


# Example usage
student1 = Student("Huzaifa", 101)
student1.set_marks(95)
print("Name:", student1.get_name())
print("Roll No:", student1.get_roll_no())
print("Marks:", student1.get_marks())
