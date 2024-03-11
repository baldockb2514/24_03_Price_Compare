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


while True:
    print()
    yn_check = string_check("Yes or No? ", ["yes", "no"], "1",
                            "Please answer yes/no.")
    print(yn_check)
    print()
    cc_check = string_check("Weight unit? ", ["gram", "milligram", "kilogram"], ["g", "mg", "kg"], "Please answer "
                                                                                                   "mg/g/kg.")
    print(cc_check)
