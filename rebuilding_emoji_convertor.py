# Rebuilding the Emoji Converter with functions


def emoji_converter(user_input):
    words_in_user_input = user_input.split(" ")
    output = ""
    emoji_store = {
        ":)": "😊",
        ":(": "😔"
    }

    for word in words_in_user_input:
        output += f"{emoji_store.get(word, word)} "

    return output


message = input("Your message here: ")

print(emoji_converter(message))

# print(emoji_converter("Hello there, :)"))
# print(emoji_converter("Hmmmm, :("))
# print(emoji_converter("Hey, Sam"))
# print(emoji_converter("Yo, jack!"))
