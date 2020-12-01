print("starting program to find numbers with sum 2020")

with open('day1/input.txt') as f:
    lines = f.read().splitlines()

input_nums = []
for str in lines:
    input_nums.append(int(str))

for i in range(len(input_nums)):
    x=input_nums[i]
    for j in range(i, len(input_nums)):
        y=input_nums[j]
        for k in range(j, len(input_nums)):
            z=input_nums[k]
            if (x+y+z == 2020):
                print("%d + %d + %d = 2020", x, y, z)
                print("product is %d", x*y*z)
