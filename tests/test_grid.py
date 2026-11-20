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

def test_no_file():
    with pytest.raises(FileNotFoundError):
        test_grid = Grid("ghrtervtrsbdtrev")

def test_simple():
    test_grid = Grid("simple.txt")
    test_height = test_grid.height
    assert test_height == 11
    test_width = test_grid.width
    assert test_width == 10
    test_start = test_grid.start_coordinates
    assert test_start == [2, 2]
    test_target = test_grid.target_coordinates
    assert test_target == [9, 10]
    test_blocks = test_grid.blocked_coordinates
    assert test_blocks == ([1, 1], [2, 1], [3, 1], [4, 1], [5, 1], [6, 1], [7, 1], [8, 1], [9, 1], [10, 1], [1, 2], [8, 2], [10, 2], [1, 3], [3, 3], [4, 3], [5, 3], [6, 3], [8, 3], [10, 3], [1, 4], [3, 4], [6, 4], [8, 4], [10, 4], [1, 5], [3, 5], [5, 5], [6, 5], [8, 5], [10, 5], [1, 6], [3, 6], [8, 6], [10, 6], [1, 7], [3, 7], [4, 7], [5, 7], [6, 7], [8, 7], [10, 7], [1, 8], [6, 8], [10, 8], [1, 9], [2, 9], [3, 9], [4, 9], [6, 9], [7, 9], [8, 9], [10, 9], [1, 10], [8, 10], [10, 10], [1, 11], [2, 11], [3, 11], [4, 11], [5, 11], [6, 11], [7, 11], [8, 11], [9, 11], [10, 11])