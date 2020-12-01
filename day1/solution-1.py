print("starting program to find numbers with sum 2020")

with open('day1/input.txt') as f:
    lines = f.read().splitlines()

input_nums = []
for str in lines:
    input_nums.append(int(str))

for x in input_nums:
    for y in input_nums:
        if (x+y) == 2020:
            print("%d + %d = 2020", x, y)
            print("product is %d", x*y)