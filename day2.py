def check(num, repeated): # num: string, repeated: integer
    if len(num)%repeated != 0:
        return False
    pointer = 0
    length = len(num)//repeated # length of pattern
    patterns = set()
    while pointer <= len(num) - length:
        current = num[pointer:pointer+length]
        patterns.add(current)
        pointer += length
    return True if len(patterns) == 1 else False

def main(input, part2=False):
    sum = 0
    for line in input.split(","):
        min_max = line.split("-")
        for i in range(int(min_max[0]), int(min_max[1]) + 1):
            for repeated in range(2, len(str(i))+1):
                if not part2 and repeated != 2:
                    continue
                if check(str(i), repeated):
                    sum += i
                    break
    print(sum)

with open("inputs/day2", "r") as file:
    input = file.read()
main(input, True)