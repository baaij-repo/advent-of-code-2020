def getLinesForDay(day):
    with open(f'day{day}/input.txt',) as f:
        lines = f.read().splitlines()
        return lines

def solve1():
    instructions = getLinesForDay(8)
    accumulator = 0
    pointer = 0
    pastIds = {}
    while pastIds.get(pointer) == None:
        pastIds[pointer] = ''
        instrSplit = instructions[pointer].split()
        cmd = instrSplit[0]
        incr = int(instrSplit[1])
        if cmd == 'acc':
            pointer += 1
            accumulator += incr
        elif cmd == 'jmp':
            pointer += incr
        else:
            pointer += 1
    print(f'Accumulator value = {accumulator}')

solve1()
