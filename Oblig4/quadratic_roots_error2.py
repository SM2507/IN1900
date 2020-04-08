"""
Exercise 4.3. Quadratic fixed
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""
from math import sqrt
from sys import argv
def roots(a,b,c):
    if b**2-4*a*c < 0:  # if True, print an error message telling user about complex roots
        print("Error, complex roots")
    else:  
        print((b+sqrt(b**2-4*a*c))/(2*a))
        print((b-sqrt(b**2-4*a*c))/(2*a))

try:  # Same commentary as quadratic_roots_error
    roots(float(argv[1]),float(argv[2]),float(argv[3]))
except IndexError:
    roots(float(input("a = ")), float(input("b = ")), \
float(input("c = ")))

"""
C:Users\moham\IN1900\Oblig4>python quadratic_roots_error2.py
a = 3
b = 1
c = 4
Error, roots not real
"""