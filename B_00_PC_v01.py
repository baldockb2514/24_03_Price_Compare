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

