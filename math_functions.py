# importing the math module
import math

val_one = 2.7
val_two = -5.5553

# something with division of numbers
print(10 / 3)   # returns 3.33333333...

# the double slash always returns the integer (not the float) value of the expression
print(10 // 3)  # returns 3

# round
print(round(val_one))

# absolute
print(abs(val_two))

print("///////////////")
print(math.floor(4.9))  # rounds to the nearest whole number (eliminating the floating points)
print(math.ceil(4.7))   # approximates to the nearest whole number ahead
print(math.pow(val_two, 2))