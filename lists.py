# users = ["Arthur", "Joanne", "Anne", "Thawne", "Lawren", "Anne"]
#
# print(users)
# print(users[2])
# print(users[-1])
# print(users[0:3])
# print(users[1:])
# print(users[:3])
# print(users.count("Anne"))
# print(users.count("Arthur"))
#
# # users.clear()
# # users.remove("Anne")
# phoneUsers = users.copy()
# phoneUsers.pop(2)
# phoneUsers.append("Chester")
# print(phoneUsers)
#
#
# users.reverse()
# print(users)
#
# users.sort()
# print(users)
# print(users.clear())

# Finding the largest number in an array

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

