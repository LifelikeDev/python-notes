is_a_person = True
knows_about_programming = False
knows_a_programming_language = True

# logical AND operator in Py is represented with the 'and' keyword
# logical OR operator in Py is represented with the 'or' keyword
# logical NOT operator in Py is represented with the 'not' keyword


if is_a_person:
    if knows_a_programming_language and knows_about_programming:
        print("You can build software")
    elif knows_a_programming_language or knows_about_programming:
        print("You can code")
    elif not knows_about_programming and not knows_a_programming_language:
        print("You should learn programming")
    elif knows_about_programming and not knows_a_programming_language:
        print("You should a programming language some time")
    else:
        print("Sorry. You're currently not up for the challenge")
else:
    print("Aliens are not involved!!!")


