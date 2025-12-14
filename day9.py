def main(input):
    red_tiles = []
    row_cnt, col_cnt = 0, 0
    for line in input.splitlines():
        current = [int(num) for num in line.split(",")]
        red_tiles.append({"x": int(current[0]), "y": int(current[1])})
        col_cnt = current[0] + 1 if current[0] + 1 > col_cnt else col_cnt
        row_cnt = current[1] + 1 if current[1] + 1 > row_cnt else row_cnt

    rectangles = {}
    for i in range(len(red_tiles)):
        for j in range(i+1, len(red_tiles)):
            area = red_tiles[i]["x"] - red_tiles[j]["x"] + 1 if red_tiles[i]["x"] >= red_tiles[j]["x"] else red_tiles[i]["x"] - red_tiles[j]["x"] + 1
            area *= red_tiles[i]["y"] - red_tiles[j]["y"] + 1 if red_tiles[i]["y"] >= red_tiles[j]["y"] else red_tiles[i]["y"] - red_tiles[j]["y"] + 1
            area = abs(area)
            if area not in rectangles:
                rectangles[area] = []
            rectangles[area].append([red_tiles[i], red_tiles[j]])
    print("part 1: ", max(rectangles.keys()))

    horizontal_lines = {}
    for row in range(row_cnt):
        tiles_in_row = []
        for tile in red_tiles:
            if tile["y"] == row:
                tiles_in_row.append(tile)
        if len(tiles_in_row) == 2:
            horizontal_lines[row] = sorted([tiles_in_row[0]["x"], tiles_in_row[1]["x"]])

    vertical_lines = {}
    for col in range(col_cnt):
        tiles_in_col = []
        for tile in red_tiles:
            if tile["x"] == col:
                tiles_in_col.append(tile)
        if len(tiles_in_col) == 2:
            vertical_lines[col] = sorted([tiles_in_col[0]["y"], tiles_in_col[1]["y"]])
    print(vertical_lines)

    max_area = 0
    max_area_corners = []
    for i in range(len(red_tiles)):
        for j in range(i + 1, len(red_tiles)):
            x = sorted([red_tiles[i]["x"], red_tiles[j]["x"]])
            y = sorted([red_tiles[i]["y"], red_tiles[j]["y"]])
            area = (x[1] - x[0] + 1) * (y[1] - y[0] + 1)
            if area > max_area:
                intersected = False
                for col in range(x[0] + 1, x[1]):
                    if col in vertical_lines:
                        if not (
                            vertical_lines[col][0] <= y[0] and vertical_lines[col][1] <= y[0]) and not(
                            vertical_lines[col][0] >= y[1] and vertical_lines[col][1] >= y[1]):
                            intersected = True
                            break
                if not intersected:
                    for row in range(y[0] + 1, y[1]):
                        if row in horizontal_lines and not (
                                horizontal_lines[row][0] <= x[0] and horizontal_lines[row][1] <= x[0]) and not (
                                horizontal_lines[row][0] >= x[1] and horizontal_lines[row][1] >= x[1]):
                            intersected = True
                            break
                if not intersected:
                    max_area = area
                    max_area_corners = [red_tiles[i], red_tiles[j]]
                    print("found max area: ", max_area, max_area_corners)
    print("part 2: ", max_area, max_area_corners)


with open("inputs/day9", "r") as file:
    input = file.read()
main(input)