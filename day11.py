def find_number_of_paths(devices, memory, current, end):
    if end in devices[current]:
        return 1
    sum = 0
    for child in devices[current]:
        if child != "out":
            if child not in memory:
                memory[child] = find_number_of_paths(devices, memory, child, end)
            sum += memory[child]
    return sum

def main(input, part2):
    devices = {}
    for line in input.splitlines():
        line = line.split(": ")
        devices[line[0]] = line[1].split(" ")
    if not part2:
        print("part 1: ", find_number_of_paths(devices, {}, "you", "out"))
        return

    print("part 2: ", find_number_of_paths(devices, {}, "svr", "fft") *
          find_number_of_paths(devices, {}, "fft", "dac") *
          find_number_of_paths(devices, {}, "dac", "out"))


with open("inputs/day11", "r") as file:
    input = file.read()
main(input, True)