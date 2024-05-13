# export information to file
import pandas
from datetime import date

# set up lists of info
all_names = ["a", "b", "c", "d"]
prices = ["$150", "$10", "$65", "$500"]
weights = ["0.5kg", "300000mg", "650g", "1.5kg"]
price_weights = [0.3, 0.03, 0.1, 0.3]
converted_list = ["500g", "300g", "650g", "1500g"]
price_weight_strings = ["$0.30/g", "$0.03/g", "$0.10/g", "$0.30/g"]

# set up frame dict
product_dict = {
    "Product": all_names,
    "Weight": weights,
    "Price": prices,
    "  Converted": converted_list,
    "  Price/Weight": price_weight_strings
}

compare_frame = pandas.DataFrame(product_dict)

# set index at end
compare_frame = compare_frame.set_index('Product')

# *** Get current date for heading and filename ***
# get today's date
today = date.today()

# Get day, month, and year as individual strings
day = today.strftime("%d")
month = today.strftime("%m")
year = today.strftime("%Y")

# get heading and filename
format_date = f"{day}/{month}/{year}"
filename = f"PC_{year}_{month}_{day}"

# Change frame to s string so that we can export it to file
compare_frame_string = pandas.DataFrame.to_string(compare_frame)

# format frame title
heading = f"\n***** Price Compare - {format_date} *****\n"

# create strings for printing...
rec_title = "\nRecommended Product/s:"
rec_string = f"b is the best deal, being $0.03 per 1g, "
f"which is cheaper than the other products.\n"

# list holding content to print / write to file
to_write = [heading, compare_frame_string, rec_title, rec_string]

# print output
for item in to_write:
    print(item)

# write output to file
# create file to hold data (add .txt extension)
write_to = f"{filename}.txt"
text_file = open(write_to, "w+")

for item in to_write:
    text_file.write(item)
    text_file.write("\n")

# close file
text_file.close()
