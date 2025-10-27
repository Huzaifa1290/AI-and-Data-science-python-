class ShoppingCart:
    def __init__(self):
        # private attribute
        self.__items = []

    # Method to add an item (no duplicates allowed)
    def add_item(self, item):
        if item not in self.__items:
            self.__items.append(item)
            print(f"{item} added to cart.")
        else:
            print(f"{item} is already in the cart.")

    # Method to remove an item
    def remove_item(self, item):
        if item in self.__items:
            self.__items.remove(item)
            print(f"{item} removed from cart.")
        else:
            print(f"{item} not found in cart.")

    # Method to view all items in the cart
    def view_cart(self):
        return self.__items


# Example usage
cart = ShoppingCart()
cart.add_item("Apple")
cart.add_item("Banana")
cart.add_item("Apple")      # Duplicate test
cart.remove_item("Banana")
print("Current Cart:", cart.view_cart())
cart.remove_item("Orange")  # Item not found test
cart.add_item("Orange")
print("Final Cart:", cart.view_cart())