class Insect:
    def fly(self):
        print("Flying...")

    def metamorphose(self):
        print("Metamorphosing...")


class Bee(Insect):
    def __init__(self, name):
        self.name = name

    def introduce(self):
        print(f"I am a {self.name}")


class DragonFly(Insect):
    def __init__(self, name, stage):
        self.name = name
        self.stage = stage

    def describe(self):
        print(f"I am a/an {self.stage} {self.name}")


class Moth(Insect):
    # use the "pass" keyword to skip the content of anything eg. class, objects, etc
    pass


insect = Insect()
insect.fly()
insect.metamorphose()

bee = Bee("Bee")
bee.introduce()
bee.fly()
bee.metamorphose()

dragon_fly = DragonFly("Dragon Fly", "adult")
dragon_fly.describe()
dragon_fly.fly()
dragon_fly.metamorphose()

moth = DragonFly("Moth", "young")
moth.describe()
moth.fly()
moth.metamorphose()
