# read input.txt into a list of strings
with open("input.txt", "r") as f:
    lines = f.readlines()

def number_to_words(number):
    number_mapping = {
        1: "one",
        2: "two",
        3: "three",
        4: "four",
        5: "five",
        6: "six",
        7: "seven",
        8: "eight",
        9: "nine"
    }

    return number_mapping.get(number, "Invalid number")

# write a function to convert a line of text into an array of numbers
def convert_line(line, reverseStrings):
    numberLine = []
    buffer = ""
    for char in line:
        if char.isdigit():
            numberLine.append(int(char))
        else:
            buffer += char
            for i in range(1, 10):
                numberString = number_to_words(i)
                if reverseStrings:
                    numberString = numberString[::-1]
                if numberString in buffer:
                    numberLine.append(i)
                    buffer = ""
    return numberLine

# write a function to find the first digit in a line of text
def find_first_digit(line):
    numbers = convert_line(line, False)
    return numbers[0]

def find_last_digit(line):
    line = reversed(line)
    numbers = convert_line(line, True)
    return numbers[0]

sum = 0
# for each line of text in lines
for line in lines:
    # find the first digit and convert to int
    first_digit = find_first_digit(line)
    # find the last digit
    last_digit = find_last_digit(line)
    print(first_digit, last_digit)

    val = first_digit * 10 + last_digit
    # add val to sum
    sum += val
print(sum)
