class BankAccount:
    def __init__(self, account_number, balance=0):
        # private attributes
        self.__account_number = account_number
        self.__balance = balance

    # Method to deposit money
    def deposit(self, amount):
        if amount > 0:
            self.__balance += amount
            print(f"Deposited: {amount}")
        else:
            print("Invalid deposit amount")

    # Method to withdraw money
    def withdraw(self, amount):
        if 0 < amount <= self.__balance:
            self.__balance -= amount
            print(f"Withdrawn: {amount}")
        else:
            print("Insufficient balance or invalid amount")

    # Method to check balance
    def get_balance(self):
        return self.__balance


# Example usage
acc1 = BankAccount("12345", 1000)
acc1.deposit(500)
acc1.withdraw(200)
print("Current Balance:", acc1.get_balance())
