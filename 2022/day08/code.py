trees = []
with open('input.txt') as data:
    trees = [[int(tree) for tree in treeRows.strip()] for treeRows in data.readlines()]

dirs = [
    [-1, 0],
    [1, 0],
    [0, -1],
    [0, 1]
]

print("Part 1:")

visibleTable = [[None for i in range(len(row))] for row in trees]


def is_tree_visible_in_dir(row_i, column_i, dir, height):
    if not ((0 <= row_i < len(trees)) and (0 <= column_i < len(trees[row_i]))):
        return True
    if trees[row_i][column_i] >= height:
        return False
    return is_tree_visible_in_dir(row_i + dir[0], column_i + dir[1], dir, height)


def is_tree_visible(row_i, column_i):
    if not ((0 <= row_i < len(trees)) and (0 <= column_i < len(trees[row_i]))):
        return False
    if visibleTable[row_i][column_i] is None:
        isVisible = False
        for dir in dirs:
            if is_tree_visible_in_dir(row_i + dir[0], column_i + dir[1], dir, trees[row_i][column_i]):
                isVisible = True
                break
        visibleTable[row_i][column_i] = isVisible
    return visibleTable[row_i][columnIndex]


visibleTreeCount = 0
for rowIndex in range(len(trees)):
    treeRow = trees[rowIndex]
    for columnIndex in range(len(treeRow)):
        if is_tree_visible(rowIndex, columnIndex):
            visibleTreeCount += 1
print(visibleTreeCount)


print("Part 2:")

def get_visible_trees_in_dir(row_i, column_i, dir, height):
    if not ((0 <= row_i < len(trees)) and (0 <= column_i < len(trees[row_i]))):
        return 0
    if trees[row_i][column_i] >= height:
        return 1
    return 1 + get_visible_trees_in_dir(row_i + dir[0], column_i + dir[1], dir, height)

maxScenicScore = 0
for rowIndex in range(len(trees)):
    treeRow = trees[rowIndex]
    for columnIndex in range(len(treeRow)):
        scenicScore = 1
        for dir in dirs:
            scenicScore *= get_visible_trees_in_dir(rowIndex + dir[0], columnIndex + dir[1], dir, trees[rowIndex][columnIndex])
        if scenicScore > maxScenicScore:
            maxScenicScore = scenicScore
print(maxScenicScore)


