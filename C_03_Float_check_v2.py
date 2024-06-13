# allow blanks and exit code

# Check that an int/float is more than 0
def num_check(question, error):
    while True:

        response = input(question).replace(" ", "")
        try:
            response = float(response)

            if response <= 0:
                print(error)
                continue

            return response

        except ValueError:
            if response == "xxx":
                return response
            elif response != "":
                print(error)
                continue
            else:
                return response


# Main routine goes here
while True:

    while True:
        # Ask the user for their budget
        get_budget = num_check("\nWhat is your budget?(press <enter> if you have no budget): $",
                               "Please enter a number more than 0 (or <enter> for no budget)")
        # if the user doesn't enter a budget, assume they have no budget
        if get_budget == "":
            print("No Budget (Program continues)")
            continue
        elif get_budget == "xxx":
            print("Loop ends")
            break
        else:
            print(f'${get_budget:.2f} (Program continues)')
            continue

    while True:

        get_cost = num_check("\nHow much does it cost/ $", "Please enter a number more than 0")
        if get_cost == "xxx":
            print("Loop ends\n********************")
            break
        else:
            print(f'${get_cost:.2f} (Program continues)')
            continue
