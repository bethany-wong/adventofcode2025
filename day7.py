def main(input):
    map = []
    for line in input.splitlines():
        map.append(list(line))
    row_cnt, col_cnt = len(map), len(map[0])
    split_cnt = 0
    start_index = -1
    for row in range(1, row_cnt):
        for col in range(col_cnt):
            if row == 1:
                if map[0][col] == "S":
                    map[1][col] = "|"
                    start_index = col
            else:
                if map[row][col] == "." and map[row - 1][col] == "|":
                    map[row][col] = "|"
                if map[row][col] == "^" and map[row - 1][col] == "|":
                    for neighbor in [col - 1, col + 1]:
                        if 0 <= neighbor < col_cnt:
                            map[row][neighbor] = "|"
                    split_cnt += 1
    print("part 1: ", split_cnt)

    for col in range(col_cnt):
        map[row_cnt - 1][col] = 1 if map[row][col] == "|" else 0

    for row in range(row_cnt - 2, 0, -1):
        for col in range(col_cnt):
            if map[row][col] == "|":
                map[row][col] = map[row + 1][col]
        for col in range(col_cnt):
            if map[row][col] == "^":
                map[row][col] = map[row][col - 1] + map[row][col + 1]
    print("part 2: ", map[1][start_index])

with open("inputs/day7", "r") as file:
    input = file.read()
main(input)