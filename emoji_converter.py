# Assuming all emojis in a sentence are inserted at the end of the sentence

user_message = input("> ")

message_store = user_message.split(" ")

emoji = message_store[-1]

emoji_store = {
    ":(": "😔",
    ":)": "😊"
}

new_message = user_message.replace(emoji, emoji_store.get(emoji, "*"))

print(new_message)