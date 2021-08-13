first_name = "Dean"
mid_name = "van"
last_name = "Thompson"
multiply_string = "good "

print(first_name, last_name)
print(first_name.isprintable())
print(first_name.upper())
print(mid_name.capitalize())
print(first_name.lower())
print(len(last_name))
print(last_name.find("s"))
print(mid_name.isdigit())
print(mid_name.isalpha())
print(last_name.count("o"))
print(last_name.replace("o", "i"))
# repeat or multiply string
print(multiply_string * 5)
print()

# no need for the plus symbol when it comes to string concatenation
# 1.
print("Your other name should be", last_name, "or", first_name)
print("His name in full is", first_name, last_name)
# 2.
print("Hello " "world")

# 3.
print("It doesn't matter what tomorrow brings along. "
      "We'll surely win and dominate there too", end="!!!")
# use the 'end=(string)' to end a given string with a string
# instead of a new line

# print multiple line statements with exact formats
# - works like the HTML <pre> tag
print(""" 
Because He lives... 
I can face tomorrow
""")