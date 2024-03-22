# Check that an int/float is more than 0
def num_check(question, error, num_type):
    while True:

        try:
            response = num_type(input(question))

            if response <= 0:
                print(error)
                continue

            return response

        except ValueError:
            print(error)
            continue


# Main routine goes here
while True:
    get_int = num_check("How many do you need? ", "Please enter an integer (whole number) more than 0\n", int)
    print(f'{get_int}\n')

    get_cost = num_check("How much does it cost/ $", "Please enter a number more than 0\n", float)
    print(f'${get_cost:.2f}\n****** \n')
