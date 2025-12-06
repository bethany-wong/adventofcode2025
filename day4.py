neighbors = [{"x":  -1, "y": -1}, {"x": -1, "y": 0}, {"x": -1, "y": 1},
             {"x":  0, "y": -1}, {"x": 0, "y": 1},
             {"x":  1, "y": -1}, {"x": 1, "y": 0}, {"x": 1, "y": 1}]

def in_map(map, x, y):
    return 0 <= x < len(map) and 0 <= y < len(map[0])

def find_rolls(map, x, y):
    if map[x][y] != "@":
        return 999999
    sum_rolls = 0
    for neighbor in neighbors:
        sum_rolls += 1 if in_map(map, x + neighbor["x"], y + neighbor["y"]) and map[x + neighbor["x"]][y + neighbor["y"]] == "@" else 0
    return sum_rolls

def find_accessible_paper_rolls(map):
    lst = []
    for i in range(len(map)):
        for j in range(len(map[0])):
            lst.append([i, j]) if find_rolls(map, i, j) < 4 else 0
    return lst

def main(input):
    map = []
    for line in input.splitlines():
        map.append(list(line))
    accessible_paper_rolls = find_accessible_paper_rolls(map)
    print("part1: ", len(accessible_paper_rolls))
    total_removed = 0
    while len(accessible_paper_rolls) > 0:
        for pos in accessible_paper_rolls:
            map[pos[0]][pos[1]] = "x"
        total_removed += len(accessible_paper_rolls)
        accessible_paper_rolls = find_accessible_paper_rolls(map)
    print("part2: ", total_removed)

with open("inputs/day4", "r") as file:
    input = file.read()
main(input)