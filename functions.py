# FUNCTIONS

# positional arguments

def greet(name):
    print(f"Hello, {name}. Welcome to our world.")


greet("Jacqueline")
greet("Xin Ping")
greet("Ukechuwkwu Amakande")

print("* " * 30)

# keyword arguments

def user_stats(first_name, last_name, age, gender, height):
    print(f'Welcome, {first_name} {last_name}. You are a {height}m tall, {age} year-old {gender}.')


user_stats(last_name="Johnson", age=45, first_name="Ezekiel", height=5.5, gender="male")
user_stats(first_name="Dorothy", last_name="Arthur", gender="female", height=4.8, age=28)

print("* " * 30)

# returning functions

def do_the_math(first, second):
    return first * second


print(do_the_math(34, second=50))
print(do_the_math(2, 5))
print(do_the_math(70223000000034352123234242000000000, 3456670000000000000003343112211309000000000))

# NOTE: By default, all functions in Python return the value "None"
# which is the "null" equivalent in JS and Java
