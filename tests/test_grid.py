import pytest
from navigator.grid import Grid

def test_bad_char():
    with pytest.raises(ValueError):
        test_grid = Grid("bad_char.txt")

def test_empty():
    with pytest.raises(ValueError):
        test_grid = Grid("empty.txt")

def test_no_start():
    with pytest.raises(ValueError):
        test_grid = Grid("no_start.txt")

def test_no_target():
    with pytest.raises(ValueError):
        test_grid = Grid("no_target.txt")

def test_two_starts():
    with pytest.raises(ValueError):
        test_grid = Grid("two_starts.txt")

def test_two_targets():
    with pytest.raises(ValueError):
        test_grid = Grid("two_targets.txt")

def test_uneven():
    with pytest.raises(ValueError):
        test_grid = Grid("uneven.txt")

def test_simple():
    test_grid = Grid("simple.txt")
    test_height = test_grid.height
    assert test_height == 11
    test_width = test_grid.width
    assert test_width == 10
    test_start = test_grid.starting_coordinates
    assert test_start == [2, 2]
    test_target = test_grid.target_coordinates
    assert test_target == [9, 10]