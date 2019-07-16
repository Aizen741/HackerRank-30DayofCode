mealCost = float(input())
tipPercent = int(input())
taxPercent = int(input())

def totalmealcost():
    tip = float(int(mealCost)* tipPercent/100)
    tax = float(int(mealCost)*taxPercent/100)

    totalcost = float(mealCost + tip + tax )
    return round(totalcost)

print(totalmealcost())