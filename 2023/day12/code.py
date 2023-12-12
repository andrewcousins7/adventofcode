spring_records = []
for line in open('input.txt'):
    springs, record = line.strip().split(' ')
    record = [int(x) for x in record.split(',')]
    spring_records.append([springs, record])


def is_valid(springs, record):
    record_index = 0
    continguous_broken_springs = 0
    working_spring_required = False
    for spring in springs:
        if spring == '#':
            if record_index >= len(record):
                return False
            if working_spring_required:
                return False
            continguous_broken_springs += 1
            if record[record_index] == continguous_broken_springs:
                record_index += 1
                continguous_broken_springs = 0
                working_spring_required = True
        elif spring == '.':
            if continguous_broken_springs > 0:
                return False
            working_spring_required = False
        else:
            raise Exception('Unknown spring type', spring)
    if record_index != len(record):
        return False
    return True


def brute_force(spring_record):
    springs = spring_record[0]
    record = spring_record[1]
    unknowns = []
    permutations = 0
    for i, spring in enumerate(springs):
        if spring == '?':
            unknowns.append(i)
    for i in range(2**len(unknowns)):
        test_arrangement = [x for x in springs]
        for j, unknown in enumerate(unknowns):
            test_arrangement[unknown] = '#' if i & (1 << j) else '.'
        if is_valid(test_arrangement, record):
            # print(test_arrangement)
            permutations += 1
    return permutations


total = 0
for spring_record in spring_records:
    count = brute_force(spring_record)
    total += count
    # print(spring_record, count)
print(total)
