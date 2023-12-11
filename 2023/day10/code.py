pipes = []
starting_pipe = None
pipe_lookup = {}
pipe_index = 0
for line in open("input.txt"):
    pipe_line = []
    line = line.strip()
    for pipe in line:
        pipe_node = {"index": pipe_index, "pipe": pipe, "visited": False, "connections": [], "distance": "@"}
        pipe_line.append(pipe_node)
        pipe_lookup[pipe_index] = pipe_node
        pipe_index += 1
        if pipe == "S":
            starting_pipe = pipe_node
            pipe_node["distance"] = 0
    pipes.append(pipe_line)


def get_modifiers(pipe_char):
    if pipe_char == "|":
        return [[1, 0], [-1, 0]]
    elif pipe_char == "-":
        return [[0, 1], [0, -1]]
    elif pipe_char == "L":
        return [[0, 1], [-1, 0]]
    elif pipe_char == "J":
        return [[0, -1], [-1, 0]]
    elif pipe_char == "7":
        return [[0, -1], [1, 0]]
    elif pipe_char == "F":
        return [[0, 1], [1, 0]]
    elif pipe_char == "S":
        return [[-1, 0], [0, 1], [1, 0], [0, -1]]
    else:
        return []


def get_connections(pipes, pipe, x, y):
    modifiers = get_modifiers(pipe["pipe"])
    connections = []
    for mod in modifiers:
        try:
            if pipes[x + mod[0]][y + mod[1]]["pipe"] != ".":
                connections.append(pipes[x + mod[0]][y + mod[1]]["index"])
        except IndexError:
            pass
    return connections


# pipes organized as x, y, where x=0 is the top and y=0 is the left
for x in range(len(pipes)):
    for y in range(len(pipes[x])):
        pipe = pipes[x][y]
        pipe["connections"] = get_connections(pipes, pipe, x, y)


def is_shared_connection(pipe, connection_index):
    for index in pipe["connections"]:
        if index == connection_index:
            return True
    return False


for x in range(len(pipes)):
    for y in range(len(pipes[x])):
        pipe = pipes[x][y]
        pipe_index = pipe["index"]
        for connection in pipe["connections"]:
            connecting_pipe = pipe_lookup[connection]
            if not is_shared_connection(connecting_pipe, pipe_index):
                pipe["connections"].remove(connection)


# write a breadth first search
def bfs(graph, start):
    max_distance = 0
    queue = [start]
    while queue:
        node = queue.pop(0)
        if not node["visited"]:
            node["visited"] = True
            distance = node["distance"]
            for index in node["connections"]:
                n = pipe_lookup[index]
                if not n["visited"]:
                    n["distance"] = distance + 1
                    if n["distance"] > max_distance:
                        max_distance = n["distance"]
                    queue.append(n)
    return max_distance


distance = bfs(pipes, starting_pipe)
for line in pipes:
    print("".join([pipe["pipe"] for pipe in line]))
print("###########")
for line in pipes:
    print("".join([str(pipe["distance"]) for pipe in line]))
print("###########")
print(distance)
