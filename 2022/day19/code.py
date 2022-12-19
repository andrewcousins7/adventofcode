import copy
import re


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
            'geode': {'clay': int(inputs[3]), 'obsidian': int(inputs[4])}
        }

    def can_build_robot(self, rb, res):
        for r in self.bots[rb].keys():
            if res[r] < self.bots[rb][r]:
                return False
        return True

    def build_robot(self, rb, res):
        for r in self.bots[rb].keys():
            res[r] -= self.bots[rb][r]


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


def optimize_for_geodes(factory, robots, resources, minutes_remaining):
    #print(minutes - minutes_remaining + 1, robots, resources)
    for r in all_resources:
        resources[r] += robots[r]
    minutes_remaining -= 1
    if minutes_remaining == 0:
        return resources['geode']
    outcomes = []
    builtRobotCount = 0
    for r in all_resources:
        new_robots = copy.deepcopy(robots)
        new_res = copy.deepcopy(resources)
        new_minutes = copy.deepcopy(minutes_remaining)
        if factory.can_build_robot(r, new_res):
            builtRobotCount += 1
            factory.build_robot(r, new_res)
            new_robots[r] += 1
            outcomes.append(optimize_for_geodes(factory, new_robots, new_res, new_minutes))
    if builtRobotCount <= 1:
        outcomes.append(optimize_for_geodes(factory, robots, resources, minutes_remaining))
    return max(outcomes)


print(optimize_for_geodes(blueprints[0], starting_robots, starting_resources, minutes))
