"""
Exercise 7.5: Make a class for quadratic functions
Author: Mohammed Shartaz Mostafa
Warning: This task has been delivered in an earlier course by me. 
"""


# Importing numpy
from numpy import linspace,array,sqrt

# Creating the class.
class Quadratic:
    def __init__(self, a, b, c):
        self.a = a; self.b = b; self.c = c
# Value method.
    def value(self, x):
        val = self.a*x**2 + self.b*x + self.c
        return val
# The table method writes the x and f(x) values to a file.
    def table(self, L , R, n):
        x = linspace(L,R,n)
        with open("table.dat", "w") as tab:
            tab.write("f and x values in the interval [L,R] \n")
            tab.write("------------------------------------ \n")
            for i in range(len(x)):
                tab.write("x = %2i                  f(x) = %g \n" \
                %(x[i], self.value(x[i])))

# The roots method returns the roots of our function.
    def roots(self):
        r1 = ((-self.b) + sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a)
        r2 = ((-self.b) - sqrt(self.b**2 - 4*self.a*self.c))/(2*self.a)
        return r1, r2

# This ensures that the functions subjected to the if-statement is only run when the program is run directly,
# not if imported.
if __name__ == "__main__":
    def test_value():
# Calling the class.
        value = Quadratic(a = 1, b = 2, c = 1)
        y = linspace(0,10,11)
        val_exp = array([1., 4., 9., 16., 25., 36., 49., 64., 81., 100., 121.])
        val_com = value.value(y)
        msg = "Error in the value method."
# Compares all the elements in the expected and computed arrays.
        for i in range(len(y)):
            assert val_exp[i] == val_com[i], msg

    test_value()

    def test_roots():
        roots = Quadratic(a = 1, b = 2, c = 1)
        r_exp = (-1.0, -1.0)
        r_com = roots.roots()
        msg = "Error in the roots method."
        assert r_exp == r_com, msg

    test_roots()

# Run program
"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig9>python Quadratic.py

"""
# Demonstration interactive session 1
"""
>>> from Quadratic import Quadratic
>>> G = Quadratic(a = 1, b= 2, c= 1)
>>> from numpy import *
>>> print(G.value(linspace(0,10,11)))
[   1.    4.    9.   16.   25.   36.   49.   64.   81.  100.  121.]
>>> exit()
"""
# Demonstration interactive session 2
"""
>>> from numpy import *
>>> from Quadratic import Quadratic
>>> D = Quadratic(a = 1, b= 2, c = 1)
>>> D.table(0, 10 , 11)
"""
# Print of the table generated:
"""
f and x values in the interval [L,R]
------------------------------------
x =  0                  f(x) = 1
x =  1                  f(x) = 4
x =  2                  f(x) = 9
x =  3                  f(x) = 16
x =  4                  f(x) = 25
x =  5                  f(x) = 36
x =  6                  f(x) = 49
x =  7                  f(x) = 64
x =  8                  f(x) = 81
x =  9                  f(x) = 100
x = 10                  f(x) = 121
"""
