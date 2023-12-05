# Read in input.txt line by line
lines = []
with open("input.txt", "r") as f:
    for line in f:
        lines.append(line.strip())

# Part 1
# Read each card into two tables
cards = []
for line in lines:
    # Split each line by a : and |
    line = line.split(":")
    card_name = line[0]
    line = line[1].split("|")
    winning_numbers = line[0].split(" ")
    winning_numbers = [x for x in winning_numbers if x]
    numbers = line[1].split(" ")
    numbers = [x for x in numbers if x]
    cards.append([card_name, winning_numbers, numbers])

total = 0
for card in cards:
    card_name = card[0]
    winning_numbers = card[1]
    numbers = card[2]

    points = 0
    for number in numbers:
        if number in winning_numbers:
            if points > 0:
                points *= 2
            else:
                points = 1
    print(card_name, points)
    total += points

print(total)

# Part 2
match_count = []
for card in cards:
    card_name = card[0]
    winning_numbers = card[1]
    numbers = card[2]

    matches = 0
    for number in numbers:
        if number in winning_numbers:
            matches += 1
    match_count.append(matches)
    print(card_name, matches)

copies = [0 for i in range(len(match_count))]
for i in range(len(match_count)):
    copies[i] += 1
    for j in range(copies[i]):
        for k in range(match_count[i]):
            if i + k + 1 < len(copies):
                copies[i + k + 1] += 1
    print(i, copies[i])

print(sum(copies))
