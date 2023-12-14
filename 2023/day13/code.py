patterns = []
current_pattern = []
for line in open("input.txt").readlines():
    line = line.strip()
    if line == "":
        patterns.append(current_pattern)
        current_pattern = []
    else:
        current_pattern.append(line)
patterns.append(current_pattern)


def check_verticle_reflection(row, starting_index):
    errors = 0
    for i in range(starting_index, len(row)):
        reflected_index = starting_index - (i - starting_index) - 1
        if reflected_index < 0:
            break
        if row[i] != row[reflected_index]:
            errors += 1
        if errors > 2:
            return errors
    return errors


def find_verticle_reflection(pattern):
    for i in range(1, len(pattern[0])):
        errors = 0
        for j in range(0, len(pattern)):
            errors += check_verticle_reflection(pattern[j], i)
            if errors > 1:
                errors = 0
                break
        if errors == 1:
            return i
    return 0


def check_horizontal_reflection(pattern, column_index, starting_index):
    errors = 0
    for i in range(starting_index, len(pattern)):
        reflected_index = starting_index - (i - starting_index) - 1
        if reflected_index < 0:
            break
        if pattern[i][column_index] != pattern[reflected_index][column_index]:
            errors += 1
        if errors > 2:
            return errors
    return errors


def find_horizontal_reflection(pattern):
    for i in range(1, len(pattern)):
        errors = 0
        for j in range(0, len(pattern[0])):
            errors += check_horizontal_reflection(pattern, j, i)
            if errors > 1:
                errors = 0
                break
        if errors == 1:
            return i
    return 0

note_sum = 0
for pattern in patterns:
    note_sum += find_verticle_reflection(pattern)
    note_sum += 100 * find_horizontal_reflection(pattern)

print(note_sum)
