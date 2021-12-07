crabs = []
with open('data.txt') as data:
    crabs = [int(a) for a in data.read().split(",")]

minPosition = min(pos for pos in crabs)
maxPosition = max(pos for pos in crabs)

fuelCosts = [0 for _ in range(minPosition, maxPosition)]

for pos in crabs:
    for targetPos in range(minPosition, maxPosition):
        fuelCosts[targetPos] += abs(targetPos - pos)

print(min(cost for cost in fuelCosts))