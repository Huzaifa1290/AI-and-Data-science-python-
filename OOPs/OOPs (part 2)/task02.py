# Parent class
class Vehicle:
    def __init__(self, brand, model):
        self.brand = brand
        self.model = model

    def show_details(self):
        print("Brand:", self.brand)
        print("Model:", self.model)


# Child class
class Car(Vehicle):
    def __init__(self, brand, model, seats):
        # Call parent class constructor
        super().__init__(brand, model)
        self.seats = seats

    def show_details(self):
        # Call parent method to display brand and model
        super().show_details()
        print("Seats:", self.seats)


# Example usage
car1 = Car("Toyota", "Corolla", 5)
car1.show_details()
car2 = Car("Honda", "Civic", 4)
car2.show_details()
car3 = Car("Ford", "Mustang", 2)
car3.show_details() 
car4 = Car("Chevrolet", "Camaro", 4)
car4.show_details()
car5 = Car("BMW", "3 Series", 5)
car5.show_details()