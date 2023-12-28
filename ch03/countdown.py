# Example in chater 3

def countdown(i: int):
    """
    Prints the countdown from the given number to 1.

    Args:
        i (int): The starting number for the countdown.

    Returns:
        None
    """
    print(i)
    if i <= 1:
        return
    else:
        countdown(i - 1)