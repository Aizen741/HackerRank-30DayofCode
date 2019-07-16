mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())


def totalmealcost():
    tip = mealCost * tipPercent / 100
    tax = mealCost * taxPercent / 100
    totalcost = round((mealCost + tip + tax))

    return totalcost


print(totalmealcost())