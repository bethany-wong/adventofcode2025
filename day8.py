import math

def calculate_distance(box_1,  box_2):
    return math.sqrt((box_1["x"]-box_2["x"])**2 + (box_1["y"]-box_2["y"])**2 + (box_1["z"]-box_2["z"])**2)

def merge(circuit_list):
    result = set()
    for circuit in circuit_list:
        for ele in circuit:
            result.add(ele)
    return result

def main(input, num_iterations, part1=True):
    boxes = []
    lines = input.splitlines()
    for line in lines:
        tmp = line.split(",")
        boxes.append({"x": int(tmp[0]), "y": int(tmp[1]), "z": int(tmp[2])})
    distances = {}
    for i in range(len(boxes)):
        for j in range(i + 1, len(boxes)):
            distances[calculate_distance(boxes[i], boxes[j])] = [lines[i], lines[j]]
    if not part1:
        num_iterations = len(distances)
        print("Number of iterations:", num_iterations)
    circuits = []
    for _ in range(num_iterations):
        current_boxes = distances[min(distances.keys())]
        del(distances[min(distances.keys())])
        belong_to_circuit = []
        for circuit_index in range(len(circuits)-1, -1, -1):
            if current_boxes[0] in circuits[circuit_index] or current_boxes[1] in circuits[circuit_index]:
                belong_to_circuit.append(circuit_index)
        if len(belong_to_circuit) == 1:
            circuits[belong_to_circuit[0]].add(current_boxes[0])
            circuits[belong_to_circuit[0]].add(current_boxes[1])
        elif len(belong_to_circuit) == 0:
            circuits.append(set(current_boxes))
        else:
            new_circuit = merge(circuits[i] for i in belong_to_circuit)
            for i in belong_to_circuit:
                del circuits[i]
            new_circuit.add(current_boxes[0])
            new_circuit.add(current_boxes[1])
            circuits.append(new_circuit)
        if len(circuits) == 1 and len(circuits[0]) == len(boxes):
            print("part 2: ", current_boxes)
            break

    if part1:
        circuit_sizes = set()
        for circuit in circuits:
            circuit_sizes.add(len(circuit))
        circuit_sizes = list(sorted(circuit_sizes, reverse=True))
        part1 = 1
        for i in range(3):
            part1 *= circuit_sizes[i]
        print("part 1: ", part1)


with open("inputs/day8", "r") as file:
    input = file.read()
main(input, 10, False)