# find the best price/weight

# set up strings
names = []
prices = []
weights = []
price_weights = []
price_weights_strings = []

unit = input("What is the weight unit of the products? ")
print("\n-------------------")

while True:

    # Get name
    name = input("\nWhat is the name of the product? ")
    if name == "xxx":
        break
    names.append(name)

    # Get price
    price = float(input("What is the price of the product? $"))
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

print()
for item in names:
    get_place = names.index(item)
    print(f"{item} - ${prices[get_place]:.2f} - {weights[get_place]}{unit} - {price_weights_strings[get_place]}")

rec = min(price_weights)
rec_place = price_weights.index(rec)
print(f"\nThe best deal is {names[rec_place]}. It only costs {price_weights_strings[rec_place]}, "
      f"which costs less than all other items per {unit}.")
