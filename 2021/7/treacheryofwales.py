crabs = []
with open('data.txt') as data:
    crabs = [int(a) for a in data.read().split(",")]

minPosition = min(pos for pos in crabs)
maxPosition = max(pos for pos in crabs)

fuelCosts = [0 for _ in range(minPosition, maxPosition)]

for pos in crabs:
    for targetPos in range(minPosition, maxPosition):
        # Part 1: fuelCosts[targetPos] += abs(targetPos - pos)
        distance = abs(targetPos - pos)
        cost = 0
        for i in range(0, distance):
            cost += (i+1)
        fuelCosts[targetPos] += cost

print(min(cost for cost in fuelCosts))