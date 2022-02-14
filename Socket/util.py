from timeit import default_timer as timer

def timefunc(func):
    def inner(*args, **kwargs):
        start = timer()
        result = func(*args, **kwargs)
        end = timer()
        message = "{} took {} ".format(func.__name__, end - start)
        print(message)
        return result
    return inner
