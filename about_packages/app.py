# Importing a function from a module in a package
from about_packages.store import *

call = say_something()
print(call)

user_input = input("""Enter a list of items you want to order:
(PS: separate items with a comma eg: Shirt, Shoe, Bag)
""")

split_order = user_input.split(",")

print(place_order(split_order))
