# checks user response is a valid response based on a list of options
def string_check(question, answer_list, num_letters, error):
    valid = False
    while not valid:
        # make response lowercase and get rid of spaces
        response = input(question).lower().replace(" ", "")

        while True:
            for item in answer_list:
                if response == item[:num_letters] or response == item:
                    return item

            # If not, print error
            else:
                print(error)
                print()
                break


while True:
    print()
    yn_check = string_check("Yes or No? ", ["yes", "no"], 1,
                            "Please answer yes/no.")
    print(yn_check)
    print()
    cc_check = string_check("Cash or Credit? ", ["cash", "credit"], 2,
                            "Please answer cash/card.")
    print(cc_check)
