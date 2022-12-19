import copy
import re
import math


# 0 - Blueprint quality
# 1 - Ore robot cost
# 2 - Clay robot cost
# 3 - Obsidian robot ore cost
# 4 - Obsidian robot clay cost
# 5 - Geode robot ore cost
# 6 - Geode robot obsidian cost
class RobotFactory:
    def __init__(self, inputs):
        self.quality = int(inputs[0])
        self.bots = {
            'ore': {'ore': int(inputs[1])},
            'clay': {'ore': int(inputs[2])},
            'obsidian': {'ore': int(inputs[3]), 'clay': int(inputs[4])},
            'geode': {'ore': int(inputs[5]), 'obsidian': int(inputs[6])}
        }
        self.robot_limits = {
            'ore': max(int(inputs[2]), int(inputs[3]), int(inputs[5])),
            'clay': int(inputs[4]),
            'obsidian': int(inputs[6]),
            'geode': math.inf
        }

    def can_build_robot(self, rb, res):
        for r in self.bots[rb].keys():
            if res[r] < self.bots[rb][r]:
                return False
        return True

    def will_be_able_to_build_robot(self, rb, robots):
        for r in self.bots[rb].keys():
            if robots[r] <= 0:
                return False
        return True

    def has_max_robots(self, rb, robots):
        return robots[rb] >= self.robot_limits[rb]

    def build_robot(self, rb, robots, res):
        for r in self.bots[rb].keys():
            res[r] -= self.bots[rb][r]
        robots[rb] += 1


all_resources = [
    'ore',
    'clay',
    'obsidian',
    'geode'
]

blueprints = []
with open('input.txt') as data:
    for line in data.readlines():
        blueprints.append(RobotFactory(re.findall("[0-9]+", line)))


print("Part 1:")
minutes = 24

starting_robots = {
    'ore': 1,
    'clay': 0,
    'obsidian': 0,
    'geode': 0
}

starting_resources = {
    'ore': 0,
    'clay': 0,
    'obsidian': 0,
    'geode': 0
}

benchmark = []

def build_target_robot(factory, robots, resources, minutes_remaining, target_robot):
    start_building = factory.can_build_robot(target_robot, resources)
    for r in all_resources:
        resources[r] += robots[r]
    minutes_remaining -= 1
    if minutes_remaining <= 0:
        return resources['geode']

    if start_building:
        new_robots = copy.deepcopy(robots)
        new_res = copy.deepcopy(resources)
        new_minutes = copy.deepcopy(minutes_remaining)
        factory.build_robot(target_robot, new_robots, new_res)
        return optimize_for_geodes(factory, new_robots, new_res, new_minutes)
    else:
        return build_target_robot(factory, robots, resources, minutes_remaining, target_robot)


def optimize_for_geodes(factory, robots, resources, minutes_remaining):
    progress = resources['geode'] + (robots['geode'] * minutes_remaining)
    benchmark[minutes_remaining] = max(benchmark[minutes_remaining], progress)
    if progress < benchmark[minutes_remaining] * 3/4:
        return 0
    outcomes = []
    for r in all_resources:
        if factory.will_be_able_to_build_robot(r, robots) and not factory.has_max_robots(r, robots):
            new_robots = copy.deepcopy(robots)
            new_res = copy.deepcopy(resources)
            new_minutes = copy.deepcopy(minutes_remaining)
            outcomes.append(build_target_robot(factory, new_robots, new_res, new_minutes, r))
    return max(outcomes)


# qualitySum = 0
# for blueprint in blueprints:
#     benchmark = [0 for i in range(33)]
#     print(blueprint.bots)
#     print(blueprint.robot_limits)
#     geodes = optimize_for_geodes(blueprint, starting_robots, starting_resources, minutes)
#     print(blueprint.quality, geodes)
#     qualitySum += blueprint.quality * geodes
# print(qualitySum)


qualityProduct = 1
for i in range(3):
    benchmark = [0 for i in range(33)]
    blueprint = blueprints[i]
    geodes = optimize_for_geodes(blueprint, starting_robots, starting_resources, 32)
    print(blueprint.quality, geodes)
    qualityProduct *= geodes
print(qualityProduct)