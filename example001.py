import timeit

__author__ = 'fenwk0'
# This is our decorator
# taken from
# https://ains.co/blog/things-which-arent-magic-flask-part-1.html
# see also

# https://www.thecodeship.com/patterns/guide-to-python-function-decorators/


def time_decorator(f):
    # This is the new function we're going to return
    # This function will be used in place of our original definition
    def wrapper():
        start = timeit.default_timer()

        print("Start Time: ", start)
        f()
        print("Time taken: ", timeit.default_timer() - start)

    return wrapper


def simple_decorator(f):
    # This is the new function we're going to return
    # This function will be used in place of our original definition
    def wrapper():
        print("Entering Function")
        f()
        print("Exited Function")

    return wrapper


@time_decorator
@simple_decorator
def hello():
    print("Hello World")

hello()
