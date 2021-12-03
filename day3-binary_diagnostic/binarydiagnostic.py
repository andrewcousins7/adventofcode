data = []
with open('data.txt') as data:
    data = [[(int(binary) == 1) for binary in value] for value in data.read().splitlines()]

bitSize = len(data[0])

print("Part 1")
bitArray = [0] * bitSize
gamma = 0
epsilon = 0

for line in data:
    for i in range(bitSize):
        if line[i]:
            bitArray[i] += 1
        else:
            bitArray[i] -= 1

for i in range(bitSize):
    decimalValue = pow(2, i)
    arrayIndex = bitSize - 1 - i
    if bitArray[arrayIndex] > 0:
        gamma += decimalValue
    else:
        epsilon += decimalValue

print(gamma, epsilon, gamma*epsilon)
