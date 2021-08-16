# Tuples  -  for storing elements. Similar to arrays or lists in Python
#            tuples are immutable. they cannot be mutated or modified
#            new elements cannot be added and existing elements
#            cannot be removed
#            they are constructed using parenthesis () instead of square brackets []

users = ("Jones", "Tiberius", "Luigi", "Morgan", "Hudson")

print(users)
print(users[2])
print(users[-2])
# due to their immutability, only few methods work on tuples
print(users.count("Tiberius"))
print(users.index("Luigi", 0, 3))
