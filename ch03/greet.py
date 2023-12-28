# Examples in chapter 3

def greet(name: str):
    """
    Greets a person by printing a message with their name.

    Parameters:
    name (str): The name of the person to greet.
    """
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name: str):
    """
    Greets the given name.

    Args:
        name (str): The name to greet.

    Returns:
        None
    """
    print("how are you, " + name + "?")

def bye():
    """
    Prints a farewell message.
    """
    print("ok bye!")
    