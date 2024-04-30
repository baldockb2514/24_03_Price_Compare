# find the best price/weight

# set up strings
names = []
prices = []
weights = []
price_weights = []
price_weights_strings = []

unit = input("What is the weight unit of the products? ")

while True:

    # Get name
    name = input("What is the name of the product? ")
    if name == "xxx":
        break
    names.append(name)

    # Get price
    price = float(input("What is the price of the product? "))
    prices.append(price)

    # Get weight
    weight = float(input("What is the weight of the product? "))
    weights.append(weight)

    # get price / weight
    price_weight = price/weight
    price_weights.append(price_weight)
    price_weight_string = f"${price_weight:.2f}/1{unit}"
    price_weights_strings.append(price_weight_string)
    continue

for item in names:
    get_place = names.index(item)
    print(f"")
