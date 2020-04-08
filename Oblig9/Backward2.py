"""
9.11: Implement a new subclass for differentiation.
Authored by Mohammed Shartaz Mostafa
Warning: This task has been delivered in an earlier course by me. 
"""
#Import
import numpy as np

# Creating a class:
class Diff:
    def __init__(self, f, h=1E-5):
        self.f = f; self.h = h

# Creating a class, based on a parent class; a subclass
# Backward1 is the subclass, and Diff is the parent.
class Backward1(Diff):
    def __call__(self, x, k):
        f = self.f; h = self.h; h = 2**-k
        return (f(x) - f(x-h))/h

class Backward2(Diff):
    def __call__(self, x, k):
        f = self.f; h = self.h; h = 2**-k
        return ((f(x-2.*h)-4.*f(x-h)+3.*f(x))/(2.*h))

def f(x):
    return np.exp(-x)

# Setting variables and calling classes.
x = 0
back_1 = Backward1(f)
back_2 = Backward2(f)

with open("Backward.txt", "w") as outfile:
    outfile.write(" Backward 1    Backward 2      Error B1            Error B2 \n")
    outfile.write("-----------------------------------------------------------------\n")

    for i in range (15):
        outfile.write("%2.7f    %2.7f       %2.11f       %2.11f \n" %(\
back_1(x,i), back_2(x,i), abs(1+back_1(x,i)), abs(1+back_2(x,i))))

"""
(base) C:Users\dorth\Google Drive\PHYSX\PYT\IN1900\Oblig9>python Backward2.py

"""