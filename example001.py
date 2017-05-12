__author__ = 'fenwk0'
# This is our decorator
# taken from
# https://ains.co/blog/things-which-arent-magic-flask-part-1.html

def simple_decorator(f):
    # This is the new function we're going to return
    # This function will be used in place of our original definition
    def wrapper():
        print ("Entering Function")
        f()
        print ("Exited Function")

    return wrapper

@simple_decorator
def hello():
    print ("Hello World")

hello()
