# formatted strings - more like template strings in JS
# begin the string with f, followed by quotes ie. f" {} ",
# enter variable names in the curly braces, eg f"{name}"
# curly braces serve as placeholders for variables

first_name = input("Your first name: ")
last_name = input("Your last name: ")
message = f"Welcome to our world, {first_name} {last_name}!"
print(message)
print()

# slicing strings
print(len(message))
print(message[0:])
print(message[0:-1])
print(message[0:7])
print(message[22:])
print()

# use the 'in' operator to check for the existence of a
# sequence of characters in a given string
sentence = "Here is some nice tutorial on Python"
print("nice" in sentence)
print("tut" in sentence)
print("rials" in sentence)
