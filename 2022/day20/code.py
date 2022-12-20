import copy


class Node:
    def __init__(self, value, index):
        self.value = value * 811589153
        self.index = index
        self.prev = None
        self.next = None


def move_node(node):
    distance = node.value % (len(order) - 1)
    if distance > 0:
        node.prev.next = node.next
        node.next.prev = node.prev
        new_prev = node
        for _ in range(distance):
            new_prev = new_prev.next
        node.prev = new_prev
        node.next = new_prev.next
        node.prev.next = node
        node.next.prev = node
    if distance < 0:
        node.prev.next = node.next
        node.next.prev = node.prev
        new_next = node
        for _ in range(abs(distance)):
            new_next = new_next.prev
        node.next = new_next
        node.prev = new_next.prev
        node.prev.next = node
        node.next.prev = node


order = None
with open('input.txt') as data:
    order = [int(value) for value in data.readlines()]


print("Part 1:")

nodes = []
rootNode = None
for index in range(len(order)):
    num = order[index]
    node = Node(num, index)
    nodes.append(node)
    if num == 0:
        rootNode = node
for i in range(len(nodes)):
    nextNodeIndex = i + 1
    if nextNodeIndex >= len(nodes):
        nextNodeIndex = 0
    prevNodeIndex = i - 1
    if prevNodeIndex < 0:
        prevNodeIndex = len(nodes) - 1
    nodes[i].next = nodes[nextNodeIndex]
    nodes[i].prev = nodes[prevNodeIndex]

for i in range(10):
    for node in nodes:
        move_node(node)

start_node = rootNode
coordinates = 0
for i in range(3):
    for j in range(1000):
        start_node = start_node.next
    print(start_node.value)
    coordinates += start_node.value
print(coordinates)
