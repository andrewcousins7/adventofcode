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


def narrow_down_values(values, index, useMoreFrequent):
    validIndex = (useMoreFrequent == is_true_more_frequent(values, index))
    newValues = []
    for value in values:
        if value[index] == validIndex:
            newValues.append(value)
    return newValues


def binary_to_decimal(array):
    value = 0
    for i in range(len(array)):
        decimalValue = pow(2, i)
        arrayIndex = len(array) - 1 - i
        if array[arrayIndex]:
            value += decimalValue
    return value


oxygenValues = data.copy()
index = 0
while len(oxygenValues) > 1:
    oxygenValues = narrow_down_values(oxygenValues, index, True)
    index += 1

oxygen = binary_to_decimal(oxygenValues[0])

co2Values = data.copy()
index = 0
while len(co2Values) > 1:
    co2Values = narrow_down_values(co2Values, index, False)
    index += 1

co2 = binary_to_decimal(co2Values[0])

print(oxygen, co2, oxygen*co2)
