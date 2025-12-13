def main(input):
    numbers = []
    ranges = []
    for i in range(len(input.splitlines()) - 1):
        line = input.splitlines()[i]
        nums = []
        ranges_row = []
        current = ""
        index_range = {}
        for j in range(len(line)):
            char = line[j]
            if char == " ":
                if current != "":
                    nums.append(current)
                    current = ""
                    ranges_row.append(index_range)
                    index_range = {}
            else:
                current += char
                if "lower" not in index_range:
                    index_range["lower"] = j
                    index_range["upper"] = j
                else:
                    index_range["upper"] = j
        if current != "":
            nums.append(current)
            ranges_row.append(index_range)
        numbers.append(nums)
        ranges.append(ranges_row)

    operators = list(input.splitlines()[len(input.splitlines()) - 1].replace(" ", ""))

    total = 0
    for i in range(len(operators)):
        if operators[i] == "+":
            result = 0
            for row in numbers:
                result += int(row[i])
        else:
            result = 1
            for row in numbers:
                result *= int(row[i])
        total += result
    print("part1: ", total)

    row_count = len(numbers)
    column_count = len(operators)
    total = 0
    for col in range(column_count):
        current_range = {}
        for row in range(row_count):
            if "lower" not in current_range:
                current_range["lower"] = ranges[row][col]["lower"]
                current_range["upper"] = ranges[row][col]["upper"]
            elif ranges[row][col]["lower"] < current_range["lower"]:
                current_range["lower"] = ranges[row][col]["lower"]
            elif ranges[row][col]["upper"] > current_range["upper"]:
                current_range["upper"] = ranges[row][col]["upper"]
        lst = ["" for i in range(current_range["upper"] - current_range["lower"] + 1)]
        for i in range(current_range["upper"], current_range["lower"] - 1, -1):
            for row in range(row_count):
                cur_range = ranges[row][col]
                if cur_range["lower"] <= i <= cur_range["upper"]:
                    lst[i - current_range["lower"]] += numbers[row][col][i - cur_range["lower"]]
        if operators[col] == "+":
            result = 0
            for num in lst:
                result += int(num)
        else:
            result = 1
            for num in lst:
                result *= int(num)
        total += result
    print("part2: ", total)


with open("inputs/day6", "r") as file:
    input = file.read()
main(input)