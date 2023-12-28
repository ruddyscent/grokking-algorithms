from typing import List

def maximum(in_list: List[int | float]) -> int | float:
    """
    Returns the maximum value in a given list.

    Args:
        in_list (List[int | float]): The input list.

    Returns:
        int | float: The maximum value in the list.
    """
    if len(in_list) == 0:
        return None
    elif len(in_list) == 1:
        return in_list[0]
    else:
        return max(in_list[0], maximum(in_list[1:]))
