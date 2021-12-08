signals = []
with open('data.txt') as data:
    for line in data.read().splitlines():
        inputSignal, outputSignal = line.split(" | ")
        signals.append({
            "input": [str(a) for a in inputSignal.split(" ")],
            "output": [str(a) for a in outputSignal.split(" ")]
        })


print("Part 1")
uniqueDigits = [2, 3, 4, 7]
uniqueCount = 0
for signal in signals:
    for outputSignal in signal["output"]:
        if len(outputSignal) in uniqueDigits:
            uniqueCount += 1

print(uniqueCount)

print("Part 2")
# a8 - only in 7 and 8
# b6
# c8 - not a
# d7 - only in 4 and 8 and not b
# e4
# f9
# g7 - not d
digits = {"abcefg": 0,"cf":1,"acdeg":2,"acdfg":3,"bcdf":4,"abdfg":5,"abdefg":6,"acf":7,"abcdefg":8,"abcdfg":9}
code8 = "gfedcba"
sum = 0
for signal in signals:
    translater = {a: None for a in code8}
    numberCount = {a: 0 for a in code8}
    one, four, seven, eight = "","","",""
    for unknown in signal["input"]:
        unknown = sorted(unknown)
        for letter in unknown:
            numberCount[letter] += 1
        if len(unknown) == 2:
            one = unknown
        elif len(unknown) == 3:
            seven = unknown
        elif len(unknown) == 4:
            four = unknown
        elif len(unknown) == 7:
            eight = unknown
    for letter in code8:
        count = numberCount[letter]
        if count == 6:
            translater['b'] = letter
        elif count == 4:
            translater['e'] = letter
        elif count == 9:
            translater['f'] = letter
        elif count == 7:
            if letter in four and letter in eight:
                if letter not in one and letter not in seven:
                    translater['d'] = letter

    numberString = ""
    for unknown in signal["output"]:
        if len(unknown) == 2:
            numberString += "1"
        elif len(unknown) == 3:
            numberString += "7"
        elif len(unknown) == 4:
            numberString += "4"
        elif len(unknown) == 7:
            numberString += "8"
        elif len(unknown) == 5:
            if translater['e'] in unknown:
                numberString += "2"
            elif translater['b'] in unknown:
                numberString += "5"
            else:
                numberString += "3"
        else:
            if translater['e'] not in unknown:
                numberString += "9"
            elif translater['d'] in unknown:
                numberString += "6"
            else:
                numberString += "0"

    sum += int(numberString)

print(sum)
