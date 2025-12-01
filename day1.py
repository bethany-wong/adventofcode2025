import math

def part1(str, dial):
    value = int(str[1:])
    dial = dial + value if str[0] == "R" else dial - value
    return [1 if dial % 100 == 0 else 0, dial % 100]

def part2(str, dial):
    value = int(str[1:])
    threshold = 0 if dial == 0 else (dial if str[0] == "L" else (100 - dial))
    zero_cnt = (1 if value % 100 >= threshold else 0) + math.floor(value/100)
    return [zero_cnt, part1(str, dial)[1]]

def main(input):
    zero_cnt = 0
    dial = 50
    for line in input.splitlines():
        lst = part1(line, dial)
        zero_cnt += lst[0]
        dial = lst[1]
    print("part 1 password is: ", zero_cnt)

    zero_cnt = 0
    dial = 50
    for line in input.splitlines():
        lst = part2(line, dial)
        zero_cnt += lst[0]
        dial = lst[1]
    print("part 2 password is: ", zero_cnt)

with open("inputs/day1", "r") as file:
    input = file.read()
main(input)