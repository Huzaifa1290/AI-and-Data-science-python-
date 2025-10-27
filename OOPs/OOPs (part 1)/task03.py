class PasswordManager:
    def __init__(self, username, password):
        # public attribute
        self.username = username
        # private attribute
        self.__password = password

    # Method to update password (only if old matches)
    def set_password(self, old, new):
        if self.__password == old:
            self.__password = new
            print("Password updated successfully.")
        else:
            print("Old password is incorrect. Password not changed.")

    # Private method to check username
    def __check_username(self, name):
        return self.username == name

    # Private method to check password
    def __check_password(self, input_password):
        return self.__password == input_password

    # Public method to verify login
    def login(self, name, input_password):
        if self.__check_username(name) and self.__check_password(input_password):
            print("Login successful.")
        else:
            print("Login failed. Invalid username or password.")
            

# Example usage
user1 = PasswordManager("Huzaifa", "abc123")

user1.login("Huzaifa", "abc123")   # Correct credentials
user1.set_password("abc123", "newpass")
user1.login("Huzaifa", "newpass")  # After password change
user1.login("Huzaifa", "wrong")    # Wrong password
