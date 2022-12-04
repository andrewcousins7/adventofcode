rucksacks = []
with open('input.txt') as data:
    rucksacks = [value.strip() for value in data.readlines()]


print("Part 1:")

totalPriority = 0
for items in rucksacks:
    halfItemCount = int(len(items) / 2)
    compartmentOne = items[:halfItemCount]
    compartmentTwo = items[halfItemCount:]

    for item in compartmentOne:
        if item in compartmentTwo:
            priority = 0
            if item.isupper():
                priority = ord(item) - 38
            else:
                priority = ord(item) - 96
            totalPriority += priority
            break

print(totalPriority)

print("Part 2:")
totalPriority = 0
pointer = 0
while pointer < len(rucksacks):
    for item in rucksacks[pointer]:
        if item in rucksacks[pointer+1]:
            if item in rucksacks[pointer+2]:
                priority = 0
                if item.isupper():
                    priority = ord(item) - 38
                else:
                    priority = ord(item) - 96
                totalPriority += priority
                break
    pointer += 3

print(totalPriority)
