# handling errors are critical in every programming language
# exceptions could be caught and handled using the try - except block Python provides

try:
    age = int(input("Your age: "))
    dad_age = int(input("Your Dad's age: "))
    measure = age / dad_age
    print(f"You are {age} years old. You are {measure} of your Dad.")
except ValueError:
    print("Enter an age of numbers")
except ZeroDivisionError:
    print("Your Dad cannot be zero years old. Enter a proper age")

# the except block is used to print something or do anything else other than throwing an exception
