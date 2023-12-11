histories = []
for line in open("input.txt", "r"):
    line = line.split(" ")
    line = [int(x) for x in line if x]
    histories.append(line)

# Part 1
def build_steps(values):
    steps = []
    for i in range(1, len(values)):
        steps.append(values[i] - values[i-1])
    return steps

def steps_are_all_zero(steps):
    for step in steps:
        if step != 0:
            return False
    return True

def extrapolate_next_step(steps, previous_steps):
    # print("extrapolating next value for", steps)
    # print("based on,", previous_steps)
    new_value = steps[-1] + previous_steps[-1]
    steps.append(new_value)
    # print("new value is", new_value)
    return steps

extrapolated_sum = 0
for line in histories:
    # print(line)
    current_steps = line.copy()
    steps_list = [current_steps]
    while not steps_are_all_zero(current_steps):
        current_steps = build_steps(current_steps)
        steps_list.append(current_steps)
    # print(steps_list)
    for i in range(len(steps_list) - 1):
        index = len(steps_list) - i - 2
        steps_list[index] = extrapolate_next_step(steps_list[index], steps_list[index + 1])
    # print(steps_list)
    # print(steps_list[0][-1])
    extrapolated_sum += steps_list[0][-1]

print(extrapolated_sum)

def extrapolate_previous_step(steps, previous_steps):
    new_value = steps[0] - previous_steps[0]
    steps.insert(0, new_value)
    return steps

extrapolated_sum = 0
for line in histories:
    current_steps = line.copy()
    steps_list = [current_steps]
    while not steps_are_all_zero(current_steps):
        current_steps = build_steps(current_steps)
        steps_list.append(current_steps)
    for i in range(len(steps_list) - 1):
        index = len(steps_list) - i - 2
        steps_list[index] = extrapolate_previous_step(steps_list[index], steps_list[index + 1])
    extrapolated_sum += steps_list[0][0]

print(extrapolated_sum)