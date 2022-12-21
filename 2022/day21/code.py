class Monkey:
    def __init__(self, name):
        self.name = name
        self.value = None
        self.part1 = None
        self.part2 = None
        self.operator = None

    def listen(self, m):
        v = int(m.value)
        n = m.name
        if self.part1 == n:
            self.part1 = v
        if self.part2 == n:
            self.part2 = v
        self.try_to_yell()

    def try_to_yell(self):
        if isinstance(self.part1, int) and isinstance(self.part2, int):
            self.value = eval(str(self.part1) + self.operator + str(self.part2))
            self.yell()

    def yell(self):
        if self.name in monkeysToInputs:
            for waiting_monkey in monkeysToInputs[self.name]:
                print("-- Yelling to", waiting_monkey.name)
                waiting_monkey.listen(self)

    def solve_backward(self, output):
        if self.value is not None:
            self.value = output
            return
        solution = 0
        if isinstance(self.part1, int):
            if output is None:
                solution = self.part1
            elif self.operator == "+":
                solution = output - self.part1
            elif self.operator == "-":
                solution = self.part1 - output
            elif self.operator == "/":
                solution = self.part1/output
            elif self.operator == "*":
                solution = output/self.part1
            nameToMonkey[self.part2].solve_backward(solution)
        elif isinstance(self.part2, int):
            if output is None:
                solution = self.part2
            elif self.operator == "+":
                solution = output - self.part2
            elif self.operator == "-":
                solution = output + self.part2
            elif self.operator == "/":
                solution = self.part2 * output
            elif self.operator == "*":
                solution = output/self.part2
            nameToMonkey[self.part1].solve_backward(solution)


monkeys = []
monkeysToInputs = {}
nameToMonkey = {}

def log_monkey(input_monkey, dest_monkey):
    if input_monkey not in monkeysToInputs:
        monkeysToInputs[input_monkey] = []
    monkeysToInputs[input_monkey].append(dest_monkey)


with open('input.txt') as data:
    for value in data.readlines():
        values = value.split(": ")
        monkeyName = values[0]
        monkey = Monkey(monkeyName)
        if len(values[1]) > 4:
            values = values[1].split(" ")
            firstMonkey = values[0]
            operator = values[1]
            secondMonkey = values[2].strip()
            monkey.operator = operator
            monkey.part1 = firstMonkey
            monkey.part2 = secondMonkey
            log_monkey(firstMonkey, monkey)
            log_monkey(secondMonkey, monkey)
        else:
            monkeyNumber = int(values[1])
            monkey.value = monkeyNumber
            monkeys.append(monkey)
        nameToMonkey[monkeyName] = monkey

# print("Part 1:")
# for monkey in monkeys:
#         monkey.yell()

print("Part 2:")
for monkey in monkeys:
    if monkey.name != "humn":
        monkey.yell()

nameToMonkey['root'].solve_backward(None)
print(nameToMonkey['humn'].value)
