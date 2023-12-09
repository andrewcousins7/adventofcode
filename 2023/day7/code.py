hands = []
for line in open('input.txt').read().splitlines():
    hands.append(line.split(" "))

value_conversion = {
    '1': 1,  # For rank
    '2': 2,
    '3': 3,
    '4': 4,
    '5': 5,
    '6': 6,
    '7': 7,
    '8': 8,
    '9': 9,
    'T': 10,
    'J': 0,  # for part 2 jokers
    'Q': 12,
    'K': 13,
    'A': 14
}

# Joker rules are for part 2 only
def add_rank_to_hand(hand):
    cards = hand[0]
    uniques = {}
    for card in cards:
        if card not in uniques:
            uniques[card] = 1
        else:
            uniques[card] += 1
    jokers = 0
    if 'J' in uniques:
        jokers = uniques['J']
        del uniques['J']
    counts = list(uniques.values())
    counts.sort(reverse=True)
    if not counts:
        counts = [0]
    counts[0] += jokers
    rank = 0
    if counts[0] == 5:
        rank = 7
    elif counts[0] == 4:
        rank = 6
    elif counts[0] == 3:
        if counts[1] == 2:
            rank = 5
        else:
            rank = 4
    elif counts[0] == 2:
        if counts[1] == 2:
            rank = 3
        else:
            rank = 2
    else:
        rank = 1
    hand[0] = str(rank) + "-" + hand[0]

def compare_values(val1, val2):
    return value_conversion[val1] > value_conversion[val2]

def compare_hands(hand1, hand2):
    for i in range(7):
        val1 = hand1[0][i]
        val2 = hand2[0][i]
        if val1 != "-" and val1 != val2:
            return compare_values(val1, val2)

for hand in hands:
    add_rank_to_hand(hand)

def partition(hands, low, high):
    pivot = hands[high]
    i = low - 1
    for j in range(low, high):
        if compare_hands(hands[j], pivot):
            i += 1
            hands[i], hands[j] = hands[j], hands[i]
    hands[i + 1], hands[high] = hands[high], hands[i + 1]
    return i + 1

# write a quick sort to sort the hands
def quick_sort(hands, low, high):
    if low < high:
        pivot = partition(hands, low, high)
        quick_sort(hands, low, pivot - 1)
        quick_sort(hands, pivot + 1, high)

quick_sort(hands, 0, len(hands) - 1)

hands.reverse()
total_winnings = 0
for i in range(len(hands)):
    value = (i + 1) * int(hands[i][1])
    total_winnings += value

print(total_winnings)
