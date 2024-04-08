# Functions go here
import re


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


# checks user response is a valid response based on a list of options
def string_check(question, answer_list, short_response, error, replace_s):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        if replace_s == "yes":
            if response[-1] == "s":
                response = response[:-1]

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
            # allow 'xxx' as a valid response
            if response == "xxx":
                return response
            elif allow_blank == "no" or response != "":
                print(error)
                continue
            else:
                return response


# gets the product weight amount and unit

def get_weight():
    # Create unit lists
    full_unit = ["milligram", "gram", "kilogram", "xxx", "millilitre", "litre", "kilolitre"]
    short_unit = ["mg", "g", "kg", "xxx", "ml", "l", "kl"]

    while True:

        # get the original item (amount + unit or just amount)
        print()
        get_item = input("Please enter the weight/amount: ").replace(" ", "").replace(",", "")
        # if the user inputs a negative number, or doesn't enter any number, output error
        if get_item == "" or get_item[0] == "-":
            print("Please enter an amount more than 0")
            continue
        elif get_item == "xxx":
            break

        # if they didn't input a unit, ask for unit
        try:
            get_amount = float(get_item)
            get_unit = string_check("Weight unit? ", short_unit, full_unit,
                                    "Please answer mg/g/kg or ml/l/kl or xxx to quit.", "yes")

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
            # if the unit is not valid, output error
            if get_unit[0] not in short_unit and get_unit[0] not in full_unit:
                print("Please enter a number with a valid unit(mg/g/kg or ml/l/kl).")
                break
            # if their unit is kilo, ask for the user to specify
            if get_unit == "kilo":
                get_unit = string_check("do you mean kilograms or kilolitres?: ",
                                        ["kilogram", "kilolitre", "xxx"],
                                        ["kg", "kl", "xxx"], "Please enter either kg or kl", "yes")

            # if the unit is in a long form(kilograms) get it's short form(kg)
            if len(get_unit) > 2:
                list_location = full_unit.index(get_unit)
                get_unit = short_unit[list_location]

            # if th unit is 'xxx', exit code
            if get_unit == "xxx":
                break

        # us function to convert and print
        converted_item = unit_converter(get_unit, get_amount)
        print(converted_item[0], converted_item[1])


while True:
    get_weight()
    print("--- Loop Ends ---")
