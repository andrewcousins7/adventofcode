import copy
import re


class Node:
    def __init__(self, name, flow_rate, tunnels):
        self.name = name
        self.flowRate = int(flow_rate)
        self.tunnels = tunnels
        self.weightedPaths = {}

    def calculate_weighted_paths(self, g):
        weighted_paths = {self.name: 0}
        search_queue = [self.name]
        while len(search_queue) > 0:
            search_start = search_queue.pop(0)
            step_count = weighted_paths[search_start] + 1
            for adjacent_location in g[search_start].tunnels:
                if adjacent_location not in weighted_paths:
                    weighted_paths[adjacent_location] = step_count
                    search_queue.append(adjacent_location)
        paths_to_remove = [self.name]
        for path in weighted_paths.keys():
            if g[path].flowRate == 0:
                paths_to_remove.append(path)
        for path in paths_to_remove:
            if path in weighted_paths:
                weighted_paths.pop(path)
        self.weightedPaths = weighted_paths


graph = {}
with open('input.txt') as data:
    for line in data.readlines():
        identifiers = re.findall("[A-Z][A-Z]", line)
        flowRate = re.findall("rate=(.+);", line)
        identifier = identifiers[0]
        graph[identifier] = Node(identifier, flowRate[0], identifiers[1:])


for key in graph.keys():
    node = graph[key]
    if key == 'AA' or node.flowRate > 0:
        node.calculate_weighted_paths(graph)
        print(key, node.weightedPaths)

print("Part 1:")

mem_solutions = {}


def find_pressure(graph, path, time_remaining):
    path.reverse()
    previous_node = None
    pressure = 0
    for node in path:
        if previous_node:
            timeToOpen = graph[previous_node].weightedPaths[node] + 1
            time_remaining -= timeToOpen
            pressure += time_remaining * graph[node].flowRate
        previous_node = node
    return pressure


def find_best_solution(graph, current_n, time_remaining, opened_valves):
    opened_valves.sort()
    mem_key = str(opened_valves)
    if mem_key in mem_solutions.keys():
        best_path = find_pressure(graph, mem_solutions[mem_key], time_remaining)
    solutions = []
    for node in graph[current_n].weightedPaths:
        if node not in opened_valves:
            timeToOpen = graph[current_n].weightedPaths[node] + 1
            if timeToOpen < time_remaining:
                valves = copy.deepcopy(opened_valves)
                valves.append(node)
                time = copy.deepcopy(time_remaining)
                time -= timeToOpen
                valveOutput = graph[node].flowRate * time
                output, path = find_best_solution(graph, node, time, valves)
                path.append(node)
                solutions.append([valveOutput + output, path])
    best_solution = 0
    best_path = []
    for option in solutions:
        if option[0] > best_solution:
            best_solution = option[0]
            best_path = option[1]
    mem_solutions[mem_key] = best_path
    #print(mem_key)
    return best_solution, best_path


solution, path = find_best_solution(graph, 'AA', 30, [])
print(solution, path)

print("Part 2:")
highScore = 0
# for human_key in mem_solutions.keys():
#     human_path = mem_solutions[human_key]
#     human_score = find_pressure(graph, human_path, 26)
#     for elephant_key in mem_solutions.keys():
#         elephant_path = mem_solutions[elephant_key]
#         if not set(human_path).intersection(set(elephant_path)):
#             print("Checking...", human_path, elephant_path)
#             elephant_score = find_pressure(graph, elephant_path, 26)
#             print(human_score, elephant_score)
#             if human_score + elephant_score > highScore:
#                 highScore = human_score + elephant_score

print(highScore)

solution, path = find_best_solution(graph, 'AA', 26, [])
print(solution, path)
solution, path = find_best_solution(graph, 'AA', 26, path)
print(solution, path)
