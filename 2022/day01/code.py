elvenInventories = []
elfInventory = []
with open('input.txt') as data:
    for value in data.readlines():
        if value == '\n':
            elvenInventories.append(elfInventory)
            elfInventory = []
        else:
            elfInventory.append(int(value))
if len(elfInventory) > 0:
    elvenInventories.append(elfInventory)

calorieCounts = [sum(inventory) for inventory in elvenInventories]
calorieCounts.sort(reverse=True)

print("Part 1:")
print(calorieCounts[0])

print("\nPart 2:")

topCalorieSum = 0
elvesToCount = 3
for i in range(elvesToCount):
    topCalorieSum += calorieCounts[i]
print(topCalorieSum)
