crabs = []
with open('data.txt') as data:
    crabs = [int(a) for a in data.read().split(",")]

minPosition = min(pos for pos in crabs)
maxPosition = max(pos for pos in crabs)

fuelCosts1 = [0 for _ in range(minPosition, maxPosition)]
fuelCosts2 = [0 for _ in range(minPosition, maxPosition)]

for pos in crabs:
    for targetPos in range(minPosition, maxPosition):
        distance = abs(targetPos - pos)
        fuelCosts1[targetPos] += distance
        fuelCosts2[targetPos] += distance * (distance + 1) // 2

print("Part 1:")
print(min(cost for cost in fuelCosts1))
print("Part 2:")
print(min(cost for cost in fuelCosts2))
