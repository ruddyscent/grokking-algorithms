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

def quicksort(array: List[C]) -> List[C]:
    """
    Sorts a list using the quicksort algorithm.

    Args:
        array (List[C]): The list to sort.

    Returns:
        List[C]: The sorted list.
    """
    if len(array) < 2:
        return array
    else:
        pivot: C = array[0]
        less: List[C] = [i for i in array[1:] if i <= pivot]
        greater: List[C] = [i for i in array[1:] if i > pivot]
        return quicksort(less) + [pivot] + quicksort(greater)