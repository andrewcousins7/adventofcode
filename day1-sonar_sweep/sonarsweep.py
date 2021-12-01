increaseCount = 0
lastValue = None

with open('data.txt') as data:
    lines = data.readlines()
    for newValue in lines:
        newValue = int(newValue)
        if lastValue is not None:
            if newValue > lastValue:
                increaseCount += 1
        lastValue = newValue

print(increaseCount)