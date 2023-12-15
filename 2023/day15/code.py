steps = open('input.txt').read().split(',')


def hash_value(current_value, character):
    # get ascii value of character
    ascii_value = ord(character)
    current_value += ascii_value
    current_value *= 17
    current_value %= 256
    return current_value


def hash_string(string):
    # hash the string
    current_value = 0
    for character in string:
        current_value = hash_value(current_value, character)
    return current_value


# # Part 1
# sum = 0
# for step in steps:
#     hash = hash_string(step)
#     sum += hash
#
# print(sum)

# Part 2


def get_label_location(box, label):
    for i in range(len(box)):
        if box[i][0] == label:
            return i
    return -1


hashmap = [[] for i in range(256)]
for step in steps:
    if '-' in step:
        label = step.split('-')[0]
        # Remove this lense
        hash = hash_string(label)
        label_index = get_label_location(hashmap[hash], label)
        if label_index >= 0:
            hashmap[hash].pop(label_index)
    else:
        # split step by = into label and focal_length
        label = step.split('=')[0]
        focal_length = step.split('=')[1]
        # Add this lense
        hash = hash_string(label)
        label_index = get_label_location(hashmap[hash], label)
        if label_index >= 0:
            hashmap[hash][label_index][1] = focal_length
        else:
            hashmap[hash].append([label, focal_length])

focus_power = 0
for i in range(len(hashmap)):
    for j in range(len(hashmap[i])):
        focus_power += int(hashmap[i][j][1]) * (j + 1) * (i + 1)

print(focus_power)
