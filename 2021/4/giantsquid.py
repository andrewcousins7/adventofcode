data = []
with open('data.txt') as data:
    data = [value for value in data.read().splitlines()]

bingoNumbers = [int(callNumber) for callNumber in data.pop(0).split(",")]

bingoBoards = []
currentBoard = []
for line in data:
    if line == "":
        if len(currentBoard) > 0:
            bingoBoards.append(currentBoard)
            currentBoard = []
    else:
        currentLine = []
        for bingoNumber in line.split(" "):
            if bingoNumber != '':
                currentLine.append(int(bingoNumber))
        currentBoard.append(currentLine)

if len(currentBoard) > 0:
    bingoBoards.append(currentBoard)


def mark_board(boardIndex, calledNumber):
    board = bingoBoards[boardIndex]
    for r in range(len(board)):
        row = board[r]
        for c in range(len(row)):
            checkNumber = row[c]
            if checkNumber == calledNumber:
                bingoBoards[boardIndex][r][c] = "found"
                return


def is_board_won(boardIndex):
    board = bingoBoards[boardIndex]
    for row in board:
        isWon = True
        for answer in row:
            if answer != "found":
                isWon = False
        if isWon:
            return True

    for c in range(len(board[0])):
        isWon = True
        for r in range(len(board)):
            answer = board[r][c]
            if answer != "found":
                isWon = False
        if isWon:
            return True

    return False


def sum_unmarked_numbers(boardIndex):
    sum = 0
    board = bingoBoards[boardIndex]
    for r in range(len(board)):
        row = board[r]
        for c in range(len(row)):
            if board[r][c] != "found":
                sum += board[r][c]
    return sum


def play_bingo():
    for calledNumber in bingoNumbers:
        print(calledNumber)
        boardIndex = 0
        numberOfActiveBoards = len(bingoBoards)
        while boardIndex < numberOfActiveBoards:
            mark_board(boardIndex, calledNumber)
            if is_board_won(boardIndex):
                unmarked_sum = sum_unmarked_numbers(boardIndex)
                print(unmarked_sum, calledNumber, unmarked_sum*calledNumber)
                bingoBoards.pop(boardIndex)
                numberOfActiveBoards -= 1
            else:
                boardIndex += 1


play_bingo()




