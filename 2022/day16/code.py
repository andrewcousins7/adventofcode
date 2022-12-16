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


def find_best_solution(graph, current_n, time_remaining, opened_valves):
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
    return best_solution, best_path


solution, path = find_best_solution(graph, 'AA', 30, [])
path.reverse()
print(solution, path)

print("Part 2:")


def find_best_solution_for_two(graph, current_n1_info, current_n2_info, time_remaining, opened_valves):
    solutions = [0]
    n1_target = copy.deepcopy(current_n1_info[0])
    n1_time_to_target = copy.deepcopy(current_n1_info[1])
    n2_target = copy.deepcopy(current_n2_info[0])
    n2_time_to_target = copy.deepcopy(current_n2_info[1])

    if n1_time_to_target > 0 and n2_time_to_target > 0:
        time_passing = min(n1_time_to_target, n2_time_to_target)
        time_remaining -= time_passing
        n1_time_to_target -= time_passing
        n2_time_to_target -= time_passing

    if n1_time_to_target == 0:
        for node in graph[n1_target].weightedPaths:
            if node not in opened_valves:
                timeToOpen = graph[n1_target].weightedPaths[node] + 1
                if timeToOpen < time_remaining:
                    valves = copy.deepcopy(opened_valves)
                    valves.append(node)
                    time = copy.deepcopy(time_remaining)
                    valveOutput = graph[node].flowRate * (time - timeToOpen)
                    output = find_best_solution_for_two(graph, [node, timeToOpen], [n2_target, n2_time_to_target], time, valves)
                    solutions.append(valveOutput + output)

    if n2_time_to_target == 0:
        for node in graph[n2_target].weightedPaths:
            if node not in opened_valves:
                timeToOpen = graph[n2_target].weightedPaths[node] + 1
                if timeToOpen < time_remaining:
                    valves = copy.deepcopy(opened_valves)
                    valves.append(node)
                    time = copy.deepcopy(time_remaining)
                    valveOutput = graph[node].flowRate * (time - timeToOpen)
                    output = find_best_solution_for_two(graph, [n1_target, n1_time_to_target], [node, timeToOpen], time,
                                                        valves)
                    solutions.append(valveOutput + output)

    return max(solutions)


solution = find_best_solution_for_two(graph, ['AA', 0], ['AA', 0], 26, [])
print(solution)
