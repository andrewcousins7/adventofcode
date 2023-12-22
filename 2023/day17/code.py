import math
from queue import PriorityQueue

costs_map = [[int(i) for i in line.strip()] for line in open("input.txt").readlines()]
max_x_index = len(costs_map[0]) - 1
max_y_index = len(costs_map) - 1

# Part 1


# def is_forced_to_turn(direction_history):
#     sequential_count = 0
#     # iterate backward through the direction history
#     for direction in direction_history[::-1]:
#         if direction == direction_history[-1]:
#             sequential_count += 1
#             if sequential_count >= 3:
#                 return True
#         else:
#             break


def get_available_directions(direction_history):
    available_directions = ["left", "right", "up", "down"]
    # iterate backward through the direction history
    if len(direction_history) == 0:
        return available_directions
    direction = direction_history[-1]
    if direction == "left":
        available_directions.remove("right")
    elif direction == "right":
        available_directions.remove("left")
    elif direction == "up":
        available_directions.remove("down")
    elif direction == "down":
        available_directions.remove("up")
    available_directions.remove(direction)
    return available_directions
            

# Returns all three moves turning left, and all three moves turning right
# edge case for when direction history is empty
# The reason is then we've considered all possible moves
# don't have to try moving forward, because we'll have already considered that move
# from the previous turn.
def get_neighbors(node, direction_history):
    x, y = node
    neighbors = []
    available_directions = get_available_directions(direction_history)
    if "left" in available_directions:
        cost = 0
        for i in range(1, 4):
            if x - i < 0:
                break
            directions = direction_history.copy() + ["left"] * i
            cost += costs_map[y][x - i]
            neighbors.append([x - i, y, directions, cost])
    if "right" in available_directions:
        cost = 0
        for i in range(1, 4):
            if x + i > max_x_index:
                break
            directions = direction_history.copy() + ["right"] * i
            cost += costs_map[y][x + i]
            neighbors.append([x + i, y, directions, cost])
    if "up" in available_directions:
        cost = 0
        for i in range(1, 4):
            if y - i < 0:
                break
            directions = direction_history.copy() + ["up"] * i
            cost += costs_map[y - i][x]
            neighbors.append([x, y - i, directions, cost])
    if "down" in available_directions:
        cost = 0
        for i in range(1, 4):
            if y + i > max_y_index:
                break
            directions = direction_history.copy() + ["down"] * i
            cost += costs_map[y + i][x]
            neighbors.append([x, y + i, directions, cost])
    return neighbors


def get_ultra_neighbors(node, direction_history):
    x, y = node
    neighbors = []
    available_directions = get_available_directions(direction_history)
    if "left" in available_directions:
        cost = 0
        for i in range(1, 11):
            if x - i < 0:
                break
            directions = direction_history.copy() + ["left"] * i
            cost += costs_map[y][x - i]
            if i >= 4:
                neighbors.append([x - i, y, directions, cost])
    if "right" in available_directions:
        cost = 0
        for i in range(1, 11):
            if x + i > max_x_index:
                break
            directions = direction_history.copy() + ["right"] * i
            cost += costs_map[y][x + i]
            if i >= 4:
                neighbors.append([x + i, y, directions, cost])
    if "up" in available_directions:
        cost = 0
        for i in range(1, 11):
            if y - i < 0:
                break
            directions = direction_history.copy() + ["up"] * i
            cost += costs_map[y - i][x]
            if i >= 4:
                neighbors.append([x, y - i, directions, cost])
    if "down" in available_directions:
        cost = 0
        for i in range(1, 11):
            if y + i > max_y_index:
                break
            directions = direction_history.copy() + ["down"] * i
            cost += costs_map[y + i][x]
            if i >= 4:
                neighbors.append([x, y + i, directions, cost])
    return neighbors


def heuristic(x1, y1, x2, y2):
    return abs(x1 - x2) + abs(y1 - y2)


def a_star_search(start, goal):
    frontier = PriorityQueue()
    frontier.put([0, 0, start, []])
    cost_so_far = {start: {}}
    while not frontier.empty():
        _, cost, current, direction_history = frontier.get()
        print(current, cost, direction_history)
        if current == goal:
            return cost, direction_history
        # for neighbor in get_neighbors(current, direction_history):
        for neighbor in get_ultra_neighbors(current, direction_history):
            new_x = neighbor[0]
            new_y = neighbor[1]
            new_direction_history = neighbor[2]
            next_node = (new_x, new_y)
            new_cost = cost + neighbor[3]
            new_direction = new_direction_history[-1]
            if next_node not in cost_so_far:
                cost_so_far[next_node] = {}
            if new_direction not in cost_so_far[next_node]:
                cost_so_far[next_node][new_direction] = math.inf
            if new_cost < cost_so_far[next_node][new_direction]:
                cost_so_far[next_node][new_direction] = new_cost
                priority = new_cost + heuristic(new_x, new_y, goal[0], goal[1])
                frontier.put([priority, new_cost, next_node, new_direction_history])
                #  print("putting", next_node, new_cost, new_direction_history)
    return None


print(a_star_search((0, 0), (max_x_index, max_y_index)))
