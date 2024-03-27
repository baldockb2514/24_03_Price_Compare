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


while True:

    while True:
        print()
        yn_check = string_check("Yes or No? ", ["yes", "no", "xxx"], "1",
                                "Please answer yes/no or xxx to quit.", "")
        if yn_check == "xxx":
            print("Program ends")
            break
        else:
            print(f"You chose {yn_check}")
            continue

    while True:
        print()
        cc_check = string_check("Weight unit? ", ["gram", "milligram", "kilogram", "xxx", "millilitres", "litres",
                                "kilolitres"], ["g", "mg", "kg", "xxx", "ml", "l", "kl"],
                                "Please answer mg/g/kg or xxx to quit.", "yes")
        if cc_check == "xxx":
            print("Program ends")
            break
        else:
            print(f"You chose {cc_check}")
            continue
