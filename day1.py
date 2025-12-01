import math

def part1(str, dial):
    value = int(str[1:])
    if str[0] == "R":
        dial += value
    else:
        dial -= value
    return [1 if dial % 100 == 0 else 0, dial % 100]


def part2(str, dial):
    value = int(str[1:])
    threshold = dial if str[0] == "L" else (100 - dial)
    if dial == 0:
        threshold = 100
    zero_cnt = (1 if value % 100 >= threshold else 0) + math.floor(value/100)
    print(str, zero_cnt)
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
print(part2("R1000", 50))
print(part2("R111", 99))