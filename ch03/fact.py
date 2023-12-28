def fact(x: int):
    """
    Calculate the factorial of a given number.

    Parameters:
    x (int): The number to calculate the factorial of.

    Returns:
    int: The factorial of the given number.
    """
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)