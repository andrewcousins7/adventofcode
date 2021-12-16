transmission = []
with open("data.txt") as data:
    transmission = [str(s) for s in data.read()]


HEX_TO_BINARY = {
    '0': '0000',
    '1': '0001',
    '2': '0010',
    '3': '0011',
    '4': '0100',
    '5': '0101',
    '6': '0110',
    '7': '0111',
    '8': '1000',
    '9': '1001',
    'A': '1010',
    'B': '1011',
    'C': '1100',
    'D': '1101',
    'E': '1110',
    'F': '1111'
}


def hexToBinary(s):
    return HEX_TO_BINARY[s]


def getNextBits(binaryTransmission, numBits):
    next = ''
    for i in range(numBits):
        next += binaryTransmission.pop(0)
    return next


def binaryToBaseTen(binary):
    return int(binary, 2)


def decodeLiteralValue(binaryTransmission):
    signalBit = getNextBits(binaryTransmission, 1)
    valueInBinary = getNextBits(binaryTransmission, 4)
    while signalBit == '1':
        signalBit = getNextBits(binaryTransmission, 1)
        valueInBinary += getNextBits(binaryTransmission, 4)
    return binaryToBaseTen(valueInBinary)


def decodeOperatorPacket(binaryTransmission):
    lengthBit = getNextBits(binaryTransmission, 1)
    subpackets = []
    if lengthBit == '0':
        subpacketLength = binaryToBaseTen(getNextBits(binaryTransmission, 15))
        targetTransmissionLength = len(binaryTransmission) - subpacketLength
        while len(binaryTransmission) > targetTransmissionLength:
            subpackets.append(decodeNextPacket(binaryTransmission))
    elif lengthBit == '1':
        numberOfSubpackets = binaryToBaseTen(getNextBits(binaryTransmission, 11))
        for _ in range(numberOfSubpackets):
            subpackets.append(decodeNextPacket(binaryTransmission))
    return subpackets


def decodeNextPacket(binaryTransmission):
    packetVersion = binaryToBaseTen(getNextBits(binaryTransmission, 3))
    typeID = binaryToBaseTen(getNextBits(binaryTransmission, 3))
    packet = {
        'packetVersion': packetVersion,
        'typeID': typeID
    }
    if typeID == 4:
        literalValue = decodeLiteralValue(binaryTransmission)
        packet['value'] = literalValue
    else:
        subpackets = decodeOperatorPacket(binaryTransmission)
        packet['subpackets'] = subpackets
    return packet

binaryTransmission = []
for s in transmission:
    binary = hexToBinary(s)
    for bit in binary:
        binaryTransmission.append(bit)

rootPacket = decodeNextPacket(binaryTransmission)

print("Part 1: ")
packets = [rootPacket]
versionSum = 0
while len(packets) > 0:
    packet = packets.pop()
    versionSum += packet['packetVersion']
    if 'subpackets' in packet:
        for subpacket in packet['subpackets']:
            packets.append(subpacket)
print(versionSum)

print("Part 2")

def calculatePacket(packet):
    typeID = packet['typeID']
    if typeID == 4:
        return packet['value']
    else:
        subPacketValues = []
        for subpacket in packet['subpackets']:
            subPacketValues.append(calculatePacket(subpacket))
        if typeID == 0:
            return sum(subPacketValues)
        if typeID == 1:
            product = 1
            for v in subPacketValues:
                product = product * v
            return product
        if typeID == 2:
            return min(subPacketValues)
        if typeID == 3:
            return max(subPacketValues)
        if typeID == 5:
            if subPacketValues[0] > subPacketValues[1]:
                return 1
            else:
                return 0
        if typeID == 6:
            if subPacketValues[0] < subPacketValues[1]:
                return 1
            else:
                return 0
        if typeID == 7:
            if subPacketValues[0] == subPacketValues[1]:
                return 1
            else:
                return 0


print(calculatePacket(rootPacket))
