import random

# Decorators with arguments

def power_of_2(func):

    def inner():

        return func() ** 2

    return inner

@power_of_2
def random_odd_digits():

    return random.choice([1, 3, 5, 7, 9])

print(random_odd_digits())


