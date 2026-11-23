from navigator.rover import Rover
from navigator.grid import Grid
import pytest

def test_out_of_bounds_horizontal_left():
    with pytest.raises(ValueError):
        test_grid = Grid("test_map_no_walls.txt")
        test_rover = Rover(test_grid)
        test_rover.move("LFF")

def test_out_of_bounds_horizontal_right():
    with pytest.raises(ValueError):
        test_grid = Grid("test_map_no_walls.txt")
        test_rover = Rover(test_grid)
        test_rover.move("RFFFF")

def test_out_of_bounds_vertical_up():
    with pytest.raises(ValueError):
        test_grid = Grid("test_map_no_walls.txt")
        test_rover = Rover(test_grid)
        test_rover.move("FF")

def test_out_of_bounds_vertical_down():
    with pytest.raises(ValueError):
        test_grid = Grid("test_map_no_walls.txt")
        test_rover = Rover(test_grid)
        test_rover.move("BBB")

def test_hit_a_wall():
    with pytest.raises(ValueError):
        test_grid = Grid("simple.txt")
        test_rover = Rover(test_grid)
        test_rover.move("F")

def test_bad_map():
    with pytest.raises(ValueError):
        test_grid = Grid("two_starts.txt")
        test_rover = Rover(test_grid)

def test_normal():
    test_grid = Grid("simple.txt")
    test_rover = Rover(test_grid)
    test_rover.move("RFFFFF")
    test_rover.move("RFFFBBFFFFF")
    test_rover.move("LFF")
    assert test_rover.position == [9, 8]
