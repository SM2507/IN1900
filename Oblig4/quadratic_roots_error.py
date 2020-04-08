"""
Exercise 4.2: Quadratic with exceptions
Author: Mohammed Shartaz Mostafa
"""
from sys import argv

def roots(a,b,c):  # Same commentary as in quadratic_roots_input
    if b**2-4*a*c < 0:
        from cmath import sqrt
    else:
        from numpy import sqrt
    print((b+sqrt(b**2-4*a*c))/(2*a))
    print((b-sqrt(b**2-4*a*c))/(2*a))

try:  # Try taking arguments from the command line
    roots(float(argv[1]),float(argv[2]),float(argv[3]))
except IndexError:  # If IndexError, take arguments as user input
    roots(float(input("a = ")), float(input("b = ")), \
float(input("c = ")))

"""
C:Users\moham\IN1900\Oblig4>python quadratic_roots_error.py
a = 1
b = 2
c = 3
(1+1.4142135623730951j)
(1-1.4142135623730951j)
"""
