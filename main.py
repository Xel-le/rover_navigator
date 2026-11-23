from navigator.grid import Grid
from navigator.rover import Rover
from navigator.pathfinder import find_path
from navigator.commands import path_to_commands
import argparse
from sys import exit

def main():
    parser = argparse.ArgumentParser(description="Rover Navigator App")
    parser.add_argument("-m", "--map", help="Provide a name of the map with extension from the /map directory")
    args = parser.parse_args() 
    if args.map == None:
        try:
            grid_name = input("Provide a name of the map with extension from the /map directory: ")
        except EOFError:
            exit("Program was terminated")
    else:
        grid_name = args.map
    grid = Grid(grid_name)
    path = find_path(grid)
    route = path_to_commands(path)
    rover = Rover(grid)
    rover.move(route)
    file_lines = int()
    file_characters = int()
    new_map = str()
    with open("maps/"+grid_name, "r") as file:
        for line in file:
            file_characters = 0
            file_lines += 1
            for c in line:
                file_characters += 1
                if [int(file_characters), int(file_lines)] in path[1:-1]:
                    new_map += f"X"
                else:
                    new_map += f"{c}"
        new_map += f"\n"
    print(new_map)
    


if __name__ == "__main__":
    main()