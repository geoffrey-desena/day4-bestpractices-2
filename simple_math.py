"""
A collection of simple math operations.

Functions
---------
simple_add(a,b) : Return the sum of a and b.
simple_sub(a,b) : Return the difference of a and b.
etc.
etc.
Say no more, say no more.
"""

def simple_add(a,b):
    """Return the sum of a and b."""
    return a+b

def simple_sub(a,b):
    """Return the difference of a and b."""
    return a-b

def simple_mult(a,b):
    """Return the product of a and b."""
    return a*b

def simple_div(a,b):
    """Return the quotient of a and b."""
    return a/b

def poly_first(x, a0, a1):
    """Evaluate a first order polynomial.
    
    Arguments:
    a0 - order 0 constant
    a1 - order 1 constant
    x - value of the variable
    """
    return a0 + a1*x

def poly_second(x, a0, a1, a2):
    """Evaluate a second order polynomial.
    
    Dependencies:
    poly_first(x, a0, a1)
    
    Arguments:
    a0 - order 0 constant
    a1 - order 1 constant
    a2 - order 2 constant
    x - value of the variable
    """
    return poly_first(x, a0, a1) + a2*(x**2)

# Feel free to expand this list with more interesting mathematical operations...
# .....

# I think I'm going to get plenty of practice with this next week.
