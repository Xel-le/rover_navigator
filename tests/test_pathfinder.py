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
    assert len(test_path) == 27
    assert test_path[0] == test_grid.start_coordinates
    assert test_path[len(test_path)-1] == test_grid.target_coordinates

def test_ok_simple():
    test_grid = Grid("simple.txt")
    test_path = find_path(test_grid)
    assert len(test_path) == 16
    assert test_path[0] == test_grid.start_coordinates
    assert test_path[len(test_path)-1] == test_grid.target_coordinates

def test_ok_open():
    test_grid = Grid("open.txt")
    test_path = find_path(test_grid)
    assert len(test_path) == 12
    assert test_path[0] == test_grid.start_coordinates
    assert test_path[len(test_path)-1] == test_grid.target_coordinates