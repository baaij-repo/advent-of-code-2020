def getLinesForDay(day):
    with open(f'day{day}/input.txt') as f:
        lines = f.read().splitlines()
        return lines

def decode(code, isLowerHalf, startRange):
    counter = 0
    stack = []
    stack.append(startRange)

    while len(stack) > 0:
        range = stack.pop()
        fromRow = range[0]
        toRow = range[1]
        midPoint = int(fromRow + ((toRow - fromRow) / 2))

        if isLowerHalf(code[counter]):
            toRow = midPoint
        else:
            fromRow = midPoint + 1
            
        if fromRow == toRow:
            return fromRow
        else:
            counter += 1
            stack.append([fromRow, toRow])

decodeRow = lambda code: decode(code, lambda x: x == 'F', [0, 127])
decodeCol = lambda code: decode(code, lambda x: x == 'L', [0, 7])

def getSeatRowCode(line):
    return line[:7]

def getSeatColCode(line):
    return line[7:]

def computeSeatId(line):
    return ((decodeRow(getSeatRowCode(line)) * 8) 
                + decodeCol(getSeatColCode(line)))

def findHighestSeat():
    maxSeatId = 0
    for line in getLinesForDay(5):
        maxSeatId = max(maxSeatId, computeSeatId(line))
    return maxSeatId

def findMissingSeat():
    sortedSeatList = sorted(map(lambda x: computeSeatId(x), getLinesForDay(5)))
    prevSeat = sortedSeatList[0]
    for seatId in sortedSeatList:
        if (seatId - prevSeat) == 2:
            return seatId - 1
        prevSeat = seatId
        

assert decodeRow('FBFBBFF') == 44
assert decodeRow('FFFBBBF') == 14
assert decodeRow('BBFFBBF') == 102

assert decodeCol('RRR') == 7
assert decodeCol('RLL') == 4

assert 'FBFFFFF' == getSeatRowCode("FBFFFFFLLL")
assert 'LLL' == getSeatColCode("FBFFFFFLLL")

print(f'Highest seat ID is {findHighestSeat()}')
print(f'Santas missing seat is {findMissingSeat()}')