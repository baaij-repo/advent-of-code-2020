adventDay = 2
CHAR_KEY = 0
LOWER_INT_KEY = 1
UPPER_INT_KEY = 2
PWD_KEY = 3


def getLinesForDay(day):
    with open(f'day{day}/input.txt') as f:
        lines = f.read().splitlines()
        return lines

def parseLine(line):
    split = line.split(':')
    ruleSplit = split[0].split()
    countRuleSplit = ruleSplit[0].split('-')

    restrictedChar = ruleSplit[1]
    charLowerLimit = int(countRuleSplit[0])
    charUpperLimit = int(countRuleSplit[1])
    password = split[1]

    return [restrictedChar, charLowerLimit, charUpperLimit, password]

def runPaswordRule1():
    validCount = 0
    invalidCount = 0
    for line in getLinesForDay(adventDay):
        inputArray = parseLine(line)
        restCharCount = inputArray[PWD_KEY].count(inputArray[CHAR_KEY])

        if (restCharCount >= inputArray[LOWER_INT_KEY]) and (restCharCount <= inputArray[UPPER_INT_KEY]) :
            validCount += 1
        else :
            invalidCount += 1
    print('Results for Rule 1')
    print("Valid count = %d \nInvalid count = %d" % (validCount, invalidCount))

def runPaswordRule2():
    validCount = 0
    invalidCount = 0
    for line in getLinesForDay(adventDay):
        inputArray = parseLine(line)
        lowerIndex = inputArray[LOWER_INT_KEY]
        upperIndex = inputArray[UPPER_INT_KEY]
        lowerPresenceFlag = inputArray[PWD_KEY][lowerIndex: lowerIndex+1] == inputArray[CHAR_KEY]
        upperPresenceFlag = inputArray[PWD_KEY][upperIndex: upperIndex+1] == inputArray[CHAR_KEY]

        if (lowerPresenceFlag and not upperPresenceFlag) or (upperPresenceFlag and not lowerPresenceFlag):
            validCount += 1
        else :
            invalidCount += 1

    print('Results for Rule 2')
    print("Valid count = %d \nInvalid count = %d" % (validCount, invalidCount))


runPaswordRule1()
runPaswordRule2()