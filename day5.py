def main(input):
    fresh_ingredients = []
    for line in input.split("\n\n")[0].split("\n"):
        fresh_ingredients.append({"lower": int(line.split("-")[0]), "upper": int(line.split("-")[1])})
    sum  = 0
    for i in input.split("\n\n")[1].split("\n"):
        i = int(i)
        for id_range in fresh_ingredients:
            if id_range["lower"] <= i <= id_range["upper"]:
                sum += 1
                break
    print("part1: ", sum)

    sum = 0
    for i in range(len(fresh_ingredients)):
        merged = False
        for j in range(i+1, len(fresh_ingredients)):
            if fresh_ingredients[i]["upper"] >= fresh_ingredients[j]["lower"] >= fresh_ingredients[i]["lower"]:
                if fresh_ingredients[j]["upper"] < fresh_ingredients[i]["upper"]:
                    fresh_ingredients[j]["upper"] = fresh_ingredients[i]["upper"]
                fresh_ingredients[j]["lower"] = fresh_ingredients[i]["lower"]
                merged = True # merged with upper or contained set
                break
            if fresh_ingredients[i]["upper"] >= fresh_ingredients[j]["upper"] >= fresh_ingredients[i]["lower"]:
                if fresh_ingredients[j]["lower"] > fresh_ingredients[i]["lower"]:
                    fresh_ingredients[j]["lower"] = fresh_ingredients[i]["lower"]
                fresh_ingredients[j]["upper"] = fresh_ingredients[i]["upper"]
                merged = True # merged with lower or contained set
                break
            if fresh_ingredients[j]["upper"] >= fresh_ingredients[i]["upper"] and fresh_ingredients[j]["lower"] <= fresh_ingredients[i]["lower"]:
                merged = True # with containing set
                break
        sum += fresh_ingredients[i]["upper"] - fresh_ingredients[i]["lower"] + 1 if not merged else 0
    print("part2: ", sum)

with open("inputs/day5", "r") as file:
    input = file.read()
main(input)