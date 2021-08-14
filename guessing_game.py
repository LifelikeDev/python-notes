### GUESSING GAME

### METHOD ONE
# actual_num = 8
# no_of_tries = 1
# user_input = 0
#
# print("Welcome to a Guessing Game...")
#
# while no_of_tries > 0:
#     # print(no_of_tries)
#
#     if user_input != actual_num:
#         if no_of_tries < 4:
#             user_input = int(input("Guess and enter a number: "))
#         else:
#             print("You lost. Game Over!!!")
#             break
#     else:
#         print(f"You won. The correct number is {user_input}")
#         break
#     no_of_tries += 1


### METHOD TWO

actual_number = 8
allowed_guesses = 3
guess_count = 0

print("Welcome to a Guessing Game...")

while guess_count < allowed_guesses:
    guessed_number = int (input("Guess and enter a number: "))
    guess_count += 1
    print(guess_count)

    if guessed_number == actual_number:
        print(f"You won. The number is {actual_number}")
        break

else:
    print("You lost. Game Over!!!")