# since I will only ever need blank or exit code, make it just an extra option.
# Check that an int/float is more than 0
def num_check(question, error, allowed_string):
    while True:

        response = input(question).replace(" ", "")
        try:
            # Check if response is a number
            response = float(response)

            # Check if response is more than 0
            if response <= 0:
                # if not, give error and re-ask question
                print(error)
                continue

            return response

        except ValueError:
            # check if response is valid
            if response == allowed_string:
                return response
            # if not, give error and re-ask question
            else:
                print(error)
                continue


# Main routine goes here
while True:

    while True:
        break
        # Ask the user for their budget
        get_budget = num_check("\nWhat is your budget?(press <enter> if you have no budget): $",
                               "Please enter a number more than 0 (or <enter> for no budget)", "")
        # if the user doesn't enter a budget, assume they have no budget
        if get_budget == "":
            print("No Budget (Program continues)")
            continue
        else:
            print(f'${get_budget:.2f} (Program continues)')
            continue

    while True:

        get_cost = num_check("\nHow much does it cost? $", "Please enter a number more than 0", "xxx")
        if get_cost == "xxx":
            print("Loop ends")
            break
        else:
            print(f'${get_cost:.2f} (Program continues)')
            continue
