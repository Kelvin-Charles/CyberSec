import random

# Decorators with arguments

def power_of(exponent):

    # Meta decorator
    def decorator(func):

        def inner():

            return func() ** exponent

        return inner

    return decorator



@power_of(2)
def random_odd_digits():

    return random.choice([1, 3, 5, 7, 9])

print(random_odd_digits())


