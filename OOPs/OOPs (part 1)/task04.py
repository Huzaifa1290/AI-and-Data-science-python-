class Employee:
    def __init__(self, name, salary):
        # private attributes
        self.__name = name
        self.__salary = salary

    # Getter for name
    def get_name(self):
        return self.__name

    # Setter for salary (only accepts positive values)
    def set_salary(self, salary):
        if salary > 0:
            self.__salary = salary
            print("Salary updated successfully.")
        else:
            print("Invalid salary! Salary must be positive.")

    # Method to show employee details
    def show_details(self):
        print("Employee Name:", self.__name)
        print("Employee Salary:", self.__salary)


# Example usage
emp1 = Employee("Huzaifa", 50000)
emp1.show_details()
emp1.set_salary(60000)
emp1.show_details()
emp1.set_salary(-1000)  # Invalid salary
