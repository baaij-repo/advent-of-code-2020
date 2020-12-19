def getLinesForDay(day):
    with open(f'day{day}/input.txt',) as f:
        lines = f.read().splitlines()
        return lines

def parse(line):
    instructionSplit = line.split()
    cmd = instructionSplit[0]
    incr = int(instructionSplit[1])
    return [cmd, incr]

def execute(cmd, incr, pointer, accumulator):
    if cmd == 'acc':
        pointer += 1
        accumulator += incr
    elif cmd == 'jmp':
        pointer += incr
    else:
        pointer += 1
    return [pointer, accumulator]

def solve1():
    instructions = getLinesForDay(8)
    accumulator = 0
    pointer = 0
    pastIds = {}
    while pastIds.get(pointer) == None:
        pastIds[pointer] = ''
        parseResult = parse(instructions[pointer])
        execResult = execute(parseResult[0], parseResult[1], pointer, accumulator)
        pointer = execResult[0]
        accumulator = execResult[1]
        
    print(f'Accumulator value for puzzle 1 = {accumulator}')

solve1()

#############################################

def terminateAndGetResult(instructions):
    isTerminating = True
    pointer = 0
    accumulator = 0
    pastIds = {}
    
    while pointer < len(instructions):
        if pastIds.get(pointer) != None:
            isTerminating = False
            break
        pastIds[pointer] = ''
        parseResult = parse(instructions[pointer])
        execResult = execute(parseResult[0], parseResult[1], pointer, accumulator)
        pointer = execResult[0]
        accumulator = execResult[1]
    return [pointer, accumulator] if isTerminating else None

def flip(instruction):
    flippedValue = None
    if instruction.find('jmp') > -1:
        flippedValue = instruction.replace('jmp', 'nop')
    if instruction.find('nop') > -1:
        flippedValue = instruction.replace('nop', 'jmp')
    return flippedValue

def solve2():
    instructions = getLinesForDay(8)
    for i in range(len(instructions)):
        instruction = instructions[i]
        flippedInstr = flip(instruction)
        if flippedInstr:
            instructions[i] = flippedInstr
            result = terminateAndGetResult(instructions)
            if result != None:
                print(f'Accumulator value for puzzle 2 = {result[1]}')
                break
            instructions[i] = instruction


solve2()