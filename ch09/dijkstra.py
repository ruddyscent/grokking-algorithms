import math
from typing import Set, Dict

graph: Dict[str, Dict[str, int]] = {}
graph["a"] = {}
graph["a"]["fin"] = 1
graph["b"] = {}
graph["b"]["a"] = 3
graph["b"]["fin"] = 5
graph["fin"] = {}

infinity: int = math.inf 
costs: Dict[str, int] = {}
costs["a"] = 6
costs["b"] = 2
costs["fin"] = infinity

parents: Dict[str, str] = {}
parents["a"] = "start"
parents["b"] = "start"
parents["fin"] = None

processed: Set[str] = set()

def find_lowest_cost_node(costs: Dict[str, int]) -> str:
    """
    Find the node with the lowest cost in the given costs dictionary.

    Args:
        costs (Dict[str, int]): A dictionary containing the costs of each node.

    Returns:
        str: The node with the lowest cost.
    """
    lowest_cost: int = float("inf")
    lowest_cost_node: str = None
    for node in costs:
        cost: int = costs[node]
        if cost < lowest_cost and node not in processed:
            lowest_cost = cost
            lowest_cost_node = node
    return lowest_cost_node

node: str = find_lowest_cost_node(costs)

while node is not None:
    cost: int = costs[node]
    neighbors: Dict[str, int] = graph[node]
    for n in neighbors.keys():
        new_cost: int = cost + neighbors[n]
        if costs[n] > new_cost:
            costs[n] = new_cost
            parents[n] = node
    processed.add(node)
    node = find_lowest_cost_node(costs)
