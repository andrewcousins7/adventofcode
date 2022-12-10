signals = []
with open('input.txt') as data:
    for line in data.readlines():
        signals.append(line.strip().split(" "))

print("Part 1:")
cycles = []
register = 1
for signal in signals:
    cycles.append(register)
    if signal[0] == "addx":
        cycles.append(register)
        register += int(signal[1])

print(cycles)

signalStrengthSum = 0
i = 19
while i < len(cycles):
    signalStrengthSum += (i+1) * cycles[i]
    print(i, cycles[i])
    i += 40

print(signalStrengthSum)

print("Part 2:")

for row in range(6):
    output = ""
    for col in range(40):
        cycleIndex = (row * 40) + col
        cycleValue = cycles[cycleIndex]
        spriteStart = cycleValue - 1
        spriteEnd = cycleValue + 1
        if spriteStart <= col <= spriteEnd:
            output += "#"
        else:
            output += "."
        #print(cycleIndex+1, col, cycles[cycleIndex])
        #print(output)
    print(output)
