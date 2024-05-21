# v4 - import and apply currency function, integrate write to file
import pandas
from datetime import date
import re


# checks user response is a valid response based on a list of options
def string_check(question, answer_list, short_response, error):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        while True:
            for item in answer_list:
                try:
                    short_response = int(short_response)
                    if response == item[:short_response] or response == item:
                        return item

                except TypeError:
                    list_spot = answer_list.index(item)
                    if response == short_response[list_spot] or response == item:
                        return item

            # If not, print error
            else:
                print(error)
                print()
                break


# Converts units
def unit_converter(unit, amount):
    # dict of units and what to multiply the
    # original amount by convert to ideal unit
    unit_dict = {
        "mg": 0.001,
        "g": 1,
        "kg": 1000,
        "ml": 0.001,
        "l": 1,
        "kl": 1000
    }

    if unit in ["mg", "g", "kg"]:
        final_unit = "g"
    else:
        final_unit = "l"
    converted = amount * float(f"{unit_dict.get(unit)}")
    return [converted, final_unit]


# Check that a float is more than 0 or 'xxx' or ""
def num_check(question, error, allow_blank):
    while True:

        response = input(question).replace(" ", "")
        try:
            response = float(response)

            if response <= 0:
                print(error)
                continue

            return response

        except ValueError:
            if allow_blank == "n" or response != "":
                print(error)
                continue
            else:
                return response


# Shows instructions
def show_instructions():
    print('''\n 
***** Instructions *****

For each product, enter ...
- The products name (can't be blank)
- The products weight (include unit)
- The products price in dollars (must be more than $0.00)

There are two categories of units the program accepts. They are mg/g/kg and ml/l/kl.
You can only use one category of unit for each run through of the program.

When you have entered all the products, press 'xxx' to quit.

The program will then display all the product details,
including the weight of each product, the converted weight, the price of each product,
and the price per one g/l for each product.

The program will then recommend one or more item/s based on their price/weight
This information will also be automatically written to a text file

**************************''')


# currency formatting function
def currency(x):
    x = f"${x:.2f}"
    # if the price is 0.00 after formatting, change it to 0.01
    if x == "$0.00":
        x = "$0.01"
    return x


# Main routine starts here

# create lists to hold product details
name_list = []
weight_list = []
price_list = []
converted_list = []
price_weight_strings = []
# for finding recommendation
price_weight_numbers = []

# Create strings
converted_unit = ""

# create unit lists for checking units
full_unit = ["milligram", "gram", "kilogram", "xxx", "millilitre", "litre", "kilolitre"]
short_unit = ["mg", "g", "kg", "xxx", "ml", "l", "kl"]

product_dict = {
    "Product": name_list,
    "Weight": weight_list,
    "  Converted": converted_list,
    "  Price": price_list,
    "  Price/Weight": price_weight_strings
}
# ask if the user wants to see instructions
want_instructions = string_check("Would you like to see the instructions?: ",
                                 ["yes", "no"], "1", "Please answer yes/no")
if want_instructions == "yes":
    show_instructions()

# Get the user's budget
budget = num_check("What is your budget in dollars?(press <enter> if you have no budget): $",
                   "Please enter a number more than 0.", "y")

