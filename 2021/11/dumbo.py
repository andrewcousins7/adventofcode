octopus = []
with open("data.txt") as data:
    octopus = [[int(energy) for energy in line] for line in data.read().splitlines()]

flashes = 0
numSteps = 100
flashesInStep = 0


def octoFlash(row, col):
    global flashes
    global octopus
    global flashesInStep
    octopus[row][col] += 1
    if octopus[row][col] == 10:
        flashes += 1
        flashesInStep += 1
        for r in range(-1, 2):
            for c in range(-1, 2):
                rowMod = row + r
                colMod = col + c
                if 0 <= rowMod < len(octopus) and 0 <= colMod < len(octopus[rowMod]):
                    octoFlash(rowMod, colMod)


for step in range(numSteps):
    flashesInStep = 0
    for row in range(len(octopus)):
        for col in range(len(octopus[row])):
            octoFlash(row, col)
    for row in range(len(octopus)):
        for col in range(len(octopus[row])):
            if octopus[row][col] >= 10:
                octopus[row][col] = 0


print("Part 1")
print(flashes)

print("Part 2")
step = numSteps
while True:
    flashesInStep = 0
    for row in range(len(octopus)):
        for col in range(len(octopus[row])):
            octoFlash(row, col)
    if flashesInStep == 100:
        step += 1
        print(step)
        break
    for row in range(len(octopus)):
        for col in range(len(octopus[row])):
            if octopus[row][col] >= 10:
                octopus[row][col] = 0
    step += 1
