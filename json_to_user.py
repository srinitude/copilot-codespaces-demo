"""
Module docstring
"""

class User:
    """
    A class representing a user.

    Attributes:
        name (str): The user's name.
        email (str): The user's email.
        password (str): The user's password.
    """
    def __init__(self, name, email, password):
        self.name = name
        self.email = email
        self.password = password

new_user = {
    "name": "John Doe",
    "email": "johndoe@gmail.com",
    "password": "password123"
}

def create_user(json_data):
    """
    Creates a new User object from a JSON object.

    Args:
        json_data (dict): A dictionary containing the user's name, email, and password.

    Returns:
        User: A new User object with the specified name, email, and password.
    """
    name = json_data["name"]
    email = json_data["email"]
    password = json_data["password"]
    return User(name, email, password)

def jsonify_user(user):
    """
    Creates a JSON object from a User object.

    Args:
        user (User): A User object.

    Returns:
        dict: A dictionary containing the user's name, email, and password.
    """
    return {
        "name": user.name,
        "email": user.email,
        "password": user.password
    }
