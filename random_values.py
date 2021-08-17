import random

for i in range(30):
    rand = round(random.randint(1, 10))
    # print(rand)

garage = ["G-Wagon", "Ferrari", "Lamborghini", "Bugatti", "F150", "Bentley", "Cardilac"]

today_pick = random.choice(garage)

# print(today_pick)


# DICE ROLLER

class DiceRoller:
    outcomes = (1, 2, 3, 4, 5, 6)
    first_choice = random.choice(outcomes)
    second_choice = random.choice(outcomes)

    def roll(self):
        print(f"Dice outcome: ({self.first_choice}, {self.second_choice})")



dice = DiceRoller()
dice.roll()
