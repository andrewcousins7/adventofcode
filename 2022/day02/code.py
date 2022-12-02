strategyGuide = []
with open('input.txt') as file:
    strategyGuide = [[str(a).strip() for a in value.split(" ")] for value in file.readlines()]

print("Part 1:")

# A - Rock
# B - Paper
# C - Scissors
outcomes = {
    "A": {"A": 3, "B": 6, "C": 0},
    "B": {"A": 0, "B": 3, "C": 6},
    "C": {"A": 6, "B": 0, "C": 3}
}

thrownOptionScore = {
    "A": 1,
    "B": 2,
    "C": 3
}

thrownOptionConversion = {
    "X": "A",
    "Y": "B",
    "Z": "C"
}

totalScore = 0
for matchup in strategyGuide:
    opponentThrow = matchup[0]
    myThrow = thrownOptionConversion[matchup[1]]
    score = outcomes[opponentThrow][myThrow]
    score += thrownOptionScore[myThrow]
    totalScore += score
print(totalScore)

print("\nPart 2:")

thrownOptionConversion = {
    "A": {"X": "C", "Y": "A", "Z": "B"},
    "B": {"X": "A", "Y": "B", "Z": "C"},
    "C": {"X": "B", "Y": "C", "Z": "A"}
}

totalScore = 0
for matchup in strategyGuide:
    opponentThrow = matchup[0]
    myThrow = thrownOptionConversion[opponentThrow][matchup[1]]
    score = outcomes[opponentThrow][myThrow]
    score += thrownOptionScore[myThrow]
    totalScore += score
print(totalScore)
