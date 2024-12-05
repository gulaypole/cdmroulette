import random
def genroulette():
    array = [1] + [0] * 5
    random.shuffle(array)
    return array