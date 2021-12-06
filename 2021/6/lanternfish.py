ages = []
with open('data.txt') as data:
    ages = [int(a) for a in data.read().split(",")]

fishAges = 7
babyFishAges = 2

babyFishGroups = [0 for _ in range(babyFishAges)]
fishGroups = [0 for _ in range(fishAges)]

for fishAge in ages:
    fishGroups[fishAge] += 1

currentDay = 0

numDays = 256
for day in range(numDays):
    newAdultFish = babyFishGroups[0]
    for i in range(1, babyFishAges):
        babyFishGroups[i - 1] = babyFishGroups[i]
    babyFishGroups[babyFishAges - 1] = fishGroups[currentDay]
    fishGroups[currentDay] += newAdultFish
    currentDay += 1
    if currentDay >= fishAges:
        currentDay = 0

print(sum(fish for fish in fishGroups) + sum(babyFish for babyFish in babyFishGroups))
