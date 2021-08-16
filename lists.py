users = ["Arthur", "Joanne", "Anne", "Thawne", "Lawren", "Anne"]

print(users)
print(users[2])
print(users[-1])
print(users[0:3])
print(users[1:])
print(users[:3])
print(users.count("Anne"))
print(users.count("Arthur"))

# users.clear()
# users.remove("Anne")
phoneUsers = users.copy()
phoneUsers.pop(2)
phoneUsers.append("Chester")
print(phoneUsers)


users.reverse()
print(users)

users.sort()
print(users)
print(users.clear())

###------------- Finding the largest number in an array

figures = [23, 5, 67.9, 10, 4, 5.3, 2, 19, 34, 89, 88, 121]

largestNum = 0
index = 0

# while index < len(figures):
#     current = figures[index]
#
#     if current > largestNum:
#         largestNum = current
#
#     index += 1

# print(largestNum)

############ OR  (much better - shorter code version)

for figure in figures:
    if figure > largestNum:
        largestNum = figure

print(largestNum)

##--------------- REMOVE DUPLICATES IN A LIST
random_list = [3, 4, 5, 6, 7, 8, 8, 2, 3, 9, 1, 2, 23, 5, 7]

# choosing to sort the list before removing duplicates
random_list.sort()
duplicates = []

#------- METHOD 1
for item in random_list:
    if random_list.count(item) > 1:
        # push duplicate item to the duplicates list
        duplicates.append(item)
        # remove any duplicate item in the list
        random_list.remove(item)

print(random_list)
print(duplicates)

#------- METHOD 2
uniques = []

for item in random_list:
    if item not in uniques:
        uniques.append(item)

print(uniques)
print(random_list)
