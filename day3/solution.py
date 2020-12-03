def getLinesForDay(day):
    with open(f'day{day}/input.txt') as f:
        lines = f.read().splitlines()
        return lines


class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def moveX(self, incr):
        self.x += incr

    def moveY(self, incr):
        self.y += incr

    def print(self):
        print("Point[%s, %s]" % (self.x, self.y))


class Matrix:
    def __init__(self):
        self.lines = getLinesForDay(3)
        self.rows = len(self.lines)
        self.cols = len(self.lines[0])
        self.position = Point(0, 0)

    def move(self, xIncr, yIncr):
        remainingSteps = self.cols - (self.position.x + xIncr)
        if (remainingSteps <= 0):
            self.position.x = remainingSteps * -1
        else:
            self.position.moveX(xIncr)
        self.position.moveY(yIncr)

    def inspect(self):
        return self.lines[self.position.y][self.position.x]
    
    def isTree(self):
        return "#" == self.inspect()
    
    def isFinished(self):
        return (self.rows - 1) == self.position.y

def runWithSlope(x , y):
    treeCount = 0
    matrix = Matrix()
    while not matrix.isFinished():
        matrix.move(x, y)
        if matrix.isTree():
            treeCount += 1

    print("Total number of trees = %d" % (treeCount))
    return treeCount

treeCountProduct = 1
treeCountProduct *= runWithSlope(1, 1)
treeCountProduct *= runWithSlope(3, 1)
treeCountProduct *= runWithSlope(5, 1)
treeCountProduct *= runWithSlope(7, 1)
treeCountProduct *= runWithSlope(1, 2)

print("Final Product = %d" % (treeCountProduct))
