
baggages = [
    {"weight": 3.5, "price": 250},
    {"weight": 2, "price": 175},
    {"weight": 5, "price": 400},
    {"weight": 3, "price": 200},
    {"weight": 5.5, "price": 500},
    {"weight": 1.5, "price": 125},
    {"weight": 6, "price": 500},
    {"weight": 4, "price": 250},
    {"weight": 2.5, "price": 175},
    {"weight": 4.5, "price": 250},
    {"weight": 1, "price": 100},
]

maxWeight = 20
sumWeight = 0
sumPrice = 0
myPackedBag = []

for baggage in baggages:
    #Calculate price per kilo and append to dictionary
    kiloPrice = baggage['price']/baggage['weight']
    baggage['kiloPrice'] = kiloPrice

# Sort array by kiloprice
baggages = sorted(baggages, key = lambda i: i['kiloPrice'])



for baggage in baggages:
    # If space for bag, append bags
    if (sumWeight + baggage["weight"] <= maxWeight):
        myPackedBag.append(baggage)
        sumWeight = sumWeight + baggage["weight"]
        sumPrice = sumPrice + baggage["price"]


# Print the bag
print("Your bag weighs", sumWeight, "and costs", sumPrice, "kr")
print("Here is your bag: \n")
for item in myPackedBag:
    print(item)