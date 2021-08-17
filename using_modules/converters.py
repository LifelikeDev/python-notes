constant = 0.48

def pounds_to_kilograms(weight):
    return round((weight * constant), 2)


def kilograms_to_pounds(weight):
    return round((weight / constant), 2)
