def double(x):
    """this is where you put an optional docstring
    that explains what the function does.
    for example, this function multiplies its input by 2"""
    return x * 2


def apply_to_one(f):
    """calls the function f with 1 as its argument"""
    return f(1)
my_double = double # refers to the previously defined function
x = apply_to_one(my_double) # equals 2


another_double = lambda x: 2 * x # don't do this
def another_double(x): return 2 * x # do this instead


def my_print(message="my default message"):
    print (message)
my_print("hello") # prints 'hello'
my_print() # prints 'my default message'


def subtract(a=0, b=0):
    return a - b
subtract(10, 5) # returns 5
subtract(0, 5) # returns -5
subtract(b=5) # same as previous



