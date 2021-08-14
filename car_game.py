user_input = ""
started = False

while True:
    user_input = input("> ").upper()

    if user_input == "HELP":
        print("""Here are a few commands for this game
Type
start - to start the car
stop  - to stop the car
quit  - to exit the game
""")

    elif user_input == "START":
        if not started:
            started = True
            print("Car started... Ready to go")
        else:
            print("Hey... the car is already started...")

    elif user_input == "STOP":
        if started:
            started = False
            print("Car stopped... In parking mode")
        else:
            print("Hey... the car is stopped already")

    elif user_input == "QUIT":
        break

    else:
        print("""Sorry, I don't get that...
Type 'help' for more information
""")

