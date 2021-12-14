rules = {}
with open("data.txt") as data:
    for line in data.read().splitlines():
        pair, insertion = line.split(" -> ")
        rules[pair] = insertion

template = "OKSBBKHFBPVNOBKHBPCO"

numSteps = 10
for i in range(numSteps):
    newTemplate = ""
    for char in range(len(template) - 1):
        pair = template[char] + template[char + 1]
        newTemplate += template[char]
        if pair in rules:
            newTemplate += rules[pair]
    newTemplate += template[len(template) - 1]
    template = newTemplate

charCounts = {}
for char in template:
    if char not in charCounts:
        charCounts[char] = 0
    charCounts[char] += 1

print("Part 1")
#print(charCounts)
maxCount = max(charCounts.values())
minCount = min(charCounts.values())
print(maxCount - minCount)


template = "OKSBBKHFBPVNOBKHBPCO"
numSteps = 40

# Save found pair counts after x steps
savedSteps = {}

def findBetweenPairCounts(pair, remainingSteps):
    if remainingSteps == 0:
        return {}
    if pair not in rules:
        return {}
    else:
        # check if we already calculated this
        if pair in savedSteps:
            if str(remainingSteps) in savedSteps[pair]:
                return savedSteps[pair][str(remainingSteps)]

        remainingSteps -= 1
        firstPair = pair[0] + rules[pair]
        secondPair = rules[pair] + pair[1]
        firstPairCounts = findBetweenPairCounts(firstPair, remainingSteps)
        secondPairCounts = findBetweenPairCounts(secondPair, remainingSteps)

        counts = {rules[pair]: 1}
        for char in firstPairCounts.keys():
            count = firstPairCounts[char]
            if char not in counts:
                counts[char] = 0
            counts[char] += count
        for char in secondPairCounts.keys():
            count = secondPairCounts[char]
            if char not in counts:
                counts[char] = 0
            counts[char] += count
        if pair not in savedSteps:
            savedSteps[pair] = {}
        savedSteps[pair][str(remainingSteps+1)] = counts
        return counts

totalCounts = {}
for char in template:
    if char not in totalCounts:
        totalCounts[char] = 0
    totalCounts[char] += 1

for char in range(len(template) - 1):
    pair = template[char] + template[char + 1]
    pairCounts = findBetweenPairCounts(pair, numSteps)
    for char in pairCounts.keys():
        count = pairCounts[char]
        if char not in totalCounts:
            totalCounts[char] = 0
        totalCounts[char] += count

print("Part 2")
#print(totalCounts)
maxCount = max(totalCounts.values())
minCount = min(totalCounts.values())
print(maxCount - minCount)
