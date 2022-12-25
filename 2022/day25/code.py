input = []
with open('input.txt') as data:
    for line in data.readlines():
        line = line.strip()
        input.append(line)


fivesTotal = [
]
for i in range(100):
    fivesTotal.append(pow(5, i)*2)
    if i > 0:
        fivesTotal[i] += fivesTotal[i-1]
print(fivesTotal)


def digit_to_snafu(d):
    if d < 0:
        if d == -1:
            return "-"
        if d == -2:
            return "="
    return str(d)


def get_next_place(decimal):
    place = 1
    high = fivesTotal[place]
    while decimal > high:
        place += 1
        high = fivesTotal[place]
    return place


def decimal_to_snafu_array(decimal):
    #print("decimal", decimal)
    if -2 <= decimal <= 2:
        return [decimal]
    is_negative = decimal < 0
    abs_decimal = abs(decimal)
    place = get_next_place(abs_decimal)
    #print("place", place)
    minFor2 = fivesTotal[place] - fivesTotal[place-1]*2
    #print("minFor2", minFor2)
    v = 2
    if abs_decimal < minFor2:
        v = 1
    if is_negative:
        v *= -1
    #print("v", v)
    result = [0 for _ in range(place+1)]
    result[place] = v
    remainder = decimal - v * pow(5, place)
    remaining_digits = decimal_to_snafu_array(remainder)
    for i in range(len(remaining_digits)):
        result[i] = remaining_digits[i]
    return result


def snafu_digit(digit):
    if digit is "-":
        return -1
    if digit is "=":
        return -2
    return int(digit)


def decimal_to_snafu(decimal):
    snafu_array = decimal_to_snafu_array(decimal)
    output = ""
    for i in range(len(snafu_array)):
        output += digit_to_snafu(snafu_array[len(snafu_array)-1-i])
    return output


def snafu_to_decimal(snafu):
    decimal = 0
    for i in range(len(snafu)):
        v = snafu[len(snafu) - 1 - i]
        v = snafu_digit(v) * pow(5, i)
        decimal += v
    return decimal


print("Part 1:")
sum = 0
for number in input:
    converted = snafu_to_decimal(number)
    sum += converted

print(sum, decimal_to_snafu(sum))
