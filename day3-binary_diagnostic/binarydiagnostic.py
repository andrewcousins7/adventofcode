data = []
with open('data.txt') as data:
    data = [[(int(binary) == 1) for binary in value] for value in data.read().splitlines()]

bitSize = len(data[0])


def is_true_more_frequent(array, index):
    runningTotal = 0
    for values in array:
        if values[index]:
            runningTotal += 1
        else:
            runningTotal -= 1
    return runningTotal >= 0


print("Part 1")
bitArray = [0] * bitSize
gamma = 0
epsilon = 0

for i in range(bitSize):
    decimalValue = pow(2, i)
    arrayIndex = bitSize - 1 - i
    if is_true_more_frequent(data, arrayIndex):
        gamma += decimalValue
    else:
        epsilon += decimalValue

print(gamma, epsilon, gamma*epsilon)


print("Part 2")