while True:
    # Loop to get product info
    product_name = ""
    while product_name != "xxx":
        # Get the product name
        product_name = input("\nWhat is the name of the product? ")
        # don't allow duplicate names or blank names
        if product_name in name_list:
            print("Please enter a unique name for every product.")
            continue
        elif product_name.replace(" ", "") == "":
            print("Your product name cannot be blank.")
            continue
            # if exit code entered, break loop
        elif product_name == "xxx":
            break

        # get the original item (amount + unit or just amount)
        get_item = input("Please enter the weight of the product: ").replace(" ", "").replace(",", "")
        # if the user doesn't input an amount, or their amount is negative, output error
        if get_item == "" or get_item[0] == "-":
            print("Please enter an amount more than 0")
            continue
        elif get_item == "xxx":
            break

        # if they didn't input a unit, ask for unit
        try:
            get_amount = float(get_item)
            get_unit = string_check("Weight unit? ", short_unit, full_unit,
                                    "Please answer mg/g/kg or xxx to quit.")
            if get_unit == "xxx":
                break

        # otherwise,separate amount from unit
        except ValueError:

            # separate amount from item
            get_amount = re.findall(r'[0-9]+', get_item)

            # if there is no amount, output error
            if len(get_amount) == 0:
                print("Please enter an amount more than 0")
                continue

            # if the list is longer than one, format as a decimal
            if len(get_amount) == 2:
                get_amount = f"{get_amount[0]}.{get_amount[1]}"
            # else, put the list into a string to convert to float
            else:
                get_amount = f"{get_amount[0]}"

            get_amount = float(get_amount)

            # if the amount is 0, output error
            if get_amount == 0:
                print("Please enter an amount more than 0")
                continue

            # Get unit from item and turn to string
            get_unit = re.findall(r'[a-zA-Z]+', get_item)
            get_unit = f"{get_unit[0]}"
            get_unit = get_unit.replace("s", "").lower()

            if get_unit not in short_unit and get_unit not in full_unit:
                # if the unit is not valid, output error
                print("Please enter a number with a valid unit(mg/g/kg or ml/l/kl).")
                continue

            # if the unit is in a long form(kilograms) get it's short form(kg)
            if len(get_unit) > 2:
                list_location = full_unit.index(get_unit)
                get_unit = short_unit[list_location]

            # if their unit is 'xxx', exit code
            if get_unit == "xxx":
                break

        # format for list
        weight = f"{get_amount}{get_unit}"
        # use function to convert and print
        converted_item = unit_converter(get_unit, get_amount)
        # get the different variables that the function returned
        converted_weight = converted_item[0]
        # if the second weight uses a different weight category i.e. 1- 2g 2- 2l, output error
        if len(weight_list) > 0:
            if converted_item[-1] != (weight_list[0])[-1]:
                print("Please enter an item with the same unit type as your first item.")
                continue
        converted_unit = converted_item[1]

        # Get price of Product
        price = num_check("What is the price of your product?: $", "Please enter a number more than 0.", "n")
        if budget != "":
            if price > budget:
                print("This item is out of your budget.")
                continue

        # Get the price/weight
        price_weight = price / converted_weight

        # format for lists
        price = currency(price)
        weight = f"{get_amount}{get_unit}"
        converted_product = f"{converted_weight}{converted_unit}"
        price_weight_string = f"{currency(price_weight)}/{converted_unit}"

        # Add to lists
        # don't add exit code to name list
        if product_name != "xxx":
            name_list.append(product_name)
        weight_list.append(weight)
        converted_list.append(converted_product)
        price_list.append(price)
        price_weight_strings.append(price_weight_string)
        price_weight_numbers.append(price_weight)

    if len(name_list) == 0:
        print("Please enter at least one product.")
        continue
    else:
        break

# get recommendation
rec_price = min(price_weight_numbers)
rec_price_string = currency(rec_price)
# if multiple items are equally the best deal, print all
if price_weight_numbers.count(rec_price) > 1:
    rec_string = f"The following items are all equally the best deal, which is {rec_price_string} " \
                 f"per 1{converted_unit}.\n"
    rec_multiple = []
    for rec_item in name_list:
        rec_place = name_list.index(rec_item)
        if price_weight_numbers[rec_place] == rec_price:
            rec_string += f"|   {rec_item}\n"
else:
    rec_place = price_weight_numbers.index(rec_price)
    rec_name = name_list[rec_place]
    rec_string = f"{rec_name} is the best deal, being {rec_price_string} per 1{converted_unit}, "
    f"which is cheaper than the other products.\n"


# Get the date
today = date.today()
# Get day, month, and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# Format date heading and filename
format_date = f"{day}/{month}/{year}"
filename = f"PC_{year}_{month}_{day}"

# Create frame, set index
compare_frame = pandas.DataFrame(product_dict)
compare_frame = compare_frame.set_index('Product')

# create strings for printing...
heading = f"\n***** Price Compare - {format_date} *****\n"
rec_title = "\n--- Recommended Item/s: ---"
if budget != "":
    budget_string = f"Budget: {currency(budget)}\n"
else:
    budget_string = "No budget.\n"

# Change frame to s string so that I can export it to file
compare_frame_string = pandas.DataFrame.to_string(compare_frame)

# list holding content to print / write to file
to_write = [heading, budget_string, compare_frame_string, rec_title, rec_string]

# print output
for frame_item in to_write:
    print(frame_item)

# write output to file
# create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for file_item in to_write:
    text_file.write(file_item)
    text_file.write("\n")

# close file
text_file.close()
