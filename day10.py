def separate_lsts(lst1, lst2):
    if len(lst2) > len(lst1):
        tmp = lst1
        lst1 = lst2
        lst2 = tmp
    new_lst1 = []
    for i in lst1.split(","):
        if i not in lst2:
            new_lst1.append(i)
    return [",".join(new_lst1), lst2]

def main(input):
    goal_configs = []
    buttons = []
    joltage_requirements = []
    for line in input.splitlines():
        elements = line.split(" ")
        goal_configs.append(list(elements[0][1:len(elements[0])-1]))
        button_lst = []
        for button_str in elements[1:len(elements)-1]:
            button_lst.append([int(i) for i in button_str[1:len(button_str)-1].split(",")])
        buttons.append(button_lst)
        joltage_requirements.append([int(i) for i in elements[len(elements)-1][1:len(elements[len(elements)-1])-1].split(",")])

    result = 0
    for idx in range(len(goal_configs)):
        even_lst, odd_lst = [], []
        for i in range(len(goal_configs[idx])):
            tmp_lst = []
            for button_idx in range(len(buttons[idx])):
                if i in buttons[idx][button_idx]:
                    tmp_lst.append(str(button_idx))
            tmp_lst = ",".join(tmp_lst)
            if goal_configs[idx][i] == ".":
                if tmp_lst not in even_lst:
                    to_append = [tmp_lst]
                    for j in range(len(even_lst)):
                        if even_lst[j] in tmp_lst or tmp_lst in even_lst[j]:
                            to_append = separate_lsts(even_lst[j], tmp_lst)
                            del even_lst[j]
                            break
                    for lst in to_append:
                        even_lst.append(lst)
            elif goal_configs[idx][i] == "#" and tmp_lst not in odd_lst:
                odd_lst.append(tmp_lst)
        #print(even_lst, odd_lst)

        min = -1
        for i in range(2**len(buttons[idx])):
            cur_config = bin(i)[2:].zfill(len(buttons[idx]))
            print("cur_config: ", cur_config)
            condition_fulfilled = True
            for odd_set in odd_lst:
                sum = 0
                for pos in odd_set.split(","):
                    if cur_config[int(pos)] == "1":
                        sum += 1
                if sum % 2 == 0:
                    condition_fulfilled = False
                    break

            if condition_fulfilled:
                for even_set in even_lst:
                    sum = 0
                    for pos in even_set.split(","):
                        if cur_config[int(pos)] == "1":
                            sum += 1
                    if sum % 2 != 0:
                        condition_fulfilled = False
                        break
            if condition_fulfilled:
                if min == -1:
                    min = cur_config.count("1")
                elif cur_config.count("1") < min:
                    min = cur_config.count("1")
        result += min
        #print(min)

        """
        config = ["." for _ in range(len(goal_configs[idx]))]
        solved = False
        for i in range(len(odd_lst)):
            cur_element = odd_lst[i]
            if len(cur_element) == 1: # toggle this button
                config[int(cur_element)] = "#"
                print("updated config: ", config)
                del odd_lst[i]
                for j in range(len(odd_lst) - 1, -1, -1):
                    if cur_element in odd_lst[j]:
                        del odd_lst[j]
                for j in range(len(even_lst)-1, -1, -1):
                    if cur_element in even_lst[j]:
                        remaining_lst = separate_lsts(even_lst[j], cur_element)[0]
                        if remaining_lst not in odd_lst:
                            odd_lst.append(remaining_lst)
                        del even_lst[j]
        """
    print("part 1: ", result)


with open("inputs/day10", "r") as file:
    input = file.read()
main(input)