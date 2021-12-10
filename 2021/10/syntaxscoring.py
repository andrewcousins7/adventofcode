lines = []
with open("data.txt") as data:
    lines = [line for line in data.read().splitlines()]

points = {
    ')': 3,
    ']': 57,
    '}': 1197,
    '>': 25137
}

openSyntax = '([{<'

pairedSyntax = {
    '(': ')',
    '[': ']',
    '{': '}',
    '<': '>'
}

autoCompletePoints = {
    ')': 1,
    ']': 2,
    '}': 3,
    '>': 4
}

nonCorruptLineStacks = []

print("Part 1")
errorScore = 0
for line in lines:
    stack = []
    isCorrupt = False
    for character in line:
        if character in openSyntax:
            stack.append(character)
        else:
            previousCharacter = stack.pop()
            if pairedSyntax[previousCharacter] != character:
                errorScore += points[character]
                isCorrupt = True
                break
    if not isCorrupt:
        nonCorruptLineStacks.append(stack)
print(errorScore)

print("Part 2")
autoCompleteScores = []
for stack in nonCorruptLineStacks:
    lineScore = 0
    while len(stack) > 0:
        characterScore = autoCompletePoints[pairedSyntax[stack.pop()]]
        lineScore = (lineScore * 5) + characterScore
    autoCompleteScores.append(lineScore)

autoCompleteScores = sorted(autoCompleteScores)
print(autoCompleteScores[len(autoCompleteScores) // 2])
