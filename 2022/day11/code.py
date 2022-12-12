import copy


class Monkey:
    def __init__(self, starting_items, inspect_function, test_function, true_target_index, false_target_index):
        self.items = [item for item in starting_items]
        self.inspect_function = inspect_function
        self.test_function = test_function
        self.true_target_index = true_target_index
        self.false_target_index = false_target_index

    def inspect_and_throw_next_item(self, monkey_list):
        item = self.items.pop(0)
        item = self.inspect_function(item)
        item = int(item / 3)
        if self.test_function(item):
            monkey_list[self.true_target_index].catch_item(item)
        else:
            monkey_list[self.false_target_index].catch_item(item)

    def inspect_and_throw_next_item_round_2(self, monkey_list, max_item_value):
        item = self.items.pop(0)
        item = self.inspect_function(item)
        item = item % max_item_value
        if self.test_function(item):
            monkey_list[self.true_target_index].catch_item(item)
        else:
            monkey_list[self.false_target_index].catch_item(item)

    def catch_item(self, item):
        self.items.append(item)

    def has_items(self):
        return len(self.items) > 0


test_monkeys = [
    Monkey([79, 98], lambda x:x*19, lambda x:0 == (x % 23), 2, 3),
    Monkey([54, 65, 75, 74], lambda x:x+6, lambda x:0 == (x % 19), 2, 0),
    Monkey([79, 60, 97], lambda x:x*x, lambda x:0 == (x % 13), 1, 3),
    Monkey([74], lambda x:x+3, lambda x:0 == (x % 17), 0, 1)
]

input_monkeys = [
    Monkey([56, 56, 92, 65, 71, 61, 79], lambda x:x*7, lambda x:0 == (x % 3), 3, 7),
    Monkey([61, 85], lambda x:x+5, lambda x:0 == (x % 11), 6, 4),
    Monkey([54, 96, 82, 78, 69], lambda x:x*x, lambda x:0 == (x % 7), 0, 7),
    Monkey([57, 59, 65, 95], lambda x:x+4, lambda x:0 == (x % 2), 5, 1),
    Monkey([62, 67, 80], lambda x:x*17, lambda x:0 == (x % 19), 2, 6),
    Monkey([91], lambda x:x+7, lambda x:0 == (x % 5), 1, 4),
    Monkey([79, 83, 64, 52, 77, 56, 63, 92], lambda x:x+6, lambda x:0 == (x % 17), 2, 0),
    Monkey([50, 97, 76, 96, 80, 56], lambda x:x+3, lambda x:0 == (x % 13), 3, 5)
]

monkeys = copy.deepcopy(input_monkeys)
print("Part 1:")
inspection_counts = [0 for i in range(len(monkeys))]
number_of_rounds = 20
for i in range(number_of_rounds):
    for monkey_index in range(len(monkeys)):
        monkey = monkeys[monkey_index]
        while monkey.has_items():
            monkey.inspect_and_throw_next_item(monkeys)
            inspection_counts[monkey_index] += 1

inspection_counts.sort(reverse=True)
print(inspection_counts[0] * inspection_counts[1])


print("Part 2:")
inspection_counts = [0 for i in range(len(monkeys))]
number_of_rounds = 10000
monkeys = copy.deepcopy(input_monkeys)
lowest_common_multiple = 3 * 11 * 7 * 2 * 19 * 5 * 17 * 13
for i in range(number_of_rounds):
    for monkey_index in range(len(monkeys)):
        monkey = monkeys[monkey_index]
        while monkey.has_items():
            monkey.inspect_and_throw_next_item_round_2(monkeys, lowest_common_multiple)
            inspection_counts[monkey_index] += 1

inspection_counts.sort(reverse=True)
print(inspection_counts[0] * inspection_counts[1])
