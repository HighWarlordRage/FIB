#Title: Project-4b

#Defining the function
def fib(a):
    """ A function named fib that takes a positive integer parameter
    And returns the number at that position of the Fibonacci sequence."""
    if a == 1:
        return 1

    elif a == 2:
        return 1

    else:
        return fib(a - 1) + fib(a - 2)

#print(fib(10))