from typing import List

def count(in_list: List) -> int:
    """
    Recursively counts the number of elements in a list.

    Args:
        in_list (List): The input list.

    Returns:
        int: The number of elements in the list.
    """
    if len(in_list) == 0:
        return 0
    else:
        return 1 + count(in_list[1:])