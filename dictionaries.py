# Dictionaries  -  used for storing unique key-value pairs

# user = {
#             "first_name": "Ian",
#             "second_name": "Roberts",
#             "email": "ianroberts@mail.co.uk",
#             "country": "UK",
#             "is_registered": True,
#             "user_code": 23409
#         }
#
# # available methods...
# user["title"] = "Mr."
# print(user.items())
# print(user.keys())
# print(user.values())
# print(user["is_registered"])
# # the get method does not throw an error if the stated value does not exist
# # unlike the square bracket method, it simply returns "None"
# print(user.get("tax_id"))
# print(user.get("first_name"))


###------- PHONE GAME
user_input = input("Phone number: ")

digit_store = {
    "0": "Zero",
    "1": "One",
    "2": "Two",
    "3": "Three",
    "4": "Four",
    "5": "Five",
    "6": "Six",
    "7": "Seven",
    "8": "Eight",
    "9": "Nine"
}

feedback = ""

for char in user_input:
    word = digit_store.get(char, "*")
    feedback += f"{word} "

print(feedback)


###-----------------------------

# {
#     {
#         "first_name": "Ian",
#         "second_name:": "Roberts",
#         "email": "ianroberts@mail.co.uk",
#         "country": "UK"
#     },
#     {
#         "first_name": "Joanne",
#         "second_name:": "Andrews",
#         "email": "jandrw20@gooode.org",
#         "country": "ES"
#     },
#     {
#         "first_name": "Meghan",
#         "second_name:": "Markle",
#         "email": "duchessmeghan@royal.co.uk",
#         "country": "CA"
#     }
# }

