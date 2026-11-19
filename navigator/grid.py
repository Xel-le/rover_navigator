class Grid:
    def __init__(self, path_to_file: str):
        self._path_to_file = None
        self._map_height = None
        self._map_width = None
        self._start_coordinates = None
        self._target_coordinates = None
        self.set_path_to_file = path_to_file

    @property
    def path_to_file(self):
        return self._path_to_file

    @path_to_file.setter
    def set_path_to_file(self, path_to_file):
        allowed_symbols = ["#", ".", "S", "T"]
        start_count = 0
        start_coordinates = []
        target_count = 0
        target_coordinates = []
        map_height = 0
        char_count = 0
        map_width = set()
        with open("maps/" + path_to_file, "r") as file:
            for line in file:
                temp_line = line.rstrip("\n")
                for _ in temp_line:
                    if _ not in allowed_symbols:
                         raise ValueError(f"Grid contains symbols that are not allowed")
                    elif _ == "T": 
                        if target_count + 1 != 1:
                            raise ValueError(f"Grid contains more than one target points")
                        target_coordinates.append(char_count + 1)
                        target_coordinates.append(map_height + 1)
                        target_count += 1
                    elif _ == "S": 
                        if start_count + 1 != 1:
                            raise ValueError(f"Grid contains more than one starting points")
                        start_coordinates.append(char_count + 1)
                        start_coordinates.append(map_height + 1)
                        start_count += 1
                    char_count += 1
                map_width.add(char_count)
                char_count = 0
                map_height += 1
        if len(map_width) != 1:
            raise ValueError(f"Grid has uneven width")
        if start_count == 0:
            raise ValueError(f"Grid has no starting point")
        if target_count == 0:
            raise ValueError(f"Grid has no target point")
        self._path_to_file = "maps/" + path_to_file
        self._map_height = map_height
        self._map_width = int("".join(map(str, map_width)))
        self._start_coordinates = start_coordinates
        self._target_coordinates = target_coordinates

    @property
    def height(self) -> int:
        return self._map_height

    @property
    def width(self) -> int:
        return self._map_width
    @property
    def starting_coordinates(self) -> list:
        return self._start_coordinates
    @property
    def target_coordinates(self) -> list:
        return self._target_coordinates