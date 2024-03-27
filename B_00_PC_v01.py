import pandas
from datetime import date
import re


# checks user response is a valid response based on a list of options
def string_check(question, answer_list, short_answer, error):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        while True:
            for item in answer_list:
                try:
                    short_answer = int(short_answer)
                    if response == item[:short_answer] or response == item:
                        return item

                except TypeError:
                    list_spot = answer_list.index(item)
                    if response == short_answer[list_spot] or response == item:
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
    return f"{converted}{final_unit}"


# Check that an float is more than 0 or 'xxx' or ""
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
            # allow 'xxx' as a valid response
            if response == "xxx":
                return response
            elif allow_blank == "no" or response != "":
                print(error)
                continue
            else:
                return response


# Shows instructions
def show_instructions():
    print('''\n 
Instructions go here''')


# Main routine starts here

# create lists to hold product details
name_list = []
weight_list = []
price_list = []
converted_list = []
price_weight_list = []

product_dict = {
    "Name": name_list,
    "Weight": weight_list,
    "Price": price_list,
    "Converted": converted_list,
    "Price/Weight": price_weight_list
}
# ask if the user wants to see instructions
want_instructions = string_check("Would you like to see the instructions?: ",
                                 ["yes", "no"], "1", "Please answer yes/no")
if want_instructions == "yes":
    show_instructions()

product_name = ""
while product_name != "xxx":
    # get the original item (amount + unit or just amount)
    print()
    get_item = input("Please enter the weight/amount: ").replace(" ", "").replace(",", "")
    # if the user doesn't input ab
    if get_item == "" or get_item[0] == "-":
        print("Please enter an amount more than 0")
        continue
    elif get_item == "xxx":
        break

    # if they didn't input a unit, ask for unit
    try:
        get_amount = float(get_item)
        get_unit = string_check("Weight unit? ", ["mg", "g", "kg", "xxx", "ml", "l", "kl"],
                                ["milligram", "gram", "kilogram", "xxx", "millilitre", "litre", "kilolitre"],
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
        get_unit = get_unit.replace("s", "")
        # if their unit is kilo, ask for the user to specify
        if get_unit == "kilo":
            get_unit = string_check("do you mean kilograms or kilolitres?: ",
                                    ["milligram", "gram", "kilogram", "xxx", "millilitre", "litre", "kilolitre"],
                                    ["mg", "g", "kg", "xxx", "ml", "l", "kl"], "Please enter either kg or kl")

        # if the unit is in a long form(kilograms) get it's short form(kg)
        if len(get_unit) > 2:
            get_unit = get_unit.replace("s", "")
            full_unit = ["milligram", "gram", "kilogram", "xxx", "millilitre", "litre", "kilolitre"]
            short_unit = ["mg", "g", "kg", "xxx", "ml", "l", "kl"]
            list_location = full_unit.index(get_unit)
            get_unit = short_unit[list_location]

        # if th unit is 'xxx', exit code
        if get_unit == "xxx":
            break

    # us function to convert and print
    converted_item = unit_converter(get_unit, get_amount)
    print(converted_item)
