"""
Exercise 4.1. Quadratic with user input
Author: Mohammed Shartaz Mostafa (python 3.6.5)
"""
def roots(a,b,c):  # Defining the function
    if b**2-4*a*c < 0:  # Using the if statement to check if we get a complex number
        from cmath import sqrt  # if True, import complex sqrt
    else:
        from numpy import sqrt  # if not, import real sqrt
    print((b+sqrt(b**2-4*a*c))/(2*a))
    print((b-sqrt(b**2-4*a*c))/(2*a))

roots(float(input("a = ")), float(input("b = ")), \
float(input("c = ")))  # Takes arguments as user input
"""
C:Users\moham\IN1900\Oblig4>python quadratic_roots_input.py
a = 1
b = 2
c = 1
1.0
1.0
"""