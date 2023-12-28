from typing import List, SupportsComplex

def sum(in_list: List[SupportsComplex]) -> SupportsComplex:
    """
    Calculates the sum of elements in a list.

    Args:
        in_list (List[SupportsComplex]): The input list.

    Returns:
        SupportsComplex: The sum of elements in the list.
    """
    if len(in_list) == 0:
        return 0
    else:
        return in_list[0] + sum(in_list[1:])
