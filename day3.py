def find_max(line, start_index, max_num): # find the first occurrence of largest number
    max_index = -1
    for i in range(start_index, len(line)):
        if max_index == -1 and int(line[i]) <= max_num:
            max_index = i
            continue
        if int(line[max_index]) < int(line[i]) <= max_num:
            max_index = i
    return max_index


def find_largest_number(line, start_index, length):
    if length == 0:
        return ""
    for i in range(9, 0, -1):
        index = find_max(line, start_index, i)
        if index != -1 and index < len(line) - (length - 1):
            return line[index]+find_largest_number(line, index + 1, length - 1)
    return ""


def main(input, part2=False):
    sum = 0
    for line in input.splitlines():
        num = find_largest_number(line, 0, 12 if part2 else 2)
        sum += int(num)
    print("part2: ", sum)

with open("inputs/day3", "r") as file:
    input = file.read()
main(input, True)