signal = []
with open('input.txt') as data:
    signal = data.read()


def recursive_duplicate_check(char, string):
    if char in string:
        return False
    if len(string) <= 1:
        return True
    return recursive_duplicate_check(string[0], string[1:])


def is_start_of_packet_marker(marker):
    return recursive_duplicate_check(marker[0], marker[1:])


print("Part 1:")
endOfMarkerIndex = 4
while not is_start_of_packet_marker(signal[endOfMarkerIndex-4:endOfMarkerIndex]):
    endOfMarkerIndex += 1
    if endOfMarkerIndex >= len(signal):
        break

print(endOfMarkerIndex)

print("Part 2:")
endOfMarkerIndex = 14
while not is_start_of_packet_marker(signal[endOfMarkerIndex-14:endOfMarkerIndex]):
    endOfMarkerIndex += 1
    if endOfMarkerIndex >= len(signal):
        break

print(endOfMarkerIndex)
