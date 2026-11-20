from navigator.grid import Grid

class Rover:
    DICT_DIRECTIONS = {
            0: "North",
            1: "East",
            2: "South",
            3: "West"
        }
    
    def __init__(self, grid):
        self._grid = grid
        self._direction = 0
        self._position = list(self._grid.start_coordinates)

    def __str__(self):
        return f"{self._position}, facing {self.DICT_DIRECTIONS[self._direction]}" 

    @property
    def direction(self):
        return self._direction

    @property
    def position(self):
        return tuple(self._position)

    def move(self, commands_list):
        movement_vectors = {
                    0: [0, -1],
                    1: [1, 0],
                    2: [0, 1],
                    3: [-1, 0]
            }
        valid_letters = {"f", "l", "r", "b"}
        coordinates_temp = list(self._position)
        direction_temp = self._direction
        commands_list = commands_list.lower().replace(" ", "")
        for cmnd in commands_list:
                if cmnd not in valid_letters:
                    raise ValueError(f"Unknown command sequence. Only letters 'F', 'B', 'L', 'R' are permitted.")
        for cmnd in commands_list:
            if cmnd == "l":
                direction_temp = (direction_temp-1)%4
            elif cmnd == "r":
                direction_temp = (direction_temp+1)%4
            elif cmnd == "f" or cmnd == "b":
                sign = 1 if cmnd == "f" else -1
                #First, it is verified that the new coordinates wont hit a wall
                if [coordinates_temp[0] + sign*movement_vectors[direction_temp][0], coordinates_temp[1] + sign*movement_vectors[direction_temp][1]] in self._grid.blocked_coordinates:
                    raise ValueError("Rover hit the wall")
                #Second, it is verified that the new X position (which is current X coordinate + the directional vector's X value) is within bounds.
                #Then the directional vector's X value is added to the current X coordinate
                if self.in_bounds_horizontal(coordinates_temp[0] + sign*movement_vectors[direction_temp][0]):
                    coordinates_temp[0] += sign*movement_vectors[direction_temp][0]
                else:
                    raise ValueError("Rover is out of bounds")
                #Third, it is verified that the new Y position (which is current Y coordinate + the directional vector's Y value) is within bounds.
                #Then the directional vector's Y value is added to the current Y coordinate
                if self.in_bounds_vertical(coordinates_temp[1] + sign*movement_vectors[direction_temp][1]):
                    coordinates_temp[1] += sign*movement_vectors[direction_temp][1]
                else:
                    raise ValueError("Rover is out of bounds")
        self._position = coordinates_temp
        self._direction = direction_temp

    def in_bounds_horizontal(self, coordinates):
        return 0 < coordinates <= self._grid.width

    def in_bounds_vertical(self, coordinates):
        return 0 < coordinates <= self._grid.height


    