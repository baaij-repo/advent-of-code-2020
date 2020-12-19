
def getLinesForDay(day):
    with open(f'day{day}/input.txt',) as f:
        lines = list(map(lambda x: int(x), f.read().splitlines()))
        return lines

def checkTrailingSum(arr, pos, size):
    subList = arr[pos-size : pos]
    for i in range(len(subList)):
        for j in range(i, len(subList)):
            if subList[i] + subList[j] == arr[pos]:
                return subList
    return False

def solve1():
    preamble = 25
    lines = getLinesForDay(9)
    for x in range(preamble, len(lines)):
        if not checkTrailingSum(lines, x, preamble):
            print(f'First number with exception = {lines[x]}')
            return lines[x]


def findContiguousSet(arr, pos, num):
    result = None
    sum = 0
    for i in range(pos, len(arr)):
        sum += arr[i]
        if sum > num:
            break
        if sum == num:
            result = sorted(arr[pos:i+1])
            break
    return result

def solve2():
    invalidNum = solve1()
    lines = getLinesForDay(9)
    for i in range(len(lines)):
        contSet = findContiguousSet(lines, i, invalidNum)
        if contSet != None:
            print(f'Encryption weakness = {contSet[0] + contSet[len(contSet)-1]}')
            break

solve2()

