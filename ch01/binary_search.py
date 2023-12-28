from abc import ABCMeta, abstractmethod
from typing import Any, TypeVar, List

class Comparable(metaclass=ABCMeta):
    """
    An abstract base class for objects that can be compared.
    Subclasses must implement the `__lt__` method to define the comparison behavior.
    """
    @abstractmethod
    def __lt__(self, other: Any) -> bool: ...

C = TypeVar('C', bound=Comparable)

def binary_search(arr: List[C], item: C) -> int:
    """
    Perform binary search on a sorted list to find the index of the given item.

    Args:
        arr (List[C]): The sorted list to search in.
        item (C): The item to search for.

    Returns:
        int: The index of the item in the list, or None if the item is not found.
    """
    low: int = 0
    high: int = len(arr) - 1
    
    while low <= high:
        mid: int = (low + high) // 2 
        guess: C = arr[mid]
        if guess == item:
            return mid
        elif guess > item:
            high = mid - 1
        else:
            low = mid + 1

    return None