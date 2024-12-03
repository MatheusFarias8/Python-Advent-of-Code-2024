def split_input():
    lines = []

    with open("input.txt") as file:
        lines = file.readlines()

    left = []
    right = []

    for i in range(len(lines)):
        left.append(int(lines[i].split(" ")[0]))
        right.append(int(lines[i].split(" ")[-1]))

    left.sort()
    right.sort()

    return left, right

left, right = split_input()

def part1():
    total = 0

    for i in range(len(left)):
        total += abs(left[i] - right[i])

    return total

def part2():
    total = 0

    for i in range(len(left)):
        total += right.count(left[i]) * left[i]

    return total
