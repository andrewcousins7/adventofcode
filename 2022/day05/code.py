import copy

stacks = []
instructions = []
with open('input.txt') as data:
    readingStacks = True
    for line in data.readlines():
        if readingStacks:
            if line[1] == "1":
                readingStacks = False
            else:
                stackIndex = 0
                while len(line) > ((stackIndex * 4) + 1):
                    boxIndex = (stackIndex * 4) + 1
                    boxCharacter = line[boxIndex]
                    if boxCharacter != " ":
                        while len(stacks) <= (stackIndex + 1):
                            stacks.append([])
                        stacks[stackIndex + 1].append(boxCharacter)
                    stackIndex += 1
        else: # Reading instructions
            if len(line.strip()) > 0:
                instructions.append([int(number) for number in line.split() if number.isdigit()])

for stack in stacks:
    stack.reverse()


print("Part 1:")
finalStacks = copy.deepcopy(stacks)
for instruction in instructions:
    countToMove = instruction[0]
    startingStack = finalStacks[instruction[1]]
    endingStack = finalStacks[instruction[2]]
    for i in range(countToMove):
        endingStack.append(startingStack.pop())

solution = [stack.pop() for stack in finalStacks if len(stack) > 0]
print(''.join(solution))

print("Part 2:")
finalStacks = copy.deepcopy(stacks)
for instruction in instructions:
    countToMove = instruction[0]
    startingStack = finalStacks[instruction[1]]
    endingStack = finalStacks[instruction[2]]

    cratesToMove = []
    for i in range(countToMove):
        cratesToMove.append(startingStack.pop())
    for i in range(len(cratesToMove)):
        endingStack.append(cratesToMove.pop())

solution = [stack.pop() for stack in finalStacks if len(stack) > 0]
print(''.join(solution))

