data = []
with open('data.txt') as data:
    data = [int(value) for value in data.readlines()]


print("Part 1:")

increaseCount = 0
lastValue = None

for newValue in data:
    newValue = int(newValue)
    if lastValue is not None:
        if newValue > lastValue:
            increaseCount += 1
    lastValue = newValue

print(increaseCount)


print("Part 2:")

maxWindowIndex = len(data) - 2
windows = [0 for value in data]
windowIndex = 0

for newValue in data:
    newValue = int(newValue)
    windows[windowIndex] += newValue
    windows[windowIndex+1] += newValue
    windows[windowIndex+2] += newValue

    windowIndex += 1
    if windowIndex >= maxWindowIndex:
        break

increaseCount = 0
lastValue = None

for newValue in windows:
    if lastValue is not None:
        if newValue > lastValue:
            increaseCount += 1
    lastValue = newValue

print(increaseCount)