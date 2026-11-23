def path_to_commands(path: list) -> str:
    movement_vectors = {
        0: [0, -1],
        1: [1, 0],
        2: [0, 1],
        3: [-1, 0]
        }
    command_list = ""
    direction = int()
    for n in range(len(path)-1):
        if direction == 0:
            if path[n][0] + movement_vectors[0][0] == path[n+1][0] and path[n][1] + movement_vectors[0][1] == path[n+1][1]:
                command_list += "F"
            elif path[n][0] + movement_vectors[1][0] == path[n+1][0] and path[n][1] + movement_vectors[1][1] == path[n+1][1]:
                command_list += "RF"
                direction = 1
            elif path[n][0] + movement_vectors[2][0] == path[n+1][0] and path[n][1] + movement_vectors[2][1] == path[n+1][1]:
                command_list += "RRF"
                direction = 2
            elif path[n][0] + movement_vectors[3][0] == path[n+1][0] and path[n][1] + movement_vectors[3][1] == path[n+1][1]:
                command_list += "LF"
                direction = 3
            else:
                raise ValueError("Unknown movement direction")
        elif direction == 1:
            if path[n][0] + movement_vectors[0][0] == path[n+1][0] and path[n][1] + movement_vectors[0][1] == path[n+1][1]:
                command_list += "LF"
                direction = 0
            elif path[n][0] + movement_vectors[1][0] == path[n+1][0] and path[n][1] + movement_vectors[1][1] == path[n+1][1]:
                command_list += "F"
            elif path[n][0] + movement_vectors[2][0] == path[n+1][0] and path[n][1] + movement_vectors[2][1] == path[n+1][1]:
                command_list += "RF"
                direction = 2
            elif path[n][0] + movement_vectors[3][0] == path[n+1][0] and path[n][1] + movement_vectors[3][1] == path[n+1][1]:
                command_list += "RRF"
                direction = 3
            else:
                raise ValueError("Unknown movement direction")
        elif direction == 2:
            if path[n][0] + movement_vectors[0][0] == path[n+1][0] and path[n][1] + movement_vectors[0][1] == path[n+1][1]:
                command_list += "LLF"
                direction = 0
            elif path[n][0] + movement_vectors[1][0] == path[n+1][0] and path[n][1] + movement_vectors[1][1] == path[n+1][1]:
                command_list += "LF"
                direction = 1
            elif path[n][0] + movement_vectors[2][0] == path[n+1][0] and path[n][1] + movement_vectors[2][1] == path[n+1][1]:
                command_list += "F"
            elif path[n][0] + movement_vectors[3][0] == path[n+1][0] and path[n][1] + movement_vectors[3][1] == path[n+1][1]:
                command_list += "RF"
                direction = 3
            else:
                raise ValueError("Unknown movement direction")
        elif direction == 3:
            if path[n][0] + movement_vectors[0][0] == path[n+1][0] and path[n][1] + movement_vectors[0][1] == path[n+1][1]:
                command_list += "RF"
                direction = 0
            elif path[n][0] + movement_vectors[1][0] == path[n+1][0] and path[n][1] + movement_vectors[1][1] == path[n+1][1]:
                command_list += "LLF"
                direction = 1
            elif path[n][0] + movement_vectors[2][0] == path[n+1][0] and path[n][1] + movement_vectors[2][1] == path[n+1][1]:
                command_list += "LF"
                direction = 2
            elif path[n][0] + movement_vectors[3][0] == path[n+1][0] and path[n][1] + movement_vectors[3][1] == path[n+1][1]:
                command_list += "F"
            else:
                raise ValueError("Unknown movement direction")
        else:
            raise ValueError("Unknown movement direction")
    return command_list