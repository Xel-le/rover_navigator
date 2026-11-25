import pytest
from navigator.commands import path_to_commands
from navigator.grid import Grid
from navigator.pathfinder import find_path
from navigator.rover import Rover

def test_simple():
    grid = Grid("simple.txt")
    path = find_path(grid)
    commands = path_to_commands(path)
    rover = Rover(grid)
    assert rover.position == path[0] and rover.position == grid.start_coordinates
    rover.move(commands)
    assert rover.position == path[len(path)-1] and rover.position == grid.target_coordinates
    

def test_maze():
    grid = Grid("maze.txt")
    path = find_path(grid)
    commands = path_to_commands(path)
    rover = Rover(grid)
    assert rover.position == path[0] and rover.position == grid.start_coordinates
    rover.move(commands)
    assert rover.position == path[len(path)-1] and rover.position == grid.target_coordinates
    

def test_adjacent():
    grid = Grid("adjacent.txt")
    path = find_path(grid)
    commands = path_to_commands(path)
    rover = Rover(grid)
    assert rover.position == path[0] and rover.position == grid.start_coordinates
    rover.move(commands)
    assert rover.position == path[len(path)-1] and rover.position == grid.target_coordinates
    

def test_open():
    grid = Grid("open.txt")
    path = find_path(grid)
    commands = path_to_commands(path)
    rover = Rover(grid)
    assert rover.position == path[0] and rover.position == grid.start_coordinates
    rover.move(commands)
    assert rover.position == path[len(path)-1] and rover.position == grid.target_coordinates
    

