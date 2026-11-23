from navigator.grid import Grid
from collections import deque

def identify_adjacent(c: list, max_height: int, max_width: int, blockers: tuple):
    temp_adj = []
    temp_coordinates = []
    movement_vectors = {
                    0: [0, -1],
                    1: [1, 0],
                    2: [0, 1],
                    3: [-1, 0]
            }
    for i in [0, 1, 2, 3]:
        if 0 < c[0] + movement_vectors[i][0] <= max_width and 0 < c[1] + movement_vectors[i][1] <= max_height:
            temp_coordinates.append(c[0] + movement_vectors[i][0])
            temp_coordinates.append(c[1] + movement_vectors[i][1])
        else:
            temp_coordinates.clear()     
        if temp_coordinates in blockers:
            temp_coordinates.clear()
        if len(temp_coordinates) == 2:
            temp_adj.append(list(temp_coordinates))
        temp_coordinates.clear()
    return temp_adj
        

def traceback(pointers, first, last):
    target_pointer = first
    sequence = [last]
    current_pointer = last
    for key, value in dict(reversed(pointers.items())).items():
        if current_pointer in value:
            sequence.append(list(key))
            current_pointer = list(key)
            if current_pointer == target_pointer:
                sequence.reverse()
                return sequence


def find_path(grid: Grid):
    first = grid.start_coordinates
    last = grid.target_coordinates
    temp_pointer = []
    pointers = {}
    visited = []
    queue = deque()
    queue.append(first)
    while len(queue) > 0:
        for coordinates in list(queue):
            visited.append(coordinates)
            if coordinates == last:
                trace = traceback(pointers, first, last)
                return trace
            adjacent = identify_adjacent(coordinates, grid.height, grid.width, grid.blocked_coordinates)
            for c in adjacent:
                if c not in visited:
                    temp_pointer.append(c)
                    queue.append(c)
            pointers.update({tuple(coordinates): list(temp_pointer)})
            temp_pointer.clear()
            queue.popleft()
    raise ValueError("No path was found")