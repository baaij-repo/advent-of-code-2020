def getLinesForDay(day):
    with open(f'day{day}/input.txt',) as f:
        lines = f.read().splitlines()
        lines.append("") # Adding empty line to get last group's answers
        return lines

def solvePuzzle(filter):
    EMPTY = {'Empty'}
    total = 0
    uniqueAnswers = EMPTY
    for line in getLinesForDay(6):
        # print(f'Pax response - {line}')
        if len(line) > 0:
            answers = set(list(line))
            if uniqueAnswers != EMPTY:
                filter(uniqueAnswers, answers)
            else:
                uniqueAnswers = answers
        else:
            # print(f'Unique set {uniqueAnswers}\n')
            total += len(uniqueAnswers)
            uniqueAnswers = EMPTY
    return total

print(f'Total answers where any pax said yes - {solvePuzzle(lambda x, y: x.update(y))}')
print(f'Total answers where all pax said yes - {solvePuzzle(lambda x, y: x.intersection_update(y))}')