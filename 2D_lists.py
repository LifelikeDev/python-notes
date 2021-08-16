groups = [[3, 4, 5, 8, 2], [21, 34, 67, 90, 74], [102, 131, 165, 149, 110], [6245, 2367, 5588, 8721, 9402]]

print(groups)
print(len(groups))
print("* * " * 8)

for group in groups:
    print(group)
    for member in group:
        print(member)
    print("* * " * 4)


print("* * " * 4)



