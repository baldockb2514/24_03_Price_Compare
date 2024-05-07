
# currency formatting function
def currency(x):
    x = f"${x:.2f}"
    # if the price is 0.00 after formatting, change it to 0.01
    if x == "$0.00":
        x = "$0.01"
    return x


price = float(input("Price: "))
price = currency(price)
print(price)
