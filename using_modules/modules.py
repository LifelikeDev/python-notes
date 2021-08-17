# Modules  -   simply files with code that perform a specific function
from using_modules import converters

# or for single exports,
#       from converters import pounds_to_kilograms
#       from converters import kilograms_to_pounds


def converter():
    unit = input('''Type "kg" to convert to kilograms or "lbs" to convert to pounds
''')
    user_input = ""
    output = ""
    output_unit = ""
    converter_function = ""

    if unit == "lbs":
        user_input = float(input("""Enter a weight in kilograms to be converted into pounds
"""))
        converter_function = converters.kilograms_to_pounds(user_input)
        output_unit = "kg"

    elif unit == "kg":
        user_input = float(input("""Enter a weight in pounds to be converted into kilograms
"""))
        converter_function = converters.pounds_to_kilograms(user_input)
        output_unit = "lbs"

    if unit == "kg" or unit == "lbs":
        output = f'{user_input} {output_unit} is equivalent to {converter_function} {unit}'
    else:
        print("Invalid input. Please try again...")

    return output


print(converter())
