import re

class Node:
    def __init__(self, name, count):
        self.name = name
        self.count = int(count)
        self.children = []
    
    def addChild(self, child):
        self.children.append(child)
    
    def __repr__(self):
        return str(vars(self))


def getLinesForDay(day):
    with open(f'day{day}/input.txt',) as f:
        lines = f.read().splitlines()
        return lines

# Part 1
def getFromCache(name, count, nodeCache):
    cachedNode = nodeCache.get(name, Node(name, count))
    nodeCache[name] = cachedNode
    return cachedNode

def addNodeToCache(line, nodeCache):
    mainSplit = line.split(' contain ')
    node = getFromCache(mainSplit[0][:mainSplit[0].rfind(' ')], 1, nodeCache)
    childSplit = list(map(lambda y: y.strip(), filter(lambda x: x != 'no other bags', mainSplit[1][:-1].split(','))))
    for childStr in childSplit:
        node.addChild(
                getFromCache(
                    childStr[childStr.find(' ')+1:childStr.rfind(' ')], 
                    childStr[:childStr.find(' ')],
                    nodeCache))

def isColorPresent(node, key, nodeCache):
    for child in node.children:
        if (child.name == key) or isColorPresent(child, key, nodeCache):
            return True
    return False

def solvePart1():
    nodeLinkedCache = {}
    lines = getLinesForDay(7)
    for line in lines:
        addNodeToCache(line, nodeLinkedCache)

    total = 0
    for node in nodeLinkedCache.values():
        if isColorPresent(node, 'shiny gold', nodeLinkedCache):
            total += 1
    return total
print(f'Total number of bags that can hold Santa\'s bag - {solvePart1()}')

# Part 2
def findInnerBagCount(node, nodeCache):
    total = 0
    for child in node.children:
        total = total + child.count + (child.count * findInnerBagCount(nodeCache[child.name], nodeCache))
    return total

def solvePart2():
    nodeIsolatedCache = {}
    lines = getLinesForDay(7)
    for line in lines:
        mainSplit = line.split(' contain ')
        node = Node(mainSplit[0][:mainSplit[0].rfind(' ')], 1)
        childSplit = list(map(lambda y: y.strip(), filter(lambda x: x != 'no other bags', mainSplit[1][:-1].split(','))))
        for childStr in childSplit:
            node.addChild(
                    Node(
                        childStr[childStr.find(' ')+1:childStr.rfind(' ')], 
                        childStr[:childStr.find(' ')]))
        nodeIsolatedCache[node.name] = node

    santaNode = nodeIsolatedCache.get('shiny gold')
    return findInnerBagCount(santaNode, nodeIsolatedCache)

print(f'Total bags inside santas bag - {solvePart2()}')
