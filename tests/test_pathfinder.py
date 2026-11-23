from navigator.grid import Grid
from navigator.pathfinder import find_path
import pytest

def test_no_route():
    test_grid = Grid("no_route.txt")
    with pytest.raises(ValueError):
        find_path(test_grid)


def test_ok_maze():
    test_grid = Grid("maze.txt")
    test_path = find_path(test_grid)
    assert test_path == [[2,2],[2,3],[2,4],[2,5],[2,6],[3,6],[4,6],[4,5],[4,4],[4,3],[4,2],[5,2],[6,2],[7,2],[8,2],[9,2],[10,2],[11,2],[12,2],[12,3],[12,4],[12,5],[12,6],[12,7],[12,8],[12,9],[12,10]]

def test_ok_simple():
    test_grid = Grid("simple.txt")
    test_path = find_path(test_grid)
    assert test_path == [[2,2],[3,2],[4,2],[5,2],[6,2],[7,2],[7,3],[7,4],[7,5],[7,6],[7,7],[7,8],[8,8],[9,8],[9,9],[9,10]]

def test_ok_open():
    test_grid = Grid("open.txt")
    test_path = find_path(test_grid)
    assert test_path == [[2,2], [2,3], [2,4], [2,5], [2,6], [3,6], [4,6], [5,6], [6,6], [7,6], [8,6], [9,6]]